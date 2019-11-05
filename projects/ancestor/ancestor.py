
def earliest_ancestor(ancestors, starting_node):
    # start a queue and add starting node
    q = []
    q.append([starting_node])
    # initialize visited cache
    visited = set()
    # initialize store of path ways
    store = []
    # while queue is not empty
    while len(q) > 0:
        # dequeue first path and add the path to store of path ways
        path = q.pop(0)
        store += [path]
        # print(path)

        # grab last node from path
        v = path[-1]
        # print(v)

        # if the node has not been visited
        if v not in visited:
            # mark node as visited
            visited.add(v)
            # loop through list of connections
            for tup in ancestors:
                # if the node is a child (i.e. second element of tuple)
                if v == tup[1]:
                    # append the parent of the child to path and add to back of queue
                    q.append(path + [tup[0]])
    # result after while loop is finished is the list that has the highest len
    result = max(store, key=len)
    # if len is only 1, we know the list only has original element and no parents
    if len(result) == 1:
        return -1
    # else return last element of the result list
    else:
        return result[-1]


ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
             (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(ancestors, 9)
