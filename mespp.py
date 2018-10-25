import math
import numpy as np
S = [2,0]

T = [0,2]

h = [[2,1,0],[3,20,1],[4,20,1]]
#h_matrix = np.matrix(h)



X =2
Y =2
neighbors = lambda x, y : [(x2, y2) for x2 in range(x-1, x+2)
                                   for y2 in range(y-1, y+2)
                                   if (-1 < x <= X and
                                       -1 < y <= Y and
                                       (x != x2 or y != y2) and
                                       (0 <= x2 <= X) and
                                       (0 <= y2 <= Y))]
def manhattan_distance (start,neigh):
    distance = abs(start[0]-neigh[0])+ abs(start[1]-neigh[1])
    return distance

def choose_neighbor(start):
    temp = []
    temp1= [0,0]
    temp2= [0,0]
    temp3= [0,0]

    #print "Its here too"
    chosen =  neighbors (start[0],start[1])
    #print "Its here too theice"
    temp1[0] = chosen[0][0]
    temp1[1] = chosen[0][1]
    temp2[0] = chosen[1][0]
    temp2[1] = chosen[1][1]
    temp3[0] = chosen[2][0]
    temp3[1] = chosen[2][1]
    #print "Its here too twice"

    #calculations for temp1
    f1 = manhattan_distance(start,temp1)
    #calculations for temp2
    f2 = manhattan_distance(start,temp2) + h[temp2[0]][temp2[1]]
    #calculations for temp3
    f3 = manhattan_distance(start,temp3) + h[temp3[0]][temp3[1]]

    f = min(f1,f2,f3)
    if f1 == f:
        print "Chosen node 1"
        temp = temp1
    if f2 == f:
        print "Chosen node 2"
        temp = temp2
    if f3 == f:
        print "Chosen node 3"
        temp = temp3
    return temp

def update_heuristic(path):
    for j in range(len(path)):
        a =[0,0]
        a[0] = path[j][0]
        a[1] = path[j][1]

        h[a[0]][a[1]] = h[S[0]][S[1]] - manhattan_distance (S,a)
        print manhattan_distance(S,a)
        print h

def a_star(start, goal):
    frontier = []
    path = []
    #print "Yes its here"
    #neighbors (start[0],start[1])
    while start != goal:
        chosen = choose_neighbor(start)
        start = chosen
        path.append(chosen)


    update_heuristic(path)

    return path









print a_star(S,T)

#if __name__ ="__main__":
