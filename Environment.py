# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 18:10:46 2021

@author: Adrián Menor de Oñate
"""
import numpy as np

# Envirnoment
class environment:
    def __init__(self,state,action,A,B,C,dt):
        self.state       = state
        self.action      = action
        self.A           = A
        self.B           = B
        self.C           = C
        self.dt          = dt
        
    def state_size(self):
        return self.A.shape[0]
    
    def input_size(self):
        return self.B.shape[1]
     
    def next_state(self):
        x_dot = np.matmul(self.A,self.state) + self.B*self.action
        state = self.state + x_dot*self.dt
        return state
    
    def reward(self):
        1
        

    
    
    
    