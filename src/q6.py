'''
CS688 HW01: Question 6

Test the Bayes net as a classifier for the variable HD.

@author: Emma Strubell
'''

import given_model as model
import bayesnet as bn
import numpy as np
from string import Template

num_data_files = 5
train_data_fname_template = Template("../data/train/data-train-${num}.txt")
test_data_fname_template = Template("../data/test/data-test-${num}.txt")
train_data_files = [train_data_fname_template.substitute(num=n) for n in range(1,num_data_files+1)]
test_data_files = [test_data_fname_template.substitute(num=n) for n in range(1,num_data_files+1)]

# populate CPTs from the hw model
trained_cpts = [bn.compute_cpts_from_dat(model.graph, model.domains, model.data_idx, fname) \
                for fname in train_data_files]

# read in test data
test_data = [np.loadtxt(fname, dtype='int', delimiter=",") for fname in test_data_files]

# the variable we want to predict
test_var = "HD"

# accuracies for each train/test pair
results = [bn.test(test_var, trained_cpts[i], test_data[i], model.graph, model.domains, model.data_idx) \
           for i in range(num_data_files)]

print "mean:", np.mean(results)
print "sd:", np.std(results)
