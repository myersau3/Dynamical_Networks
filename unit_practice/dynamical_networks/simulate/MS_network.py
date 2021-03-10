"""
Manufacturer-Supplier Dynamical Network Simulation.
=======================================================================

This function simulates a Manufacturer-Supplier (MS) dynamical network.
"""

def MS_simulation(t, parameters):
    """This function takes system parameters to develop a time dependent throughput simulation of manufacturers and suppliers.

    Args:
       parameter (float):  system parameter or parameters.
       t (array): time array for simulation.

    Kwargs:
       plotting (bool): Plotting for user interpretation. defaut is False.

    Returns:
       (M and S arrays): Arrays of t for the throughput of manufacturers and suppliers.

    """
    
    import numpy as np
    from scipy.integrate import odeint
    import odeintw as OIW
    
    #setting simulation time series parameters
    M, K_M, alpha_M, B_M1, B_M2, mu_M, S, K_S, alpha_S, B_S1, B_S2, mu_S, h, A_MS = parameters
    m, s = len(M), len(S)
    A_MS = np.array(A_MS)
    alpha_M_scale, alpha_S_scale = alpha_M, alpha_S
    delta = 0.1 #interaction strength modulation
    
    def competition_function(i, M, B_M1_i, B_M2_i):
        C_sum = 0
        for j in range(len(B_M1_i)):
            if j != i:
                C_sum = C_sum + (B_M1_i[j] + B_M2_i[j])*M[j]
        return M[i]*C_sum
    
    def mutualistic_manufacturer_interaction_function(i, M, S, h, A_MS, delta):
        gamma_0 = 1 #mutualistic strength level
        MI_sum = 0
        for k in range(len(A_MS[i])): #go through each supplier of of manufacturer
            y_ik = A_MS[i][k]
            N_i = np.sum(A_MS[i]) #number of interactions
            gamma_ik = y_ik*gamma_0/(N_i**delta)
            MI_sum = MI_sum + gamma_ik*S[k]
        return M[i]*MI_sum/(1+h*MI_sum)
    def mutualistic_supplier_interaction_function(i, M, S, h, A_MS, delta):
        AT_MS = A_MS.T
        gamma_0 = 1 #mutualistic strength level
        MI_sum = 0
        for k in range(len(AT_MS[i])): #go through each supplier of of manufacturer
            y_ik = AT_MS[i][k]
            N_i = np.sum(AT_MS[i]) #number of interactions
            gamma_ik = y_ik*gamma_0/(N_i**delta)
            MI_sum = MI_sum + gamma_ik*M[k]
        return S[i]*MI_sum/(1+h*MI_sum)
    
    #defining simulation functions
    def dot_MS(M, K_M, alpha_M, B_M1, B_M2, mu_M,
               S, K_S, alpha_S, B_S1, B_S2, mu_S,
               h, A_MS, delta):
        
        #M is array of manufacturers
        #S is array of suppliers
        dM = [] #state space time derivatives for M and S
        for i in range(len(M)):
            M_i, K_M_i, alpha_M_i = M[i], K_M[i], alpha_M[i]
            B_M1_i, B_M2_i = B_M1[i], B_M2[i]
            mu_M_i = mu_M[i]
            growth = M_i*(1-M_i/K_M_i)
            internal_perturbation = alpha_M_i*M_i
            competition = competition_function(i, M, B_M1_i, B_M2_i)
            mutualistic_interaction = mutualistic_manufacturer_interaction_function(i, M, S, h, A_MS, delta)
            dM_i = growth - internal_perturbation - competition + mutualistic_interaction + mu_M_i
            dM.append(dM_i)
        
        dS = [] #state space time derivatives for M and S
        for i in range(len(S)):
            S_i, K_S_i, alpha_S_i = S[i], K_S[i], alpha_S[i]
            B_S1_i, B_S2_i = B_S1[i], B_S2[i]
            mu_S_i = mu_S[i]
            growth = S_i*(1-S_i/K_S_i)
            internal_perturbation = alpha_S_i*S_i
            competition = competition_function(i, S, B_S1_i, B_S2_i)
            mutualistic_interaction = mutualistic_supplier_interaction_function(i, M, S, h, A_MS, delta)
            dS_i = growth - internal_perturbation - competition + mutualistic_interaction + mu_S_i
            dS.append(dS_i)
            
        return np.array(dM), np.array(dS)
    
    
    dt = np.mean(np.diff(t))
    T = len(t)
    M_arr = [M]
    S_arr = [S]
    perturbation_CD = 0
    alpha_M = np.random.rayleigh(0,m) #internal perturbation of manufacturer
    alpha_S = np.random.rayleigh(0,s) #internal perturbation of supplier
    for i in range(T):
        perturbation_CD = perturbation_CD+dt
        if perturbation_CD > 1:
            alpha_M = np.random.rayleigh(alpha_M_scale,m) #internal perturbation of manufacturer
            alpha_S = np.random.rayleigh(alpha_S_scale,s) #internal perturbation of supplier
            perturbation_CD = 0
        
        dM, dS = dot_MS(M, K_M, alpha_M, B_M1, B_M2, mu_M,S, K_S, alpha_S, B_S1, B_S2, mu_S, h, A_MS, delta)
        M, S = M+dM*dt, S+dS*dt
        M_arr.append(M)
        S_arr.append(S)
    
    return np.array(M_arr)[:-1], np.array(S_arr)[:-1]

