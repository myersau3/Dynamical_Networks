

.. automodule:: dynamical_networks.analysis.statistics
    :members:

The following is an example::

    from dynamical_networks.analysis.statistics import centrality, capacity, node_degree_distribution, betweenness
    from dynamical_networks.simulate.PG_network import PG_network
    A = PG_network()
    S = [centrality(A), capacity(A), node_degree_distribution(A), betweenness(A)]

