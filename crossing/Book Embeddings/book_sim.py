# this program simulates the greedy book embeddings of K_6

import time
import random
import math
import numpy
import operator as op
from functools import reduce

def main():
    tic = time.perf_counter()
    # n = trials
    n = 1_000_000
    total_sheets = 0

    for i in range(n):
        sheets = K_6()
        total_sheets += len(sheets)
        if (i % 10_000 == 0) and (i != 0):
            print("average # sheets after", i, "trials:", total_sheets / i)
    print("the average number of sheets in the random process is:", total_sheets / n)

    toc = time.perf_counter()
    print("Program executed in", toc - tic, "seconds")


def K_6():
    # our vertices will be numbered 0 - 5
    # [0, 1, 2, 3, 4, 5]

    edges = [{2, 5}, {3, 5}, {0, 2}, {0, 4}, {1, 4}, {1, 5}, {2, 4}, {1, 3}, {0, 3}] # list of all possible edges (aka all interior edges)
    # and then we will remove as we randomly pick edges

    return book_embedding(edges)


def book_embedding(edges):
    #distribute all 15 edges into different sheets
    
    sheets = [[]] #LOL containing all sheets


    for i in range(9):
        # we first generate a random edge
        n = random.randint(0, 8 - i) 
        edge = edges.pop(n)

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
                    if (intersection(e, edge) == False):
                        can_place = False
                        break
                if (can_place):
                    sheet.append(edge)
                    break
        if not (can_place):
            sheets.append([edge])
    return sheets



def intersection(edge1, edge2):
    # edge1 will be our original edge
    # of form (a, b)
    # edge2 will be the one where we check if it intersects
    # edge1
    # edge2 is of form (x, y)

    # this func will return
    # True if we do NOT have an intersection
    # and False if we DO

    if (len(edge1) == set()):
        return True
    elif (edge1 == edge2):
        return False

    edge1 = list(edge1)

    a = edge1[0]
    b = edge1[1]

    range1, range2 = partition(a, b)

    edge2 = list(edge2)
    
    x = edge2[0]
    y = edge2[1]
    
    if (x in range1) and (y in range1):
        return True
    elif (x in range2) and (y in range2):
        return True
    
    return False


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

    return {a, b} #edge should be unordered


def partition(a, b):
    # takes in two values a, b which defines our edge
    # and partitions the circle along that edge
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

if __name__ == "__main__":
    main()