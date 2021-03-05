"""
Evolutionary homology calculation for dynamical networks.
=======================================================================

This functions calculates the evelutionary homology of a dynamical networks adjacency matrix.
"""

def EveHom(A):
    """This function takes the time varying adjacency matrix and returns the evolutionary homology.

    Args:
       A (array): Time varying adjacency matrix.

    Kwargs:
       plotting (bool): Plotting for user interpretation. defaut is False.

    Returns:
       (array): Statistic array over time.

    """

    import numpy as np
    statistic = []
    for a in A:
        stat = np.nanmax(a)
        statistic.append(stat)
    
    return np.array(statistic)


# In[ ]:


if __name__ == '__main__':
    
    from dynamical_networks.analysis.evolutionary_homology import EveHom
    from dynamical_networks.simulate.PG_network import PG_network
    A = PG_network()
    S = EveHom(A)



