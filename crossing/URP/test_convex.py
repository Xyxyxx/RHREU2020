# code to test convex hull probabilities

import math as ma
import numpy as np
import random as rand


def main():
    n = 10_000

    convex_case = 0

    
    for i in range(n):
        if (test_convex()):
            convex_case += 1

    print("#Convex / #Total number of trials =", convex_case / n)
    

def test_convex():
    S = []

    for i in range(5):
        S.append( generate_coords() )

    P = jarvis(S)
    
    # check if len(P) == n to check if convex hull is n points
    if (len(P) == 4):
        return True
    
    return False


def generate_coords():
    return (rand.uniform(0,1), rand.uniform(0, 1), rand.uniform(0, 1))


def jarvis(S):
    # S is set of points to check
    # P will be set of points which form convex hull 
    # final set size is i

    P = []

    point_on_hull = S[0]


    
    # check if point_on_hull is left most point in S
    for x in S:
        if (x[0] < point_on_hull[0]):
            point_on_hull = x

    i = 0
    while True:
        P.append(point_on_hull)

        end_point = S[0] # initial endpoint candidate for edge of hull

        for v in S:
            if (end_point == point_on_hull) and (v == S[1]):
                end_point = v
            elif ( check_left(v, P[i], end_point) ):
                end_point = v
        
        i = i + 1
        point_on_hull = end_point
        
        if (end_point == P[0]):
            # we wrapped around to the first hull
            return P
    
    return P

def check_left(x, p, end_point):
    
    u = tuple( np.subtract( end_point, p) )
    v = tuple( np.subtract( x, p ) )
    # next find det of [u, v]
    d = det(u, v)
    
    if (d < 0):
        return True
    
    return False


def det(u, v):
    a = u[0]
    b = v[0]
    c = u[1]
    d = v[1]

    return a * d - b * c

if __name__ == "__main__":
    main()