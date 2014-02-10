'''
CS688 HW01: Problem 5

Perform some queries on the network.

@author: Emma Strubell
'''

import given_model as model
import bayesnet as bn
import numpy as np

data_fname = "../data/train/data-train-1.txt"

# populate CPTs from the hw model
cpts = bn.compute_cpts_from_dat(model.graph, model.domains, model.data_idx, data_fname)

def prod(x, y):
    return x * y

'''
P(CH=ch|...) = 
P(CH=ch|A=2,G=M)P(HD=No|CH=ch,BP=L)/sum_{ch}(P(CH=ch|A=2,G=M)P(HD=No|CH=ch,BP=L))
'''
def part_a():
    domain_size = model.domains["CH"]
    probs = np.zeros(domain_size)
    total = 0.0
    
    # observed values
    a_value = 1
    g_value = 1
    hd_value = 0
    bp_value = 0
    
    for ch_value in range(domain_size):
        probs[ch_value] = \
        cpts["CH"][ch_value,a_value,g_value]* \
        cpts["HD"][hd_value,bp_value,ch_value]
        total += probs[ch_value]
    print probs/total
    print

'''
P(BP=bp|...) = ...
'''
def part_b():
    bp_domain_size = model.domains["BP"]
    g_domain_size = model.domains["G"]
    probs = np.zeros(bp_domain_size)
    
    # observed values
    a_value = 1
    ch_value = 1
    hr_value = 1
    hd_value = 0
    
    total = 0.0
    for bp_value in range(bp_domain_size):
        probs[bp_value] += \
        reduce(prod, [cpts["BP"][bp_value,g_value] for g_value in range(g_domain_size)])* \
        reduce(prod, [cpts["G"][g_value] for g_value in range(g_domain_size)])* \
        reduce(prod, [cpts["CH"][ch_value,a_value,g_value] for g_value in range(g_domain_size)])* \
        cpts["HD"][hd_value,bp_value,ch_value]* \
        cpts["HR"][hr_value,hd_value,bp_value,a_value]
        total += probs[bp_value]
    print probs/total
       
part_a()
part_b()
    
