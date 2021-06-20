# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 16:59:49 2021

@author: Adrián Menor de Oñate
"""
import numpy as np
import matplotlib.pyplot as plt
from Environment import environment

# time step
dt = 0.01 #[s]

# State-Space matrices
A = np.array([[0, 1],[14.7805 ,0]])
B = np.array([[0],[3.4858]])
C = np.array([[1 ,1]])

# Simulating the system
x = np.array([[0],[0]])
i = 0
t = 0 #[s]
a = np.array([1])
x1_history = []
x2_history = []
t_history = []
while i<200:
    rocket = environment(x, a, A, B, C,dt)
    x = rocket.next_state()
    i+=1
    t+=dt
    x1_history.append(x[0,0])
    x2_history.append(x[1,0])
    t_history.append(t)

# Plotting
plt.plot(t_history, x1_history)
plt.plot(t_history, x2_history)
plt.xlabel("Time [s]")
plt.ylabel("State magnitude")
plt.legend(['Pitch angle [rad]','Pitch rate [rad/s]'])
plt.grid()
plt.show()
