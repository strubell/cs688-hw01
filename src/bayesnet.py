'''
CS688 HW01: Bayes Net

Some functions for performing parameter estimation using a Bayesian network.

@author: Emma Strubell
'''

import numpy as np

def compute_cpts_from_dat(graph, domains, data_idx, data_fname):
    # load data
    raw_data = np.loadtxt(data_fname, dtype='int', delimiter=",")
    cpts = {}
    for key, value in graph.iteritems():
        combinations = reduce(lambda x, y: x*y, map(lambda x: domains[x], value), 1)*domains[key]
        print "Processing variable: %s, table size: %d" % (key, combinations)
        
        # initialize empty cpt with a dimension for each variable
        dimensions = [domains[key]] + map(lambda x: domains[x], value)
        cpt = np.zeros(dimensions)
        
        # get necessary indices into data
        indices = [data_idx[key]] + map(lambda x: data_idx[x], value)
        
        # read in counts from data (need to subtract 1 to get 0 indexing)
        for i in raw_data[:, indices]-1:
            cpt[tuple(i)] += 1.0
        
        print "counts:", cpt
        rolled_cpt = np.rollaxis(cpt, axis=-1)
        print "counts rolled:", rolled_cpt
              
        # normalize to get cpt rather than counts
        #sums = np.sum(cpt, axis=0)
        sums = np.sum(cpt, axis=0)
        print "sums:", sums
        if sums.shape:
            sums = np.transpose(sums)
            print "sums tranpose:", sums
            for i in range(cpt.shape[-1]):
                print "rows:", cpt[...,i], "sums:", sums[i]
                print "transpose:", np.transpose(cpt[...,i])
                print "sums:", np.transpose(sums[i,np.newaxis])
                cpt[...,i] = np.transpose(np.transpose(cpt[...,i]) / np.transpose(sums[i,np.newaxis]))
                print cpt[...,i]
                #for j in range(len(cpt[...,i])):
                    #print "row:", cpt[...,i][j], "sum:", sums[i]
                    #cpt[...,i][j] /= sums[i]
        else:
            cpt = cpt/sums
        cpts[key] = cpt
#         if sums.shape:
#             for i in range(cpt.shape[-1]):
#                 for j in range(len(cpt[...,i])):
#                     cpt[...,i][j] /= sums[j]
#         else:
#             cpt = cpt/sums
#         cpts[key] = cpt
    print
    return cpts

def print_cpt(variable, cpts, graph, variable_map):
    cpt = cpts[variable]
    parents = graph[variable]
    print "P(%s%s)" % (variable, "|"+",".join(parents) if parents else "")
    print cpt
    print
    