from __future__ import print_function, division

"""
Power-Grid Dynamical Network Simulation.
=======================================================================

This function simulates a Power-Grid (PG) dynamical network.
"""
def PG_steady_state(N, P, K):
    """ Find steady state solution for given network
        
    The default parameters are for the first example in the results section.
    """
    import numpy as np
    from scipy.optimize import minimize
    omega_ss = np.zeros((N,))
    theta_ss = np.zeros((N,))
    def cost_function(theta_ss):
        cost = []
        for i in range(N):
            cost_i = P[i]
            for j in range(N):
                cost_i += K[i][j]*np.sin(theta_ss[j] - theta_ss[i])
            cost.append(cost_i)
        return np.sum(np.array(cost)**2)
    res = minimize(cost_function, x0 = theta_ss, method='Nelder-Mead', tol=1e-6)
    theta_ss = res.x
    return theta_ss, omega_ss
    
def PG_flows(theta, omega, K, N):
    """ Calculates flows from theta and omega of steady state
    """
    import numpy as np
    F = np.zeros((N,N))
    for i in range(N):
        for j in range(N):
            F[i][j] = K[i][j]*np.sin(theta[j] - theta[i])
    return F

def get_edge_list(A):
    """ From adjacency matrix go to list of edges.
    """
    import numpy as np
    A_ut = np.triu(A)
    E = []
    for i in range(len(A_ut)):
        for j in range(len(A_ut[i])):
            if A_ut[i][j] != 0:
                E.append([i,j])
    return np.array(E)
    
def PG_network(A, t, V_gen, V_con, K_0 = 1.63, P_gen = 1.5, P_con = 1, alpha = 0.6, I_0 = 1,
                  damping = 0.5):
    """This function simulates and returns a power grids network through the adjacency matrix over time t.

    Args:
       t (array): time array

    Kwargs:
       plotting (bool): Plotting for user interpretation. defaut is False.

    Returns:
       (matrix): A, an n by n matrix A over time t.

    """
    
    import networkx as nx
    import numpy as np

    A_0 = np.copy(A) #use copy of adjacency matrix for plotting all the flows
    E = get_edge_list(A)

    def swing_equation(omega, theta):
        d_theta, d_omega = np.zeros((N,)), np.zeros((N,))
        for i in range(N):
            d_theta[i] = omega[i]
            d_omega[i] = P[i] - G[i]*omega[i]
            for j in range(N):
                d_omega[i] = d_omega[i] + K[i][j]*np.sin(theta[j] - theta[i])
                #I believe the authors used A[i][j] here instead of K[i][j] as they state in their equations.
            d_omega[i] = d_omega[i]/I[i]
        return d_theta, d_omega
    
    
    G = nx.convert_matrix.from_numpy_matrix(A)
    N = G.number_of_nodes()
    
    P = np.zeros((N,)) 
    P[V_gen] = P_gen
    P[V_con] = -P_con
    
    K = K_0*A
    I = np.zeros((N,)) + I_0 #inertia of power generators
    G = np.zeros((N,)) + damping #damping of rotary machine
    C = alpha*K
    
    
    
    #get new steady state values
    
    
    theta, omega = PG_steady_state(N, P, K)
    Fs = []
    dt = t[1]-t[0]
    for t_i in t:
        
        e_kill = (1,3)
        if t_i > 1: # remove line 4-2 at 1 second
            K[e_kill[0]][e_kill[1]], K[e_kill[1]][e_kill[0]] = 0, 0
            
        d_theta, d_omega = swing_equation(omega, theta)
        theta, omega = theta+d_theta*dt, omega+d_omega*dt
        F = PG_flows(theta, omega, K, N)
        
        for e in E:
            if np.abs(F[e[0],e[1]]) > C[e[0],e[1]]: # if flow is greater than line capacity
                K[e[0]][e[1]], K[e[1]][e[0]] = 0, 0
            
        flows = []
        for e in E:
            flows.append(np.abs(F[e[0], e[1]]))
        Fs.append(flows)
        
    Fs = np.array(Fs).T  
    
    return Fs, E


# In[ ]:


if __name__ == '__main__':
    #from dynamical_networks.simulate.PG_network import PG_network
    
    import matplotlib.pyplot as plt
    import numpy as np
    
    t = np.linspace(0,12, 5000)
    P_gen = 1
    P_con = 2
    K_0 = 1.63
    I_0 = 1 
    damping = 0.5
    alpha = 0.6
    V_gen = np.array([1, 4]) #vertices indices of generates and consumers
    V_con = np.array([0, 2, 3])
    A = np.array([[0, 1, 1, 0, 1],
                  [1, 0, 1, 1, 0],
                  [1, 1, 0, 1, 0],
                  [0, 1, 1, 0, 1],
                  [1, 0, 0, 1, 0]])
    
    
    
    Fs, E = PG_network(A, t, V_gen, V_con, K_0, P_gen, P_con, alpha, I_0, damping)
    
    
    #---------------PLOTTING-------------------
    
    plt.figure(figsize = (10,5))
    TextSize = 35
    for i in range(len(Fs)):
        plt.plot(t, Fs[i], label = '$('+str(E[i][0]+1)+','+str(E[i][1]+1)+')$')
    plt.plot([0,max(t)], [alpha*K_0, alpha*K_0], 'k--')
    
    plt.grid()
    plt.xlim(0,max(t))
    plt.ylim(0,)
    plt.xticks(size = TextSize)
    plt.yticks(size = TextSize)
    plt.xlabel(r'$t$', size = TextSize)
    plt.ylabel(r'$|F_{i,j}|$', size = TextSize)
    plt.legend(loc = 'upper right', fontsize = TextSize-12, ncol = 1)
    plt.show()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    