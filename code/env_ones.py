# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 09:46:33 2016

@author: stan
"""
from environment import Environment
class Ones(Environment):
    
    def __init__(self,n):
        self.n = n
    def evaluate(self,population):
        for individual in population.individuals:
            bits = individual.genotype.chromosome
            individual.fitness = self.contar_unos(bits)
        
    def get_gene_template(self):
        return [([self.n,0])]
        
    def decode(self,population):
        for individual in population.individuals:
            individual.phenotype = individual.genotype.chromosome
        
    def get_chromosome_length(self):
        return self.n
    
    def contar_unos(self, bits):
        return bin(bits).count("1")
    
    