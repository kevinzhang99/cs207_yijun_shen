def k_const(k):
    """Returns the constant reaction rate coefficients
    
    INPUTS
    ======
    k: float, constant reaction rate coefficient
    
    RETURNS
    =======
    constant reaction rate coefficients, which is k
    
    EXAMPLES
    ========
    >>> k_const(1.5)
    1.5
    """
    k1 = k
    return k1

def k_arr(A, E, T, R=8.314):
    """Returns Arrhenius reaction rate coefficients
    
    INPUTS
    ======
    A: float, the Arrhenius prefactor, strictly positive
    E: float, a parameter
    T: float, temperature using a Kelvin scale, strictly positive
    R: float, default value is 8.314 which is the ideal gas constant. 
        R should not be changed except to convert units
    
    RETURNS
    =======
    Arrhenius reaction rate coefficients: a float
        a ValueError exception is raised if A <= 0
        a ValueError exception is raised if T <= 0
    Raise OverflowError if the result is beyond the maximum representable finite float
    Raise UnderflowError if the result is below the minimum positive normalized float
        since A, T and exponential function are all strictly positive,
        only consider positive overflow and positive underflow
    
    EXAMPLES
    ========
    >>> k_arr(10**7, 10**3, 10**2)
    3003549.0889639612
    """
    import numpy as np
    import sys
    if A <= 0:
        raise ValueError("The Arrhenius prefactor must be strictly positive.")
    if T <= 0:
        raise ValueError("Temperature must be strictly positive.")
    k2 = A * np.exp(-E / (R*T))
    if k2 > sys.float_info.max:
        raise OverflowError("Arrhenius coefficients overflow.")
    if k2 < sys.float_info.min:
        raise UnderflowError("Arrhenius coefficients underflow.")
    return k2

def k_modarr(A, b, E, T, R=8.314):
    """Returns the modified Arrhenius reaction rate coefficients.
    
    INPUTS
    ======
    A: float, the Arrhenius prefactor, strictly positive
    b: float, a parameter, must be real
    E: float, a parameter
    T: float, temperature using a Kelvin scale, strictly positive
    R: float, default value is 8.314 which is the ideal gas constant. 
        R should not be changed except to convert units
    
    RETURNS
    =======
    Modified Arrhenius reaction rate coefficients: a float
        a ValueError exception is raised if A <= 0
        a ValueError exception is raised if T <= 0
        a ValueError exception is raised if b is not real.
    Raise OverflowError if the result is beyond the maximum representable finite float
    Raise UnderflowError if the result is below the minimum positive normalized float
        since A, T and exponential function are all strictly positive,
        only consider positive overflow and positive underflow
    
    EXAMPLES
    ========
    >>> k_modarr(10**7, 0.5, 10**3, 10**2)
    30035490.889639609
    """
    import numpy as np
    import sys
    if A <= 0:
        raise ValueError("The Arrhenius prefactor must be strictly positive.")
    if T <= 0:
        raise ValueError("Temperature must be strictly positive.")
    if np.iscomplex(b):
        raise ValueError("The parameter b must be real.")
    k3 = A * (T**b) * np.exp(-E / (R*T))
    if k3 > sys.float_info.max:
        raise OverflowError("Arrhenius coefficients overflow.")
    if k3 < sys.float_info.min:
        raise UnderflowError("Arrhenius coefficients underflow.")
    return k3