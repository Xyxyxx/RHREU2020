# simulates greedy book embeddings of K_n
# seems to show that the number of sheets grows O(n)!

import time
import random
import math
import numpy
import operator as op
from functools import reduce
from copy import deepcopy

def main():
    tic = time.perf_counter()
    #n = trials
    n = 100_000

    total_sheets = 0

    #k = int(input("Enter the number of vertices"))

    k = 15  

    edges = create_edges(k)

    for i in range(n):
        sheets = general_book_embeddings(edges, k)
        total_sheets += len(sheets)

        if (i % 10000 == 0) and (i != 0):
            print("total sheets:", total_sheets, "\ntrials:", i)
            print("average # sheets after", i, "trials:", total_sheets / i)

    print("the average number of sheets in the random process is:", total_sheets / n)

    toc = time.perf_counter()
    print("Program executed in", toc - tic, "seconds")


def general_book_embeddings(edges, k):
    # since python is Pepega, I have to actually do this
    local_edges = deepcopy(edges)

    sheets = [[]]
    
    num_edges = len(edges)
    numbered_edges = num_edges - 1

    for i in range(num_edges):
        # we first generate a random edge
        n = random.randint(0, numbered_edges - i) 
        edge = local_edges.pop(n)

        can_place = True

        # then we loop through the sheets
        # and checking if we can place our edge inside the sheet
        for sheet in sheets:
            if (len(sheet) == 0):
                # if the sheet is empty, then we can place the sheet inside
                sheet.append(edge)
            else:
                can_place = True
                # next check if there is an intersection in the sheet
                # for each edge in the sheet
                for e in sheet:
                    if (general_intersection(e, edge, k) == False):
                        can_place = False
                        break
                if (can_place):
                    sheet.append(edge)
                    break
        if not (can_place):
            sheets.append([edge])
    return sheets


def general_generate_edge(n):
    a = random.randint(0, n - 1)
    b = random.randint(0, n - 1)

    diff = abs(a - b)

    if (diff == 1):
        return general_generate_edge(n)
    elif (diff == n - 1):
        return general_generate_edge(n)
    elif (a == b):
        return general_generate_edge(n)

    return {a, b}


def general_partition(a, b, n):
    diff1 = abs(a - b)
    diff2 = n - diff1

    range1 = []
    counter = min(a ,b)
    for i in range(diff1 + 1):
        range1.append(counter % n)
        counter += 1

    range2 = []
    counter = max(a, b)
    for i in range(diff2 + 1):
        range2.append(counter % n)
        counter += 1

    return range1, range2

def create_edges(n):
    possible_edges = []
    while (len(possible_edges) != ncr(n, 2) - n):
        edge = general_generate_edge(n)
        if edge in possible_edges:
            continue
        else:
            possible_edges.append(edge)

    return possible_edges

def general_intersection(edge1, edge2, k):

    if (len(edge1) == set()):
        return True
    elif (edge1 == edge2):
        return False

    edge1 = list(edge1)

    a = edge1[0]
    b = edge1[1]

    range1, range2 = general_partition(a, b, k)

    edge2 = list(edge2)
    
    x = edge2[0]
    y = edge2[1]
    
    if (x in range1) and (y in range1):
        return True
    elif (x in range2) and (y in range2):
        return True
    
    return False

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom

if __name__ == "__main__":
    main()