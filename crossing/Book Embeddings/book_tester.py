import general_book_sim as gb

def main():
    edges = gb.create_edges(6)

    print(edges)

    edge = gb.general_generate_edge(6)

    print(edge)

    edge = list(edge)


    a = edge[0]
    b = edge[1]

    range1, range2 = gb.general_partition(a, b, 6)
    print(range1)
    print(range2)

    for e in edges:
        if gb.general_intersection(e, edge, 6):
            print(e, "does not intersect", edge)
        else: 
            print(e, "intersects", edge)


if __name__ == "__main__":
    main()