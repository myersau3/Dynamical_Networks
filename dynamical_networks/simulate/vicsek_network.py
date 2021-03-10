# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 11:03:26 2021

@author: myersau3
"""

def check_boundaries(x_new_i, y_new_i, B):
    x_width, y_width = B[0][1] - B[0][0], B[1][1] - B[1][0]
    if x_new_i > B[0][1]:
        x_new_i = x_new_i-x_width
    if x_new_i < B[0][0]:
        x_new_i = x_new_i+x_width
    if y_new_i > B[1][1]:
        y_new_i = y_new_i-y_width
    if y_new_i < B[1][0]:
        y_new_i = y_new_i+y_width
    return x_new_i, y_new_i
        
def vicsek_model(t, initial_conditions, velocity, noise_std, eps, B):
    dt = np.mean(np.diff(t))
    x, y = initial_conditions.T[0], initial_conditions.T[1]
    theta = initial_conditions.T[2]
    I = np.arange(len(x))
    dx, dy = v*dt*np.cos(theta), v*dt*np.sin(theta)
    pos = []
    for t_i in t:
        pos.append(np.array([x, y, theta]).T)
        x_new = []
        y_new = []
        theta_new = []
        for i in range(len(initial_conditions)):
            x_i, y_i, theta_i = x[i], y[i], theta[i]
            d_i = np.sqrt((x-x_i)**2 + (y-y_i)**2)
            neighbors = I[d_i<eps]
            theta_ave = np.mean(theta[neighbors])
            theta_new_i = theta_ave + np.random.normal(0,noise_std,1)[0]
            dx, dy = v*dt*np.cos(theta_i), v*dt*np.sin(theta_i)
            x_new_i, y_new_i = x_i+dx, y_i+dy
            x_new_i, y_new_i = check_boundaries(x_new_i, y_new_i, B)
            
            x_new.append(x_new_i)
            y_new.append(y_new_i)
            theta_new.append(theta_new_i)
        x, y, theta = np.array(x_new), np.array(y_new), np.array(theta_new)
    pos = np.array(pos)
    
    plotting = True
    if plotting == True:
        for i in np.arange(0,len(pos), 2):
            x, y = pos[i].T[0], pos[i].T[1]
            plt.figure(figsize = (7,7))
            plt.plot(x,y, 'k.')
            lim = 1
            plt.xlim(-0,lim)
            plt.ylim(-0,lim)
            plt.show()
            
        
    return pos
    
    
# In[ ]: 

if __name__ == "__main__": 
        
    import numpy as np
    import matplotlib.pyplot as plt
    
    n = 100
    v = 10
    dt = 0.01
    x = np.random.rand(n,1).T[0]
    y = np.random.rand(n,1).T[0]
    theta = 2*np.pi*np.random.rand(n,1).T[0]
    
    
    nu = 0.1
    IC = np.array([x, y, theta]).T
    t = np.linspace(0,3,2000)
    B = [[-0,1],[-0,1]]
    
    vicsek_model(t = t, initial_conditions = IC, velocity = v, 
                 noise_std = nu, eps = 0.05, B = B)
    
    
    
    
    
    
    
    
    
    
    
    
    