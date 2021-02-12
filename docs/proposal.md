# Modeling Coupled Dynamical Systems Using Complex Networks
### By Audun Myers

<p align="center">
  <img src="images/coupled_dyn_sys_network.png" width="250">
</p> <em>Example coupled dynamical system represented using a complex network with each node as a state variable's dynamics and edges weighted between coupled variables.</em>

## Overview

This software package provides code for analyzing and modeling coupled dynamical systems through complex networks networks. Coupled dynamical systems are present in many physical, biological, and social dynamical systems. This package will provide both data sets for these catagories as well as new and commonly used tools to analyze the resulting complex networks.

Specifically, this package will provide code for reproducing network representation methods and data sets used for modeling complex coupled dynamical systems such as Manufacturer-Supplier systems [[1]](#1). Additionally, the package will host both new and existing tools for analyzing these networks. These tools will range from traditional techniques to to more advanced topology based analysis methods [[2]](#2).

## Program Description

This software will build on existing theory and methods [[1]](#1) for modeling and analyzing coupled dynamical systems as complex networks. Additionally, it will provide data generation methods for several coupled dynamical system models. More specifically, I plan to first write simulation code for generating data from coupled dynamical system models to be used in creating complex network representations. After this, I plan to develop and reproduce methods for generating complex networks from the simulations and methods for analyzing the resulting networks.

## Project Goals and Timeline

Throughout the project I will work on developing documentation for both code functionality and the methods reproduced and developed in this work. However, here are some of the specific short and long term goals I have:

#### Short Term Goals:
- Program atleast three coupled dynamical systems for simulations including the supplier-manufacturer system in [[1]](#1).
- Read more about current methods for creating networks from coupled dynamical systems.

#### Mid Term Goals:
- Program functions to generate complex networks from coupled dynamical systems.
- Read about and reproduce methods for analyzing complex networks from coupled dynamical systems.

#### Long Term Goals:
- Develop novel methods for analyzing these complex networks.

## Anticipating Challenges

#### Needed skills:
I already have experience with documentation using sphinx so I am not concerned about that portion. However, I am concerned about how much time it will take to learn about existing methods and reproducing the results. 

#### Challenges:
A major challenge for me will be immersing myself in the field of network representations of complex networks. While I have experience with graph theory, I have not researched methods for generating complex networks from coupled dynamical system data and forsee this being a challenge. If I am unable to make as much progress on researching current methods, I will focus on a single model (probably supplier-manufacturer coupled dynamical systems) and only the basic tools to analyze them. I hope I can do much more than this though.

#### Deviations
I do not plan for my project to use any other language than Python. I do hope to incorporate outside packages (e.g. network analysis packages such as networkx) whenever possible.


## References
<a id="1">[1]</a> 
MengkaiXu, Srinivasan Radhakrishnan, Sagar Kamarthi and Xiaoning Jin (2019). 
Resiliency of Mutualistic SupplierManufacturer Networks. 
Scientific Reports, Nature Research.

<a id="1">[2]</a> 
Zixuan Cang, Elizabeth Munch, and Guo-Wei Wei (2019). 
Evolutionary homology on coupled dynamical systems. 
Journal of Applied and Computational Topology, Springer.
