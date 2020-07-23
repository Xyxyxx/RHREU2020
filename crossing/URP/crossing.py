# first attempt at simulating URP crossings

import time
import random
import math
import numpy
  
def main():
    #n=input()
    #n = int(n)
    
    n = 50000
    run_number = 0

    crossings = 0

    for i in range(n):
      p_one = generate_coords()
      p_two = generate_coords()

      q_one = generate_coords()
      q_two = generate_coords()

      result = find_intersection(p_one, p_two, q_one, q_two)

      run_number += 1

      if (is_intersecting(result)):
        over_cross = find_overstrand(result[0], result[1], p_one, p_two, q_one, q_two)
        if (over_cross == 1):
          # calculate crossing with p line as over
          over = tuple(numpy.subtract(p_one, p_two))
          under = tuple(numpy.subtract(q_one, q_two))
        elif (over_cross == 2):
          # calculate crossing with q line as over
          over = tuple(numpy.subtract(q_one, q_two))
          under = tuple(numpy.subtract(p_one, p_two))
        else:
          # this should never happen
          over = (0,0)
          under = (0,0)
          print("Error, bad crossing")
        # then need to find crossing
        crossing = find_crossing(over, under)

        crossings += 1

    print( (crossings / n) * 0.5 )
    print("End")
  
def generate_coords():
    return (random.uniform(0,1), random.uniform(0,1), random.uniform(0,1))


def find_intersection(p_one, p_two, q_one, q_two):
    # matrix of form 
    # [p1 - p2, q2 - q1](s,t) = q2 - p2
    # [[p1[0] - p2[0], p1[1] - p2[1]], [q2[0] - q1[0], q2[1] - q1[1]]] (t,s) = [q2[0] - p2[0], q2[1] - p2[1]]
    matrix = [ [p_one[0] - p_two[0], q_two[0] - q_one[0]] ]
    matrix.append([p_one[1] - p_two[1], q_two[1] - q_one[1]])

    inverted = invert_matrix(matrix)

    vec = ( q_two[0] - p_two[0] , q_two[1] - p_two[1] )

    result = apply_matrix(inverted, vec)

    return result

def is_intersecting(result):
    if ((0 <= result[0] <= 1) and (0 <= result[1] <= 1)):
      return True

    return False

def find_overstrand(s, t, p_one, p_two, q_one, q_two):
    # given s and t
    p_z = p_one[2] * s + (1 - s) * p_two[2]

    q_z = q_one[2] * t + (1 - s) * q_two[2]

    if (p_z > q_z):
      return 1

    return 2

def find_crossing(u, v):
    u = list(u)
    v = list(v)

    matrix = [u, v]

    a = matrix[0][0]
    b = matrix[1][0]
    c = matrix[0][1]
    d = matrix[1][1]

    det = a * d - b * c

    if (det > 0):
      return 1

    return -1


def invert_matrix(m):  # m is a 2x2 matrix
    # m = [ [a, c], [b, d] ]
    a = m[0][0]
    b = m[0][1]
    c = m[1][0]
    d = m[1][1]

    det = a * d - b * c

    factor = 1 / det

    inverted = [ [ factor * d , -factor * c ] , [ -factor * b , factor * a] ]
    return inverted

def apply_matrix(m, vec):
    # m = [[a, c],[b, d]]
    # each entry of m is a column vec
    a = m[0][0]
    b = m[1][0]
    c = m[0][1]
    d = m[1][1]

    x = a * vec[0] + b * vec[1]

    y = c * vec[0] + d * vec[1]

    return (x, y)

if __name__ == "__main__":
    main()