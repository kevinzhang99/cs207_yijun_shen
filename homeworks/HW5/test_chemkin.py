import chemkin
import numpy as np

def test_list_type():
    try:
        chemkin.progress_rate1([2.0, 1.0, 0.0], ["", "green", "hi"], 10)
    except TypeError as err:
        assert(type(err) == TypeError)
        
def test_list_length():
    try:
        chemkin.progress_rate1([2.0, 1.0], [1.0, 2.0, 3.0], 10)
    except ValueError as err:
        assert(type(err) == ValueError)

def test_progress1_types():
    try:
        chemkin.progress_rate1([2.0, 1.0, 0.0], ["", "green", "hi"], 10)
    except TypeError as err:
        assert(type(err) == TypeError)

def test_progress2_types():
    try:
        chemkin.progress_rate2(np.array([[1.0, 2.0, 0.0],[2.0, 0.0, 2.0]]),np.array([[0.0, 0.0, 2.0], [0.0, 1.0, 1.0]]),\
                                ["", "green", "hi"], [10,10])
    except TypeError as err:
        assert(type(err) == TypeError)
        
def reaction_rate():
    try:
        chemkin.reaction_rate(np.array([[1.0, 2.0, 0.0],[2.0, 0.0, 2.0]]),np.array([[0.0, 0.0, 2.0], [0.0, 1.0, 1.0]]),\
                                ["", "green", "hi"], [10,10])
    except TypeError as err:
        assert(type(err) == TypeError)