# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 14:02:55 2021

@author: myersau3
"""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__),'..'))
from analysis import evolutionary_homology # centrality, capacity, node_degree_distribution, betweenness

import pytest
import numpy as np 


def test_statistics_list_for_A():
    # test to make sure a list of lists for A does not work
    A = [[[0,0],[1,1]], [[0,0],[1,1]]]
    with pytest.raises(TypeError) as excinfo:
        evolutionary_homology.EveHom(A)

        
        
def test_statistics_for_size_of_A():
    # test to make sure a list of lists for A does not work
    A = np.array([[0,0],[1,1]])
    with pytest.raises(TypeError) as excinfo:
        evolutionary_homology.EveHom(A)

        
def test_statistics_correct_output():
    # test if function returns numpy array for good input file.
    A = np.array([[[0,0],[1,1]], [[0,0],[1,1]]])
    S = evolutionary_homology.EveHom(A)
    assert type(S) == np.ndarray
