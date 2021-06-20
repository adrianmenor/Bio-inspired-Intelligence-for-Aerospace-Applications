# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 17:10:45 2021

@author: Adrián Menor de Oñate
"""
from Environment  import environment
from keras.models import Sequential
from keras.layers import Dense

# Controller
class controller():
        def __init__(self):
            self.actor  = self.actor_network()
            self.critic = self.critic_network()
            
        def actor_network(self):
            actor = Sequential([
                Dense(64, activation='tanh', input_shape=(environment.state_size(),0)),
                Dense(64, activation='tanh'),
                Dense(environment.input_size(), activation='relu'),])
            return actor

        def critic_network(self):
            critic = Sequential([
                Dense(64, activation='tanh', input_shape=(environment.state_size(),0)),
                Dense(64, activation='tanh'),
                Dense(1, activation='relu'),])
            return critic




