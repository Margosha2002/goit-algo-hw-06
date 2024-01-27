# Graph's Research Results

### DFS

| Source |    Path     |
| :----: | :---------: |
|   1    | 1 2 4 6 5 3 |
|   2    | 2 1 3 5 6 4 |
|   3    | 3 1 2 4 6 5 |
|   4    | 4 2 1 3 5 6 |
|   5    | 5 3 1 2 4 6 |
|   6    | 6 4 2 1 3 5 |

### BFS

| Source |    Path     |
| :----: | :---------: |
|   1    | 1 2 3 4 5 6 |
|   2    | 2 1 4 3 6 5 |
|   3    | 3 1 5 2 4 6 |
|   4    | 4 2 6 1 5 3 |
|   5    | 5 3 6 1 4 2 |
|   6    | 6 4 5 2 1 3 |

## Conclusion

###

In the case of DFS, a recursive function is used to traverse the graph, while for BFS, a queue is employed for systematic examination of all neighbors at each level of the graph. Both algorithms return lists of vertices that form the discovered paths.
The choice between BFS and DFS may depend on the specific constraints of each method. Despite its higher memory resource demands, BFS ensures the discovery of the shortest route. On the other hand, DFS is more memory-efficient but may lead to less optimal solutions in the context of finding paths.
