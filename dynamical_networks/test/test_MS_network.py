# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 14:02:55 2021

@author: myersau3
"""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__),'..'))
from analysis import statistics # centrality, capacity, node_degree_distribution, betweenness

import pytest
import numpy as np 


