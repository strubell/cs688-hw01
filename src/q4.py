'''
CS688 HW01: Problem 4



@author: Emma Strubell
'''

import given_model as model
import bayesnet as bn

data_fname = "../data/train/data-train-1.txt"

# populate CPTs from the hw model
cpts = bn.compute_cpts_from_dat(model.graph, model.domains, model.data_idx, data_fname)

bn.print_cpt("A", cpts, model.graph, model.variable_map)
bn.print_cpt("BP", cpts, model.graph, model.variable_map)
bn.print_cpt("HD", cpts, model.graph, model.variable_map)
bn.print_cpt("HR", cpts, model.graph, model.variable_map)

    
