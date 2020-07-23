import time
import random
import math
import numpy


def main():
    n = 1_000_000
    print("p value after " + str(n) + " trials:")
    print( ptest(n) )
    print("u value after " + str(n) + " trials:")
    print( utest(n) )
    print("v value after " + str(n) + " trials:")
    print( vtest(n) )

    '''
    count = 0
    for i in range(n):
        point = generate_coords()
        vertices = []
        for i in range(4):
            vertices.append(generate_coords())
        if (is_inside(point, vertices)):
            count += 1

    print("Average of convex after {} runs".format(n))
    print(count / n)
    '''



#returns the s and t values that give that generate the point of intersection on the line containing {p1,p2} and the line containing {q1,q2}
def find_intersection(p_one, p_two, q_one, q_two):
    # matrix of form 
    # [p1 - p2, q2 - q1](s,t) = q2 - p2
    # [[p1[0] - p2[0], p1[1] - p2[1]], [q2[0] - q1[0], q2[1] - q1[1]]] (t,s) = [q2[0] - p2[0], q2[1] - p2[1]]
    matrix = [ [p_one[0] - p_two[0], p_one[1] - p_two[1]] ]
    matrix.append([q_two[0] - q_one[0], q_two[1] - q_one[1]])

    inverted = invert_matrix(matrix)

    vec = ( q_two[0] - p_two[0] , q_two[1] - p_two[1] )

    result = apply_matrix(inverted, vec)

    return result    


def invert_matrix(m):  # m is a 2x2 matrix
    # m = [ [a, c], [b, d] ]
    a = m[0][0]
    b = m[1][0]
    c = m[0][1]
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


def epsilon(p_one, p_two, q_one, q_two):

    result = find_intersection(p_one, p_two, q_one, q_two)

    if(not is_intersecting(result)):
        return 0
    else:
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
    #then need to find crossing
    return crossing_sign(over, under)


def ptest(n):  
    crossings = 0
    positive = 0
    negative = 0
    length = 0

    for i in range(n):
        p_one = generate_coords()
        p_two = generate_coords()

        dist = distance_between(p_one, p_two)

        q_one = generate_coords()
        q_two = generate_coords()

        '''
        result = find_intersection(p_one, p_two, q_one, q_two)
        if (is_intersecting(result)):
            crossings += 1
        '''

        epsilon_one = epsilon(p_one, p_two, q_one, q_two)
        crossings += epsilon_one * epsilon_one

        length += dist

        if (i % 10_000 == 0) and (i != 0):
            print("p value after {} trials:".format(i), crossings / i / 2)

        if (epsilon_one == 1):
            positive += 1
        elif (epsilon_one == -1):
            negative += 1

    '''
    print("Number of positives:")
    print(positive)
    print("Number of negatives:")
    print(negative)
    '''

    print("Average distance of l_1")
    print(length / n)

    return ( (crossings / n) * 0.5 )


def utest(n):
    partial_sum = 0
    positive = 0
    negative = 0

    for i in range(n):
        # ell_1 = ell_2
        p_one = generate_coords()
        p_two = generate_coords()
        #p1, p2 make line 1 and line 2

        # ell_1' ell_2'
        q_one = generate_coords()
        q_two = generate_coords()
        q_thr = generate_coords()
        #q1, q2 make line 1 prime
        #q2, q3 make line 2 prime

        epsilon_one = epsilon(p_one, p_two, q_one, q_two)
        epsilon_two = epsilon(p_one, p_two, q_two, q_thr)

        product = epsilon_one * epsilon_two

        partial_sum += epsilon_one * epsilon_two

        if (product == 1):
            positive += 1
        elif (product == -1):
            negative += 1
        

        if (i % 10_000 == 0) and (i != 0):
            print("u value after {} trials:".format(i), partial_sum / i)

    #total_non_zero = positive + negative

    #print("Number of non-zero over total")
    #print(total_non_zero / n)

    #print("Number of positives:")
    #print(positive)
    #print(positive / total_non_zero)
    #print("Number of negatives:")
    #print(negative)
    #print(negative / total_non_zero)
    

    return (partial_sum / n)


def vtest(n):
    partial_sum = 0

    for i in range(n):
        # ell_1 and ell_2
        p_one = generate_coords()
        p_two = generate_coords()
        p_thr = generate_coords()
        #p1, p2 make line 1
        #p2, p3 make line 2

        # ell_1' ell_2'
        q_one = generate_coords()
        q_two = generate_coords()
        q_thr = generate_coords()
        #q1, q2 make line 1 prime
        #q2, q3 make line 2 prime

        epsilon_one = epsilon(p_one, p_two, q_one, q_two)
        epsilon_two = epsilon(p_two, p_thr, q_two, q_thr)

        partial_sum += epsilon_one * epsilon_two

        if (i % 10_000 == 0) and (i != 0):
            print("v value after {} trials:".format(i), partial_sum / i)

    return (partial_sum / n)


