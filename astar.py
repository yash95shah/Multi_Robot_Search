S= [2,0]
T =[1,2]
X =2
Y =2
import numpy
neighbors = lambda x, y : [(x2, y2) for x2 in range(x-1, x+2)
                                   for y2 in range(y-1, y+2)
                                   if (-1 < x <= X and
                                       -1 < y <= Y and
                                       (x != x2 or y != y2) and
                                       (0 <= x2 <= X) and
                                       (0 <= y2 <= Y))]
A= [(2,3),(1,2)]
print neighbors(S[0], S[1])

T[0] = neighbors(S[0], S[1])[1][0]
T[1] = neighbors(S[0], S[1])[1][1]
print  T
