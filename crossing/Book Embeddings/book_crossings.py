def check_crossings_case3(sheets): #**
    crossing = 0
    # check (0,2) and (1,5)
    if (find_over({0, 2}, {1, 5}, sheets) == {0, 2}):
        crossing += 1
    #elif (find_over({0, 2}, {1, 5}, sheets) == {1, 5}):
    else:
        crossing -= 1

    # check {0, 2} and {1, 3}
    if (find_over({0, 2}, {1, 3}, sheets) == {0, 2}):
        crossing -= 1
    #elif (find_over({0, 2}, {1, 3}, sheets) == {1, 3}):
    else:
        crossing += 1

    # check {0, 4} and {1，5}
    if (find_over({0, 4}, {1, 5}, sheets) == {0, 4}):
        crossing -= 1
    #elif (find_over({0, 4}, {1, 5}, sheets) == {1, 5}):
    else:
        crossing += 1

    # check {0, 4} and {3, 5}
    if (find_over({0, 4}, {3, 5}, sheets) == {0, 4}):
        crossing += 1
    #elif (find_over({0, 4}, {3, 5}, sheets) == {3, 5}):
    else:
        crossing -= 1

    # check {4, 2} and {1，3}
    if (find_over({2, 4}, {1, 3}, sheets) == {2, 4}):
        crossing += 1
    #elif (find_over({2, 4}, {1, 3}, sheets) == {1, 3}):
    else:
        crossing -= 1

    # check {2, 4} and {3, 5}
    if (find_over({2, 4}, {3, 5}, sheets) == {2, 4}):
        crossing -= 1
    #elif (find_over({2, 4}, {3, 5}, sheets) == {3, 5}):
    else:
        crossing += 1

    return crossing


def check_crossings_case2(sheets):
    crossing = 0

    # check {0, 3} and {2, 5}
    if (find_over({0, 3}, {2, 5}, sheets) == {0, 3}):
        crossing += 1
    #elif (find_over({0, 3}, {2, 5}, sheets) == {2, 5}):
    else:
        crossing -= 1

    # check {0, 3} and {2, 4}
    if (find_over({0, 3}, {2, 4}, sheets) == {0, 3}):
        crossing -= 1
    #elif (find_over({0, 3}, {2, 4}, sheets) == {2, 4}):
    else:
        crossing += 1

    # check {1, 3} and {2，5}
    if (find_over({1, 3}, {2, 5}, sheets) == {1, 3}):
        crossing -= 1
    #elif (find_over({1, 3}, {2, 5}, sheets) == {2, 5}):
    else:
        crossing += 1

    # check {1, 3} and {2, 4}
    if (find_over({1, 3}, {2, 4}, sheets) == {1, 3}):
        crossing += 1
    #elif (find_over({1, 3}, {2, 4}, sheets) == {2, 4}):
    else:
        crossing -= 1

    return crossing


def find_over(edge1, edge2, sheets): #**
    #find the overstrand
    for index, sheet in enumerate(sheets):
        for e in sheet:
            if (e == edge1):
                index1 = index
            elif (e == edge2):
                index2 = index

    if (index1 > index2):
        return edge2
    elif (index2 > index1):
        return edge1

    return edge1 # this probably should never happen