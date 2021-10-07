#!/usr/bin/python3
"""Module that creates a function
that multiples two matrix with
module numpy"""


import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Function that returns the mul of
    two matrices using the module numpy"""

    return (np.matmul(m_a, m_b))
