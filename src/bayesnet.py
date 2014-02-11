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
             
        # normalize to get cpt rather than counts
        sums = np.sum(cpt, axis=0)
        if sums.shape:
            flatsums = sums.reshape(sums.shape[0], -1).flatten()         
            flatcounts = cpt.reshape(cpt.shape[0], -1)
            cpt = (flatcounts/flatsums).reshape(cpt.shape)
        else:
            cpt = cpt/sums
        cpts[key] = cpt
    print
    return cpts

def test(unknown, cpts, data, graph, domains, data_idx):
    unk_domain_size = domains[unknown]
    unk_dat_idx = data_idx[unknown]
    probs = np.zeros((len(data),unk_domain_size))
    true_classes = np.empty(len(data))
    for i,d in enumerate(data-1): # shift everything down by 1 to be zero-indexed
        # grab true classification
        true_classes[i] = d[unk_dat_idx]
        # predict probability dist over classes given training data
        total = 0.0
        for unknown_val in range(unk_domain_size):
            prod = 1.0
            for key, value in graph.iteritems():
                # get necessary indices into data
                settings = d[[data_idx[key]] + map(lambda x: data_idx[x], value)]
                # get index that should be replaced with unknown setting
                # and replace with unknown variable setting if necessary
                try :
                    unk_idx = 0 if key == unknown else value.index(unknown)+1
                    settings[unk_idx] = unknown_val
                except ValueError:
                    pass
                #print "key:", key, "settings:", settings
                prod *= cpts[key][tuple(settings)]
            probs[i,unknown_val] += prod
            total += prod
        probs[i] /= total
    return np.sum((np.argmax(probs,axis=1) == true_classes).astype(float))/len(data)

def print_cpt(variable, cpts, graph, variable_map):
    cpt = cpts[variable]
    parents = graph[variable]
    print "P(%s%s)" % (variable, "|"+",".join(parents) if parents else "")
    print cpt
    print
    