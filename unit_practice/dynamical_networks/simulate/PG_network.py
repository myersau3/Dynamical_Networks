from __future__ import print_function, division

"""
Power-Grid Dynamical Network Simulation.
=======================================================================

This function simulates a Power-Grid (PG) dynamical network.
"""

def PG_network():
    """This function simulates and returns a power grids network through the adjacency matrix over time t.

    Args:
       t (array): time array

    Kwargs:
       plotting (bool): Plotting for user interpretation. defaut is False.

    Returns:
       (matrix): A, an n by n matrix A over time t.

    """
    
    import pypsa
    import numpy as np
    
    network = pypsa.Network()
    
    #add three buses
    n_buses = 20
    
    for i in range(n_buses):
        network.add("Bus","My bus {}".format(i),
                    v_nom=20.)
    
    #add three lines in a ring
    for i in range(n_buses):
        network.add("Line","My line {}".format(i),
                    bus0="My bus {}".format(i),
                    bus1="My bus {}".format((i+1)%n_buses),
                    x=0.1,
                    r=0.01)
    
    #add a generator at bus 0
    network.add("Generator","My gen",
                bus="My bus 0",
                p_set=100,
                control="PQ")
    
    network.add("Load","My load",
            bus="My bus 1",
            p_set=100)
    
    network.loads.q_set = 100.
    
    
    x = network.pf()
    print(network.lines_t.p0)
    
    import numpy as np
    As = []
    for i in range(100):
        A = np.zeros((10,10))
        As.append(A)
    
    
    return np.array(As)


# In[ ]:


if __name__ == '__main__':
    from dynamical_networks.simulate.PG_network import PG_network
    A = PG_network()
    
    