import numpy as np

from os import listdir
from os.path import isfile, join

from scipy.io import loadmat




meta_clsloc_file = "meta_clsloc.mat"

synsets = loadmat(meta_clsloc_file)["synsets"][0][:1000]
synsets = sorted([(int(s[0]), str(s[1][0])) for s in synsets], key=lambda v:v[1])

corr = {}
for i in range(1,1001):
    corr[i] = next(j for j in range(1000) if synsets[j][0] == i)

    

def synset_to_id(synset):
    a = next(i for (i,s) in synsets if s == synset)
    return a


def id_to_synset(id):
    return synsets[corr[id]][1]
    
