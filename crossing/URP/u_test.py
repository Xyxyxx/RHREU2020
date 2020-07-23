# test for just the u case

from URP.test_crossings import *
from URP.test_convex import *

def main():
    n = 1_000_000_000
    partial_sum = 0
    positive = 0
    negative = 0
    total = 0

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

        S = [p_one, p_two, q_one, q_two, q_thr]

        P = jarvis(S)
        
        '''
        if (len(P) == 5):
            total += product
            if (product > 0):
                partial_sum += 1
                positive += 1
            elif (product < 0):
                partial_sum += 1
                negative += 1
        '''

        if (len(P) == 4):
            total += product
            if (product > 0):
                partial_sum += 1
                positive += 1
            elif (product < 0):
                partial_sum += 1
                negative += 1

        if (i % 1_000 == 0) and (i != 0):
            print("Neg/Convex after", i, "trials:", negative / partial_sum)
            print("Pos/Convex after", i, "trials:", positive / partial_sum)
            print("Difference after", i, "trials", (positive - negative) / partial_sum)

    '''
    print("#Non-zero Convex / #Total =", partial_sum / n)
    print("Negative / Convex", negative / partial_sum)
    print("Positive / Convex", positive / partial_sum)
    print("Non-zero / Convex", partial_sum / total)
    print("Expected value of convex:", total / n)
    '''

    print("Negative / Convex = ", negative / partial_sum)
    print("Positive / Convex =", positive / partial_sum)
    



if __name__ == "__main__":
    main()