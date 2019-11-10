# # First Pass Solution
# def earliest_ancestor(ancestors, starting_node):
#     # start a queue and add starting node
#     q = []
#     q.append([starting_node])
#     # initialize visited cache
#     visited = set()
#     # initialize store of path ways
#     store = []
#     # while queue is not empty
#     while len(q) > 0:
#         # dequeue first path and add the path to store of path ways
#         path = q.pop(0)
#         store += [path]
#         # print(path)

#         # grab last node from path
#         v = path[-1]
#         # print(v)

#         # if the node has not been visited
#         if v not in visited:
#             # mark node as visited
#             visited.add(v)
#             # loop through list of connections
#             for tup in ancestors:
#                 # if the node is a child (i.e. second element of tuple)
#                 if v == tup[1]:
#                     # append the parent of the child to path and add to back of queue
#                     q.append(path + [tup[0]])
#     # result after while loop is finished is the list that has the highest len
#     result = max(store, key=len)
#     # if len is only 1, we know the list only has original element and no parents
#     if len(result) == 1:
#         return -1
#     # else return last element of the result list
#     else:
#         return result[-1]


# def earliest_ancestor(ancestors, starting_node):
#     # start a queue and add starting node
#     q = []
#     q.append([starting_node])
#     # initialize store of path
#     store = [[starting_node]]
#     # while queue is not empty
#     while len(q) > 0:
#         # dequeue first path and add the path to store of path ways
#         path = q.pop(0)
#         if len(path) > len(store[0]):
#             store[0] = path
#         if len(path) == len(store[0]) and path[-1] < store[0][-1]:
#             store[0] = path
#         # print(path, store)

#         # grab last node from path
#         last = path[-1]

#         # loop through list of connections
#         for tup in ancestors:
#             # if the node is a child (i.e. second element of tuple)
#             if last == tup[1]:
#                 # append the parent of the child to path and add to back of queue
#                 q.append(path + [tup[0]])
#     # if len is only 1, we know the list only has original element and no parents
#     if len(store[0]) == 1:
#         return -1
#     # else return last element of the result list
#     else:
#         return store[0][-1]


def earliest_ancestor(ancestors, starting_node):
    # start a queue and add starting node
    q = []
    q.append(starting_node)
    # initialize store of earliest ancestors
    anc_list = [starting_node]
    # while queue is not empty
    while len(q) > 0:
        # dequeue first child
        cur_anc = q.pop(0)
        # ancestor is smallest number in ancestor list if ancestor list is not empty
        if len(anc_list) > 0:
            ancestor = min(anc_list)
        # clear anc_list for new loop through ancestors/family connections list
        anc_list = []
        # loop through list of family connections
        for tup in ancestors:
            # if cur_anc is a child (i.e. second element of tuple)
            if cur_anc == tup[1]:
                # append the parent of the child to queue and anc_list
                q.append(tup[0])
                anc_list.append(tup[0])

    # if ancestor is the same as start node, return -1 due to no parents
    if ancestor == starting_node:
        return -1
    # else return ancestor
    else:
        return ancestor


ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (11, 8),
             (4, 5), (4, 8), (8, 9), (10, 1)]
print(earliest_ancestor(ancestors, 9))
