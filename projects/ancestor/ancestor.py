
def earliest_ancestor(ancestors, starting_node):
    q = []
    q.append([starting_node])
    visited = set()
    store = []
    while len(q) > 0:
        path = q.pop(0)
        store += [path]
        # print(path)
        v = path[-1]
        # print(v)
        if v not in visited:
            visited.add(v)
            for tup in ancestors:
                if v == tup[1]:
                    q.append(path + [tup[0]])
    result = max(store, key=len)
    if len(result) == 1:
        return -1
    else:
        return result[-1]


ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
             (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(ancestors, 9)
