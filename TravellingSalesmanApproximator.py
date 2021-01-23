import itertools

# consumes a 2D square list and an integer row and outputs the min entry
# in that row of the array


def minInRow(array, row):
    min = array[row][0]
    index = 0
    if (min == 0):
        min = array[row][1]
        index = 1
    size = len(array)
    for i in range(0, size):
        if (array[row][i] > 0 and array[row][i] < min):
            min = array[row][i]
            index = i
    return [min, row, index]


# path is a list of ints
# cost is a 2d square list of lists of ints
def pathCost(path, cost):
    pathLength = len(path)
    distance = 0
    for i in range(0, pathLength):
        if i == pathLength - 1:
            distance += cost[path[i]][path[0]]
        else:
            distance += cost[path[i]][path[i+1]]
    return distance


# cost is a 2D square list of lists of ints
# solves the TSP for the given instance, but in exponential time
def tspSolve(cost):
    size = len(cost)
    basePath = list(range(0, size))
    paths = list(map(list, list(itertools.permutations(basePath))))

    numPaths = len(paths)
    min = -1
    for i in range(0, numPaths):
        currPathCost = pathCost(paths[i], cost)
        if min == -1 or currPathCost < min:
            min = currPathCost
            basePath = paths[i]

    print([min, basePath])
    return [min, basePath]


# cost is a 2D square list of lists of ints
# approximates a solution to the TSP. It will be at most 2 x worse than OPT
def nearestAddition(cost):
    solution = []
    size = len(cost)

    shortestDist = [-1, 0, 0]     # shortestDist = closest 2:[dist, row, index]
    for i in range(0, size):
        if (minInRow(cost, i)[0] < shortestDist[0] or shortestDist[0] == -1):
            shortestDist = minInRow(cost, i)

    solution.append(shortestDist[1])
    solution.append(shortestDist[2])

    # print(solution)

    for i in range(0, size - 2):
        min = -1
        index = 0
        for j in range(0, len(solution)):
            for k in range(0, size):
                if (k not in solution) and (min == -1 or cost[solution[j]][k] < min):
                    min = cost[solution[j]][k]
                    index = [j, k]
        # print(index)
        if index[0] == 0:
            # print("inserting city", index[1], "before city", solution[index[0]])
            solution.insert(0, index[1])
        elif index[0] == len(solution) - 1:
            # print("inserting city", index[1], "after city", solution[index[0]])
            solution.append(index[1])
        else:
            # print("inserting city", index[1], "near city", solution[index[0]])
            if cost[solution[index[0] + 1]][index[1]] > cost[solution[index[0] - 1]][index[1]]:
                # print("inserting city", index[1], "before city", solution[index[0]])
                solution.insert(index[0], index[1])
            else:
                # print("inserting city", index[1], "after city", solution[index[0]])
                solution.insert(index[0] + 1, index[1])
        # print(solution)
        # print("---------")
    solution.append(solution[0])
    print(solution)
    return solution


example1 = [[0, 3, 5, 4, 6],
            [3, 0, 3, 1, 4],
            [5, 3, 0, 4, 5],
            [4, 1, 4, 0, 2],
            [6, 4, 5, 2, 0]]

example2 = [[0, 25, 10, 15],
            [25, 0, 10, 45],
            [10, 10, 0, 5],
            [15, 45, 5, 0]]

example3 = [[0, 10, 15, 20],
            [10, 0, 35, 25],
            [15, 35, 0, 30],
            [20, 25, 30, 0]]

print(pathCost(nearestAddition(example3), example3))