#returns true if the point p is inside the polygon given by the list of vertices with edges between the ith and (i+1)th vertices
def is_inside(point, vertices):
    edges_match = True
    # record the sign of the point with an edge (the one between the first and last vertices)
    # turn those four vertices into vectors

    u = tuple( numpy.subtract(vertices[len(vertices) - 1], vertices[0]) )
    v = tuple( numpy.subtract(vertices[len(vertices) - 1], point) )


    first_sign = crossing_sign(u, v)
    for i, vec in enumerate(vertices):
        #see if the sign of the point with the edge between vertices i and i+1 match the sign of the first
        first = tuple( numpy.subtract( vec, vertices[ (i+1) % len(vertices) ] ) )
        second = tuple( numpy.subtract( vec, point ) )
        if (first_sign != crossing_sign(first,second)):
          	edges_match = False
    # will return true if and only if every edge has the same sign. That is, the point is always to the left/right of a directed edge
    return edges_match


def project(vec):
    # take 3 vector (x,y,z) and turns that in to a two vector
    x = vec[0]
    y = vec[1]

    return (x, y)


def distance(vec):
    x = vec[0]
    y = vec[1]
    z = vec[2]

    return math.sqrt(x**2 + y**2 + z**2)

def distance_between(p, q):
    return distance(tuple( numpy.subtract(p, q) ))

'''
# for the cube case
def generate_coords():
    return (random.uniform(0,1), random.uniform(0,1), random.uniform(0,1))
'''

def n_norm(vec):
    n = 1

    x = vec[0]
    y = vec[1]

    return ((abs(x) ** n) + (abs(y) ** n)) ** (1 / n)

# for the ball under n-norm case
def generate_coords():
    vec = (random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1))

    if (n_norm(vec) > 1):
        return generate_coords()
    
    return vec

'''
# for the ball case
def generate_coords():
    vec = (random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1))

    if (distance(vec) > 1):
        return generate_coords()
    
    return vec
'''

'''
# the case of the cylinder
def generate_coords():
    vec = (random.uniform(-1,1), random.uniform(-1,1), random.uniform(0,1))

    x = vec[0]
    y = vec[1]
    
    if (math.sqrt(x**2 + y**2) > 1):
        return generate_coords()
    
    return vec
'''

'''
# triangular prism
def generate_coords():
    vec = (random.uniform(0,1), random.uniform(0,1), random.uniform(0,1))

    x = vec[0]
    y = vec[1]

    if (y > 1 - x):
        return generate_coords()

    return vec
'''

'''
# uniform spherical coords
def generate_coords():
    r = random.uniform(0, 1)
    theta = random.uniform(0, 2 * math.pi)
    phi = random.uniform(0, math.pi)

    x = r * math.cos(theta) * math.sin(phi)
    y = r * math.sin(theta) * math.sin(phi)
    z = r * math.cos(phi)

    return (x, y, z)
'''

'''
# unif cylindrical
def generate_coords():
    r = random.uniform(0, 1)
    theta = random.uniform(0, 2 * math.pi)
    z = random.uniform(0, 1)

    x = r * math.cos(theta)
    y = r * math.sin(theta)
    
    return (x, y, z)
'''

'''
# non unif cylindrical
def generate_coords():
    x = random.uniform(-1, 1)
    y_bounds = math.sqrt(1 - x**2)
    y = random.uniform(-y_bounds, y_bounds)
    z = random.uniform(0, 1)

    return (x, y, z)
'''

'''
# rect prism
def generate_coords():
    return (random.uniform(0, 2), random.uniform(0, 1), random.uniform(0, 1))
'''


def is_intersecting(result):
    # checks 0 <= s <= 1 and 0 <= t <= 1
    if ((0 <= result[0] <= 1) and (0 <= result[1] <= 1)):
        return True

    return False

def find_overstrand(s, t, p_one, p_two, q_one, q_two):
    # given s and t
    p_z = p_one[2] * s + (1 - s) * p_two[2]
    #       p1_z                    p2_z

    q_z = q_one[2] * t + (1 - t) * q_two[2]
    #       q1_z                    q2_z

    if (p_z > q_z):
        return 1

    return 2

def crossing_sign(u, v):
	# basically sign of det[u, v]
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


if __name__ == "__main__":
    main()