import math as ma
import numpy as np
import random as rand


def main():
    n = 10_000

    convex_case = 0

    
    for i in range(n):
        #print(check_convex())
        if (test_convex()):
            convex_case += 1
            #print(convex_case)
            #print(convex_case / n)

    print("#Convex / #Total number of trials =", convex_case / n)
    

    #print(test_convex())

def test_convex():
    S = []

    for i in range(5):
        S.append( generate_coords() )

    #print(len(S))
    #print(S)

    #print(S)
    P = jarvis(S)
    
    '''
    if (P != 5):
        print(False)
    else:
        print(True)
    '''

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

    #print("S =", S)

    point_on_hull = S[0]

    #print(point_on_hull)

    
    # check if point_on_hull is left most point in S
    for x in S:
        #print(x)
        #print(x[0])

        #print("point_on_hull = ", point_on_hull)

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
                #print("here")
                end_point = v
                #print(P)
        
        i = i + 1
        point_on_hull = end_point
        #print(P)
        
        if (end_point == P[0]):
            # we wrapped around to the first hull
            return P
        #if (i == 5):
            #print("This is looping infinitely!")
        #    return P
    
    return P

def check_left(x, p, end_point):
    
    u = tuple( np.subtract( end_point, p) )
    v = tuple( np.subtract( x, p ) )
    # next find det of [u, v]
    d = det(u, v)
    
    if (d < 0):
        return True
    
    return False
    
    '''
    # check if height of x in between height of p and end_point
    y_max = max(p[1], end_point[1])
    y_min = min(p[1], end_point[1])

    # now need to find x-coord of when height of line of p to end_point match up
    t = (x[1] - p[1]) / (end_point[1] - p[1])

    line_x = end_point[0] * t + (1 - t) * p[0]

    if (x[1] < line_x):
        return True

    return False
    '''


def det(u, v):
    a = u[0]
    b = v[0]
    c = u[1]
    d = v[1]

    return a * d - b * c

if __name__ == "__main__":
    main()