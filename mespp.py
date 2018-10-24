''' Sequential Allocation MESPP algorithm

Input: Multi-agent efficient search problem
 % V C N' is the set of nodes visited by the searchers
 V= [] initially
 for all searchers k do
 % Ak C N' is a feasible path for searcher k
 % Finding the arg max solves the ESPP for searcher k
 Ak = arg max over Ak the value of F (V U Ak)
 V = V U Ak
 end for
 Return Ak for all searchers k '''
import numpy as np
import random as rd
capture_state = False
V = []   # This is the set of nodes visited by the searchers
N = [[0.5, 0.5, 0.0], [0.3,0.3,0.3], [0.0, 0.5, 0.5]]
N_mat = np.matrix(N)
print (N_mat)
'''def __init__ (self, searcher):
     self.searcher = searcher
def captured (searcher):
    for k in range(0,2): '''