def MS_network(A_MS, M_arr, S_arr):
    """This function takes system parameters to develop a time dependent adjacency matrix A(t).

    Args:
       A_MS (array):  Unweighted adjacency matrix for network.
       M_arr (array): Throughput array for manufacturers.
       S_arr (array): Throughput array for suppliers.

    Kwargs:
       plotting (bool): Plotting for user interpretation. defaut is False.

    Returns:
       (matrix): A, an n by n matrix A over time t.

    """
    import numpy as np
    import networkx as nx
    import matplotlib.gridspec as gridspec
    import matplotlib.pyplot as plt
    E = []
    num_man = len(A_MS)
    num_sup = len(A_MS[0])
    for m in range(num_man):
        for s in range(num_sup):
            if A_MS[m][s] != 0:
                E.append([m,s+num_man])
        
    V_M = np.arange(num_man).astype(int) 
    V_S = np.arange(num_man, num_man+num_sup).astype(int) 
    n = num_man+num_sup
    G = nx.Graph()
    G.add_nodes_from(V_M, bipartite=0)
    G.add_nodes_from(V_S, bipartite=1)
    G.add_edges_from(E)
    
    As = []
    for t in np.arange(0,len(M_arr.T[0])):
        A = np.zeros((n,n))
        for e in E:
            w1 = M_arr.T[e[0]][t]
            w2 = S_arr.T[e[1]-num_man][t]
            e_ij = np.min([w1, w2])
            A[e[0], e[1]] = e_ij
        A = A+A.T
        As.append(A)
    return np.array(As)
    
    
    make_gif = False
    if make_gif == True:
        top = nx.bipartite.sets(G)[0]
        pos = nx.bipartite_layout(G, top)
        colors = ['lightgreen'] * num_man + ['lightblue'] * num_sup
        labeldict = {}
        for i in range(num_man): 
            labeldict[i] = r'$M_{'+str(i)+'}$'
        for i in range(num_sup): 
            j = i+num_man
            labeldict[j] = r'$S_{'+str(i)+'}$'
            
        frame_count = 0
        for j in np.arange(0,len(M_arr.T[0]),int(len(M_arr.T[0])/100)):
            node_sizes = []
            M_max = np.amax(M_arr)
            S_max = np.amax(S_arr)
            for i in range(num_man): 
                node_sizes.append(2000*M_arr.T[i][j]/M_max)
            for i in range(num_sup): 
                node_sizes.append(2000*S_arr.T[i][j]/S_max)
                
            weights = []
            for e in E:
                w1 = M_arr.T[e[0]][j]/M_max
                w2 = S_arr.T[e[1]-num_man][j]/S_max
                w = np.min([w1, w2])
                weights.append(4*w) 
                
            fig = plt.figure(figsize = (4,3))
            print(pos)
            nx.draw(G, pos=pos, with_labels=False, labels = labeldict, 
                    node_color=colors, node_size = node_sizes, width = weights)
            axis = plt.gca()
            axis.set_xlim([1.25*x for x in axis.get_xlim()])
            axis.set_ylim([1.25*y for y in axis.get_ylim()])
            plt.text(x = -0.32, y = -0.15, s=' Dynamical \n Networks',
                     ma = 'center',
                     wrap = True, fontsize = 30, 
                     bbox=dict(boxstyle="round",ec=(0.0, 0.0, 0.0),fc=(0.85, 0.85, 0.85),))
            plt.savefig('C:\\Users\\myersau3.EGR\\Desktop\\python_png\\frames\\frame'+str(frame_count)+'.png', 
                     pad_inches = 0.30, dpi = 200)
            plt.show()
            frame_count = frame_count + 1
        
        import imageio
        images = []
        for i in range(int(frame_count)):
            print(i)
            images.append(imageio.imread('C:\\Users\\myersau3.EGR\\Desktop\\python_png\\frames\\frame'+str(i)+'.png'))
        for i in range(int(frame_count)):
            i = int(frame_count) - i - 1
            print(i)
            images.append(imageio.imread('C:\\Users\\myersau3.EGR\\Desktop\\python_png\\frames\\frame'+str(i)+'.png'))
        imageio.mimsave('C:\\Users\\myersau3.EGR\\Desktop\\python_png\\MS_network_gif.gif', images, fps = 50)


