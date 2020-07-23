import math
import random

def partition():
    a, b = generate_edge()
    
    diff1 = abs(a - b)
    diff2 = 6 - diff1

    range1 = []
    counter = min(a ,b)
    for i in range(diff1 + 1):
        range1.append(counter % 6)
        counter += 1

    range2 = []
    counter = max(a, b)
    for i in range(diff2 + 1):
        range2.append(counter % 6)
        counter += 1

    return range1, range2

def generate_edge():
    a = random.randint(0, 5)
    b = random.randint(0, 5)

    diff = abs(a - b)

    if (diff == 1):
        return generate_edge()
    elif (diff == 5):
        return generate_edge()
    elif (a == b):
        return generate_edge()

    return {a, b}

def main():
    possible_edges = []

    while (len(possible_edges) != 9):
        edge = generate_edge()
        if edge in possible_edges:
            continue
        else:
            possible_edges.append(edge)

    print(possible_edges)

main()