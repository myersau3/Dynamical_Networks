# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 16:56:42 2021

@author: myersau3
"""
def degree_matrix(A):
    import numpy as np
    n = len(A[0]) #get degree of graph
    d = np.sum(A, axis = 1) #get degree vector from graph
    D = np.zeros((n,n)) #initialize degree matrix as zeros
    np.fill_diagonal(D, d) #fill diagonal with degree vector
    return D

def graph_laplacian(A):
    A = np.array(A)
    D = degree_matrix(A) #get degree matrix from adjacency matrix
    L = D - A #difference between degree matrix and adjacency matrix is graph laplacian
    return L

def lorenz(u1, u2, u3, parameters):
    rho, sigma, beta = parameters
    u1_dot = sigma*(u2 - u1)
    u2_dot = u1*(rho-u3) - u2
    u3_dot = u1*u2 - beta*u3
    return np.array([u1_dot, u2_dot, u3_dot])

def coupled_lorenz_system(t, A, Tau, U_0, parameters, eps):
    U = U_0
    N = len(A[0])
    import numpy as np
    dt = np.mean(np.diff(t))
    Us=[U]
    for t_i in range(len(t)):
        G_u = []
        for u in U:
            g_u_i = lorenz(u[0], u[1], u[2], parameters)
            G_u.append(g_u_i)
        G_u = np.array(G_u)
        dU = G_u + eps*np.matmul(A,U)
        U = U + dU*dt
        Us.append(U)
    Us = Us[:-1]
    return np.array(Us)
        
    
    
    

# In[ ]:


if __name__ == '__main__':
    import numpy as np
    import matplotlib.pyplot as plt
    #NxN adjacency matrix decribing influence between systems
    N = 5
    A = np.random.rand(N,N)-0.5
    A = A + A.T
    np.fill_diagonal(A,0)
    #A[A>0.5] = 1
    
    #nxn linking matrix
    n = 3
    Tau = np.zeros((n,n))
    Tau[1][0] = 1
    
    #Nxn initial conditions matrix
    U_0 = np.random.rand(N,n)-0.5
    #U_0 = np.zeros((N,n))
    #U_0[0][0] = 1
    
    #parameters for lorenz
    parameters = [60,10,8/3]\
    
    #set time of solution
    T = 400
    fs = 100
    t = np.linspace(0,T,fs*T)
    
    eps = 0.4
    
    U = coupled_lorenz_system(t, A, Tau, U_0, parameters, eps)

    xs = U.T[0]
    ys = U.T[1]
    zs = U.T[2]
    keep_time = 80
        
    
    for i in range(N):
        plt.plot(t[-fs*keep_time:], xs[i][-fs*keep_time:])
    plt.show()
            
            
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    