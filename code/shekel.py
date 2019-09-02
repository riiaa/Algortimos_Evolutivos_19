# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 11:29:30 2016

@author: stan
"""
from environment import Environment
import numpy as np
from decoding_tools import DecodingTools as dt
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

class Shekel(Environment):
    
    A = np.matrix([
    [0.5,0.5],
    [0.25,0.25],
    [0.25,0.75],
    [0.75,0.25],
    [0.75,0.75]])
    
    c = np.matrix([
    [0.002],
    [0.005],
    [0.005],
    [0.005],
    [0.005],
    ])
    
    
    def __init__(self,precision=10):
        self.precision = precision
        self.fig = plt.figure()
        self.ax = Axes3D(self.fig)
    
    def evaluate(self,population):
        for individual in population.individuals:
            individual.fitness = Shekel.function(individual.phenotype)
                
    
    def decode(self,population):
        for individual in population.individuals:
            ch = individual.genotype.chromosome
            individual.phenotype = \
            np.matrix([\
            dt.decode_normalized_real(ch,0,self.precision),\
            dt.decode_normalized_real(ch,self.precision,self.precision)])
    
    @staticmethod
    def function(x):
        d = (np.kron(x,np.ones((5,1)))-Shekel.A)
        return np.sum(1/(np.sum(np.multiply(d,d),axis=1) + Shekel.c))

    
    def get_chromosome_length(self):
        return self.precision*2
        
    def compute_distance(self,individual1,individual2):
        return np.linalg.norm(individual1.phenotype-individual2.phenotype)
        
    def compute_normalized_distance(self,individual1,individual2):
        return np.linalg.norm(individual1.phenotype-individual2.phenotype)
        
    def show(self,population=None,clear=False):
        f = np.vectorize(lambda x,y: Shekel.function(np.array([x,y])))  
        
        if(population != None):
            fen =[x.phenotype for x in population.individuals]
            X = [x.item(0) for x in fen]
            Y = [x.item(1) for x in fen]
        else:
            x = np.linspace(0,1,100)
            y = np.linspace(0,1,100)
            X,Y = np.meshgrid(x,y)
            
        Z = f(X,Y)
        
        
        if(population != None):
            self.ax.scatter(X,Y,Z,cmap=cm.jet)
        else:
            self.ax.plot_surface(X,Y,Z,rstride=5,cstride=5,cmap=cm.jet)
            
        plt.show()
        
        
        
        
        
        
        