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
    
    