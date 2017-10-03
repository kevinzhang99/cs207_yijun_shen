def progress_rate1(v_i, x, k):
    """Returns the progress rate for a reaction (v_A)A+(v_B)B --> (v_C)C
    
    INPUTS
    ====== 
    v_i: a list of floats representing Stoichiometric coefficients of reactants
        ordered according to the reaction form, left to right
    x: a list of floats representing the concentration of each reactant and product
        ordered according to the reaction form, left to right
    k: float, reaction rate coefficient
        
    RETURNS
    =======
    progress rate for the reaction: a float
    
    EXAMPLES
    ========
    >>> progress_rate1([2.0, 1.0, 0.0], [1.0, 2.0, 3.0], 10)
    20.0
    """
    r=1
    
    if (len(v_i) != len(x)):
        raise ValueError("Lengths do not match.")
    
    for v, xi in zip(v_i, x):
        r *= xi**v
    w = k*r
    
    return w

def progress_rate2(v_ij1, v_ij2, x, k):
    """Returns the progress rate for a system of reactions of the following form:
        (v_11')A + (v_21')B --> (v_31'')C
        (v_12')A + (v_32')C --> (v_22'')B + (v_32'')C

    INPUTS
    =======
    v_ij1: a numpy array of floats, representing the stoichiometric coefficient of reactnat i in reaction j
    v_ij2: a numpy array of floats, representing the stoichiometric coefficient of product i in reactio j
    x: a list of floats representing the concentration of each reactant and product
    k: float, reaction rate coefficient
    
    RETURNS
    =======
    progress rate for the system of reactions: a list of floats [w1, w2, ..., wj]
        wj is the progress rate for reaction j
    
    EXAMPLES:
    >>> import numpy as np
    >>> progress_rate2(np.array([[1.0, 2.0, 0.0],[2.0, 0.0, 2.0]]),np.array([[0.0, 0.0, 2.0], [0.0, 1.0, 1.0]]), [1.0,2.0,1.0], [10,10])
    [40.0, 10.0]

"""
    import numpy as np
    
    if (np.shape(v_ij1)[1] != len(x)):
        raise ValueError("Lengths do not match.")
    if (np.shape(v_ij2)[1] != len(x)):
        raise ValueError("Lengths do not match.")
    
    w_list = []
    each_reaction = np.vsplit(v_ij1,1)[0].tolist()
    for n in range(0, len(each_reaction)):
        r = 1
        for v, xi, ki in zip(each_reaction[n], x, k):
            r *= (xi**v)
            w = ki * r
        w_list.append(w)
    return w_list

def reaction_rate(v_ij1, v_ij2, x, k):
    """Returns the reaction rate for a system of reactions of the following form:
        (v_11')A + (v_21')B --> (v_31'')C
        (v_32')C --> (v_12'')A + (v_22'')B 
        
    INPUTS
    =======
    v_ij1: a numpy array of floats, representing the stoichiometric coefficient of reactnat i in reaction j
    v_ij2: a numpy array of floats, representing the stoichiometric coefficient of product i in reactio j
    x: a list of floats representing the concentration of each reactant and product
    k: a list of floats, reaction rate coefficient for each reaction
    
    RETURNS
    =======
    reaction rate for the system of reactions: a list of floats [f1, f2, ..., fi]
        fj is the reaction rate for specie i
    
    EXAMPLES:
    >>> import numpy as np
    >>> reaction_rate(np.array([[1.0, 2.0, 0.0], [0.0, 0.0, 2.0]]), np.array([[0.0, 0.0, 1.0], [1.0, 2.0, 0.0]]), [1.0,2.0,1.0], [10,10])
    [-30.0, -60.0, 20.0]

"""
    import numpy as np
    
    if (np.shape(v_ij1)[1] != len(x)):
        raise ValueError("Lengths do not match.")
    if (np.shape(v_ij2)[1] != len(x)):
        raise ValueError("Lengths do not match.")
    
    v_ij = v_ij2 - v_ij1
    f_list = []
    if v_ij.ndim > 1:
        w_list = progress_rate2(v_ij1, v_ij2, x, k)
        component = np.vsplit(np.transpose(v_ij),1)[0].tolist()
        for n in range(0, len(component)):
            f = 0
            for i in range(0, len(w_list)):
                f += component[n][i] * w_list[i]
            f_list.append(f)
    
    if v_ij.ndim == 1:
        w_list = progress_rate1(v_ij1, x, k)
        component = v_ij.tolist()
        for i in range(0, len(w_list)):
            f_list.append(v_ij[i] * w_list[i])
    return f_list