# In[ ]:


if __name__ == '__main__':
    
    from dynamical_networks.simulate.MS_network import MS_simulation, MS_network
    import numpy as np
    import matplotlib.pyplot as plt
    
    
    #----------------------System Parameters and intial conditions------------------------
    M = np.zeros((3,))+0.7                     #current throughput of manufacturer
    S = np.zeros((2,))+0.8                      #current throughput of supplier
    m = len(M)
    s = len(S)
    a = np.ones(s*m)
    a[:int((m*s)*0.65)] = 0
    np.random.shuffle(a)
    A_MS = a.reshape((m,s))        #adjacency matrix for M/S connections
    for i in range(len(A_MS)):
        if np.sum(A_MS[i]) == 0:
            j = int(np.random.uniform(0,len(A_MS[i]),1))
            A_MS[i][j] = 1
    for i in range(len(A_MS.T)):
        if np.sum(A_MS.T[i]) == 0:
            j = int(np.random.uniform(0,len(A_MS.T[i]),1))
            A_MS[j][i] = 1
            
    K_M = np.zeros((m,))+2      #maximum throughput of manufacturer
    K_S = np.zeros((s,))+1       #maximum throughput of supplier
    alpha_M = 0.01                     #internal perturbation of manufacturer
    alpha_S = 0.01                      #internal perturbation of supplier
    B_M1 = np.zeros((m,m))+0.6         #effects of price competition on manufacturer
    B_S1 = np.zeros((s,s))+0.6        #effects of price competition on supplier
    B_M2 = np.zeros((m,m))+0.0          #effects of technology competition on manufacturer
    B_S2 = np.zeros((s,s))+0.0          #effects of technology competition on supplier
    mu_M = np.zeros((m,))               #Manufacturer production outsourcing intensity
    mu_S = np.zeros((s,))               #Supplier production outsourcing intensity
    h = 2
    
    
    
    # package parameters and define time array
    parameters = [M, K_M, alpha_M, B_M1, B_M2, mu_M,S, K_S, alpha_S, B_S1, B_S2, mu_S, h, A_MS]
    fs, L = 300, 15
    t = np.linspace(0, L,int(L*fs))
    
    
    
    #run simulation
    M_arr, S_arr = MS_simulation(t, parameters)
    A = MS_network(A_MS, M_arr, S_arr)
    
    
    
    #plot resulting simulation throughput
    for i in range(len(M_arr[0])):
        plt.plot(t, M_arr.T[i], label = r'$M_{'+str(i)+'}$')
    plt.legend()
    plt.ylim(0,)
    plt.grid()
    plt.show()
    
    for i in range(len(S_arr[0])):
        plt.plot(t, S_arr.T[i], label = r'$S_{'+str(i)+'}$')
    plt.legend()
    plt.ylim(0,)
    plt.grid()
    plt.show()
    
    
    
    


