# this program simulates the nongreedy book embeddings of K_6

import random
import time
from book_crossings import *

def main():
    edges = [{2, 5}, {3, 5}, {0, 2}, {0, 4}, {1, 4}, {1, 5}, {2, 4}, {1, 3}, {0, 3}] # list of all interior edges of K_6
    num_sheets = 0

    trials = 100_000_000

    trivial = 0
    hopf = 0 
    solomon = 0

    total_cross_1 = 0

    total_cross_2 = 0

    case2_link = 0

    case2_hopf = 0

    case3_hopf = 0
    tic = time.perf_counter()
    for i in range(trials):
        sheets = shuffled_edges_book_embedding(edges)

        crossing_1 = check_crossings_case2(sheets)

        if (crossing_1 == 0):
            trivial += 1
        elif (crossing_1 == 2):
            hopf += 1
            case2_hopf += 1
        elif (crossing_1 == 4):
            solomon += 1
            print("Probably shouldn't happen")
        elif (crossing_1 == -2):
            hopf += 1
            case2_hopf += 1
        elif (crossing_1 == -4):
            solomon += 1
            print("Probably shouldn't happen")
        else:
            print("Bad crossing?")

        crossing_2 = check_crossings_case3(sheets)
        if (crossing_2 == 0):
            trivial += 1
        elif (crossing_2 == 2):
            hopf += 1
            case3_hopf += 1
        elif (crossing_2 == 4):
            solomon += 1
        elif (crossing_2 == -2):
            hopf += 1
            case3_hopf += 1
        elif (crossing_2 == -4):
            solomon += 1
        else:
            print("Bad crossing?")

        total_cross_1 += crossing_1
        total_cross_2 += crossing_2

        case2_link += abs(crossing_1) / 2
        
        if (i % 100_000 == 0 and i != 0):
            toc = time.perf_counter()
            print(i, "Trials")
            print("Trivial:", trivial)
            print("Hopfs:", hopf)
            print("Solomons:", solomon)
            print("Prob of Case 2 Hopf:", case2_hopf / (i + 1))
            print("Solomon prob:", solomon / (i + 1))
            print("Case 3 Hopf:", case3_hopf / (i + 1))
            print("Prob of Hopf:", hopf / (i + 1))
            print("Squared linking number case 2:", (total_cross_1 ** 2) / (4 * (i + 1)))
            print("100k trials done in", toc - tic, "seconds")
            tic = time.perf_counter()

    print("Trivial:", trivial)
    print("Hopfs:", hopf)
    print("Solomons:", solomon)
    print("Average squared linking number for Case 2:", (total_cross_1 / 2) * (total_cross_1 / 2) * (1 / trials))
    print("Average squared linking number for Case 3:", (total_cross_2 / 2) * (total_cross_2 / 2) * (1 / trials))


def shuffled_edges_book_embedding(edges):
    #place every edge on its own sheet
    sheets=[]
    
    for edge in edges:
        sheets.append([])
        sheets[-1].append(edge)

    #randomly shuffle (Fisher Yates Shuffle) the sheets to get any permutation of edge placements
    random.shuffle(sheets)

    return sheets


if __name__ == "__main__":
    main()