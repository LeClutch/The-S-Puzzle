#https://en.wikipedia.org/wiki/A*_search_algorithm#Pseudocode

import time
import sys
import copy
import threading

finalPuzzle = [[1,2,3],
               [4,5,6],
               [7,8,9]]

searchList = []
#############State object
class State:
  def __init__(self, node, previous, gValue, fValue):
    self.node = str(node)
    self.nodeList = node
    self.previous = previous
    self.gValue = gValue
    self.fValue = fValue

  def __hash__(self):
      return hash((self.node, self.previous, self.gValue, self.fValue))

  def __eq__(self, other):
      return (self.node, self.previous, self.gValue, self.fValue) == (other.node, other.previous, other.gValue, other.fValue)

###############################################################################################

def get_moves( num,  state = [] ):
    i = int
    j = int

    for ii, lst in enumerate(state):
        for jj, number in enumerate(lst):
            if number == num:
                i=ii
                j=jj


    old = int
    new = int
    up  = [copy.copy(element) for element in state]
    down = [copy.copy(element) for element in state]
    right = [copy.copy(element) for element in state]
    left = [copy.copy(element) for element in state]
    possibleMoves = []


    #MOVE UP
    if i > 0:
       # print(up)
        old = up[i][j]
        new = up[i-1][j]
        up[i][j] = new
        up[i-1][j] = old
        possibleMoves.append(up)

    #MOVE DOWN
    if i < 2 :
       # print(down)
        old = down[i][j]
        new = down[i+1][j]
        down[i][j] = new
        down[i+1][j] = old
        possibleMoves.append(down)

    #MOVE RIGHT
    if j < (len(right[i])-1):
        #print(right)
        old = right[i][j]
        new = right[i][j+1]
        right[i][j] = new
        right[i][j+1] = old
        possibleMoves.append(right)

    #MOVE LEFT
    if j > 0:
       # print(left)
        old = left[i][j]
        new = left[i][j-1]
        left[i][j] = new
        left[i][j-1] = old
        possibleMoves.append(left)

    return possibleMoves


##########################################  DFS
#DFS LIKE IN NOTES LECTURES
def dfs(puzzle, goal):
  solutionPath = []
  noSolution = []
  endTime = time.time() + 60  #TIMER
  while time.time() < endTime:  # timer
    '''do whatever you do'''
    # maintain a stack of paths
    openStack = []
    closedStack = []

    # push the first path into the stack
    openStack.append(puzzle)

    while openStack:
        # remove leftmost state from open, call it x
        x = openStack.pop()
        solutionPath.append(x)
        # path found
        if x == goal:
            #solutionPath.append(x)
            closedStack.append(x)
            #print("--------------------------")
            #print("-------SEARCH PATH--------")
            # for item in closedStack:
            #     for items in item:
            #         print(items)
            #     print()
            # print(len(closedStack))
            #
            # print("--------------------------")
            # print("------SOLUTION PATH-------")
            # for item in solutionPath:
            #     for items in item:
            #         print(items)
            #     print()
            # print(len(solutionPath))

            return solutionPath

        # enumerate all adjacent nodes, construct a new path and push it into the stack
        moves = get_moves(8, x)

        #reverse the order of the list to stack the nodes in the right order
        moves.reverse()
        #put x in closed
        closedStack.append(x)

        #Discard children of x if already in open or closed
        for adjacent in moves:
            if (adjacent not in closedStack) and (adjacent not in openStack):
                solutionPath = list(solutionPath)
                solutionPath.append(adjacent)
                openStack.append(adjacent)

        if(time.time() > endTime):
            break
  if not noSolution:
    noSolution.append([["No solution"]])
    return noSolution


###############################################################################################
#Adapted from https://eddmann.com/posts/using-iterative-deepening-depth-first-search-in-python/
searchPath =[]
solutionPath = []
def id_dfs(puzzle, goal):
    import itertools
    global searchPath

    endTime = time.time() + 60 #TIMER
    while time.time() < endTime:  # timer
        '''do whatever you do'''
        def dfs(currentpath, depth):


            if depth == 0:
                return
            if currentpath[-1] != goal:
                searchPath.append([currentpath])
            if currentpath[-1] == goal:
                solutionPath.append([currentpath])
                # print("--------------------------")
                # print("------SOLUTION PATH-------")
                # for item in solutionPath[0][0]:
                #    for t in item:
                #           print(t)
                #    print()
                #print((len(solutionPath[0][0])-1))
                return solutionPath
            possibleMoves = get_moves(9, currentpath[-1])
            for move in possibleMoves:
                if move not in currentpath:
                    next_route = dfs(currentpath + [move], depth - 1)
                    if next_route:

                        return next_route

        for depth in itertools.count():
            route = dfs([puzzle], depth)
            if route:
                return route
            if (time.time() > endTime):
                break


    if not solutionPath:
        searchPath.clear()
        searchPath = [["No solution"]]
        solutionPath.append(["No solution"])
        return solutionPath

###############################################################################################
# puzzle here is a State object

def astar(puzzleObject, goal):
  noSolution = []

  endTime = time.time() + 60  #TIMER
  while time.time() < endTime:  # timer
        '''do whatever you do'''

        openList = []
        openList.append(puzzleObject)

        allNodesDict = {}
        allNodesDict[puzzleObject.node] = puzzleObject


        searchList.append(puzzleObject.node)

        #initialize dictionary for tracking previous node
        #prevDict = {} #dict()
        #prevDict[0] = -1 #start node with no previous node

        #initialize dictionary for tracking g values [float('inf')]
        #gValue = {}
        #gValue[0] = 0

        # initialize dictionary for tracking g values [float('inf')]
        fValueDict = {}
        #fValue[0] = heur(puzzle)
        fValueDict[puzzleObject] = puzzleObject.fValue
        #0:puzzle1.fValue

        #{puzzle1 : puzzle1.fValue}

        #puzzle1 ([], [pre], )
        #puzzle2
        #puzzle3

        #if puzzle not in openList:
        #    del fValueDict[puzzle]
        #elif puzzle in openList:
        #    fValueDict.setdefault(puzzle, puzzle.fValue)
        #    #if puzzle not in fValueDict: #if not(fValueDict.has_key(puzzle)):
        #    #    fValueDict[puzzle] = puzzle.fValue

        #if dict[key][]

        cv = 0

        while openList:
            # we might just create the fValue Dict in here so it destroys it upon exit (loop scope)
            fValueDict.clear() #clear and repopulate every iteration of while loop to keep updated
            for nodesObject in openList:
                fValueDict.setdefault(nodesObject, nodesObject.fValue) # CHANGE TO ADD OR APPEND OR WHATEVER IF PROBLEMS OCCUR

            #Find the smallest fValue in fValueDict and return its corresponding puzzle object (used as a key)
            nodeObject = min(fValueDict, key = lambda k : fValueDict[k])

            searchList.append(nodeObject.node)


            if nodeObject.nodeList == goal:
                return buildPath(nodeObject, allNodesDict)
                #return buildPath(allNodesDict.get(str(nodeObject.previous)), allNodesDict)
            if (time.time() > endTime):
                break
            openList.remove(nodeObject)

            # List of nodes only, not objects of Class State
            neighboursList = []

            i = 1

            while i < 10:
                if (time.time() > endTime):
                    break
                neighboursList.extend(get_moves(i, nodeObject.nodeList))
                for neighbourR in get_moves(i, nodeObject.nodeList):

                    if (time.time() > endTime):
                        break

                    allNodesDict.setdefault(str(neighbourR), State(neighbourR, nodeObject.nodeList, (nodeObject.gValue + 1), (nodeObject.gValue + 1 + heur(neighbourR))))
                i += 1
                    #                                   State(     node, prev           ,      gValue          ,            fValue                 )
                    # Check if neighbourR exist, if not: create a State object
                    # Dict of objects of Class State, if key (puzzle) is not found
                    # create and add State object, otherwise leave the old State object


            #for neighbour in get_moves(9, node):
            for neighbour in neighboursList:
                if (time.time() > endTime):
                    break
                neighbourObject = allNodesDict.get(str(neighbour))
                gValueTemp = nodeObject.gValue + 1
                if gValueTemp <= neighbourObject.gValue:
                    neighbourObject.previous = nodeObject
                    neighbourObject.gValue = gValueTemp
                    neighbourObject.fValue = gValueTemp + heur(neighbour)
                    if neighbourObject not in openList:
                        openList.append(neighbourObject)
        #return 0

  if not noSolution:
    noSolution.append(["No solution"])
    return noSolution

# State(node, previous, gValue, fValue)




##### A* H2 *****
def astar2(puzzleObject, goal):
  noSolution = []

  endTime = time.time() + 60  #TIMER
  while time.time() < endTime:  # timer
        '''do whatever you do'''

        openList = []
        openList.append(puzzleObject)

        allNodesDict = {}
        allNodesDict[puzzleObject.node] = puzzleObject


        searchList.append(puzzleObject.node)

        #initialize dictionary for tracking previous node
        #prevDict = {} #dict()
        #prevDict[0] = -1 #start node with no previous node

        #initialize dictionary for tracking g values [float('inf')]
        #gValue = {}
        #gValue[0] = 0

        # initialize dictionary for tracking g values [float('inf')]
        fValueDict = {}
        #fValue[0] = heur(puzzle)
        fValueDict[puzzleObject] = puzzleObject.fValue
        #0:puzzle1.fValue

        #{puzzle1 : puzzle1.fValue}

        #puzzle1 ([], [pre], )
        #puzzle2
        #puzzle3

        #if puzzle not in openList:
        #    del fValueDict[puzzle]
        #elif puzzle in openList:
        #    fValueDict.setdefault(puzzle, puzzle.fValue)
        #    #if puzzle not in fValueDict: #if not(fValueDict.has_key(puzzle)):
        #    #    fValueDict[puzzle] = puzzle.fValue

        #if dict[key][]

        cv = 0

        while openList:
            # we might just create the fValue Dict in here so it destroys it upon exit (loop scope)
            fValueDict.clear() #clear and repopulate every iteration of while loop to keep updated
            for nodesObject in openList:
                fValueDict.setdefault(nodesObject, nodesObject.fValue) # CHANGE TO ADD OR APPEND OR WHATEVER IF PROBLEMS OCCUR

            #Find the smallest fValue in fValueDict and return its corresponding puzzle object (used as a key)
            nodeObject = min(fValueDict, key = lambda k : fValueDict[k])

            searchList.append(nodeObject.node)


            if nodeObject.nodeList == goal:
                return buildPath(nodeObject, allNodesDict)
                #return buildPath(allNodesDict.get(str(nodeObject.previous)), allNodesDict)
            if (time.time() > endTime):
                break
            openList.remove(nodeObject)

            # List of nodes only, not objects of Class State
            neighboursList = []

            i = 1

            while i < 10:
                if (time.time() > endTime):
                    break
                neighboursList.extend(get_moves(i, nodeObject.nodeList))
                for neighbourR in get_moves(i, nodeObject.nodeList):

                    if (time.time() > endTime):
                        break

                    allNodesDict.setdefault(str(neighbourR), State(neighbourR, nodeObject.nodeList, (nodeObject.gValue + 1), (nodeObject.gValue + 1 + heur2(neighbourR))))
                i += 1
                    #                                   State(     node, prev           ,      gValue          ,            fValue                 )
                    # Check if neighbourR exist, if not: create a State object
                    # Dict of objects of Class State, if key (puzzle) is not found
                    # create and add State object, otherwise leave the old State object


            #for neighbour in get_moves(9, node):
            for neighbour in neighboursList:
                if (time.time() > endTime):
                    break
                neighbourObject = allNodesDict.get(str(neighbour))
                gValueTemp = nodeObject.gValue + 1
                if gValueTemp <= neighbourObject.gValue:
                    neighbourObject.previous = nodeObject
                    neighbourObject.gValue = gValueTemp
                    neighbourObject.fValue = gValueTemp + heur2(neighbour)
                    if neighbourObject not in openList:
                        openList.append(neighbourObject)
        #return 0

  if not noSolution:
    noSolution.append(["No solution"])
    return noSolution





###############################################################################################
#Adapted from https://github.com/memoodm/AI-8Puzzle-SearchAlgorithm/blob/749b8481b57f82fc6dbbf598920e1a534825eee5/driver.py

def heur(puzzle):
    # Heuristic: distance to root numbers
    values_1 = [0, 1, 2, 1, 2, 3, 2, 3, 4]
    values_2 = [1, 0, 1, 2, 1, 2, 3, 2, 3]
    values_3 = [2, 1, 0, 3, 2, 1, 4, 3, 2]
    values_4 = [1, 2, 3, 0, 1, 2, 1, 2, 3]
    values_5 = [2, 1, 2, 1, 0, 1, 2, 1, 2]
    values_6 = [3, 2, 1, 2, 1, 0, 3, 2, 1]
    values_7 = [2, 3, 4, 1, 2, 3, 0, 1, 2]
    values_8 = [3, 2, 3, 2, 1, 2, 1, 0, 1]
    values_9 = [4, 3, 2, 3, 2, 1, 2, 1, 0]

    flatPuzzle = []
    for l in puzzle:
        flatPuzzle.extend(l)

    #global values_0, values_1, values_2, values_3, values_4, values_5, values_6, values_7, values_8
    v1 = values_1[flatPuzzle.index(1)]
    v2 = values_2[flatPuzzle.index(2)]
    v3 = values_3[flatPuzzle.index(3)]
    v4 = values_4[flatPuzzle.index(4)]
    v5 = values_5[flatPuzzle.index(5)]
    v6 = values_6[flatPuzzle.index(6)]
    v7 = values_7[flatPuzzle.index(7)]
    v8 = values_8[flatPuzzle.index(8)]
    v9 = values_9[flatPuzzle.index(9)]

    valorTotal = v1 + v2 + v3 + v4 + v5 + v6 + v7 + v8 + v9

    return valorTotal

###############################################################################################

def heur2(puzzle):
    # How many numbers are misplaced
    values_1 = [0, 0.5, 2, 0.5, 2, 4.5, 2, 4.5, 8]
    values_2 = [0.5, 0, 0.5, 2, 0.5, 2, 4.5, 2, 4.5]
    values_3 = [2, 0.5, 0, 4.5, 2, 0.5, 8, 4.5, 2]
    values_4 = [0.5, 2, 4.5, 0, 0.5, 2, 0.5, 2, 4.5]
    values_5 = [2, 0.5, 2, 0.5, 0, 0.5, 2, 0.5, 2]
    values_6 = [4.5, 2, 0.5, 2, 0.5, 0, 4.5, 2, 0.5]
    values_7 = [2, 4.5, 8, 0.5, 2, 4.5, 0, 0.5, 2]
    values_8 = [4.5, 2, 4.5, 2, 0.5, 2, 0.5, 0, 0.5]
    values_9 = [8, 4.5, 2, 4.5, 2, 0.5, 2, 0.5, 0]

    # #swaps - weight
    # 4 - 2
    # 3 - 1.5
    # 2 - 1
    # 1 - 0.5

    flatPuzzle = []
    for l in puzzle:
        flatPuzzle.extend(l)

    #global values_0, values_1, values_2, values_3, values_4, values_5, values_6, values_7, values_8
    v1 = values_1[flatPuzzle.index(1)]
    v2 = values_2[flatPuzzle.index(2)]
    v3 = values_3[flatPuzzle.index(3)]
    v4 = values_4[flatPuzzle.index(4)]
    v5 = values_5[flatPuzzle.index(5)]
    v6 = values_6[flatPuzzle.index(6)]
    v7 = values_7[flatPuzzle.index(7)]
    v8 = values_8[flatPuzzle.index(8)]
    v9 = values_9[flatPuzzle.index(9)]

    valorTotal = v1 + v2 + v3 + v4 + v5 + v6 + v7 + v8 + v9

    return valorTotal

###############################################################################################

def buildPath(puzzleObject, allNodesDict):
    solutionPath = []
    solutionPath.append(puzzleObject.nodeList)
    while puzzleObject.previous:
        puzzleObject = allNodesDict.get(str(puzzleObject.previous.nodeList))
        solutionPath.append(puzzleObject.nodeList)
    # We might need to prepend the start node if the while loop doesn't already take care of that
    # We might need to reverse the order of the output list
    return solutionPath

###############################################################################################
#
# puzzle = [[1,2,3],
#               [4,5,6],
#               [7,9,8]]
#
# a_file = open("input.txt")
# lines_to_read = [0]
# a=[]
# for position, line in enumerate(a_file):
#
#     if position in lines_to_read:
#         a= [int(s) for s in line.split(',')]
#
# k=0
# #print(a)
# for i, item  in enumerate(puzzle):
#     for j , pos in enumerate(item):
#         item[j] = a[k]
#         k+=1
#
#
#  #print(puzzle)
#
#
#
#
# total_time = 0
# t0 = time.time()
#
# # DO IDFS ON PUZZLE
#
# solution = id_dfs(puzzle, finalPuzzle)
#
# t1 = time.time()
# total_time += t1 - t0
# print('Puzzle solved using iterative deepening search in', total_time, 'seconds.')
# file = open("IDDFS_SOLUTION.txt", "w")
# file.write("------SOLUTION PATH-------" + "\n")
# for item in solution[0][0]:
#     file.write(str(item) + "\n")
# file.write(str(len(solution[0][0])))
# file.close()
#
# file = open("IDDFS_SEARCH.txt", "w")
#
# file.write("------SEARCH PATH-------" + "\n")
# for item in searchPath:
#     file.write(str(item) + "\n")
# file.write(str(len(searchPath)) + "\n")
#
# file.close()
#
# ###############################################################################################
# #### A*
#
# total_time = 0
# t0 = time.time()
#
# start = State(puzzle, 0, 0, heur(puzzle))
#
# solution = astar(start, finalPuzzle)
#
# t1 = time.time()
# total_time += t1 - t0
# print('Puzzle solved using A* search in', total_time, 'seconds.')
# file = open("Astar_SOLUTION_H1.txt", "w")
# file.write("------SOLUTION PATH-------" + "\n")
# for item in solution:
#     file.write(str(item) + "\n")
# file.write(str(len(solution)) + "\n" + "\n")
#
# file.close()
#
# file = open("Astar_SEARCH_H1.txt", "w")
#
# file.write("------SEARCH PATH-------" + "\n")
# for item in searchList:
#     file.write(str(item) + "\n")
# file.write(str(len(searchList)) + "\n")
#
# file.close()
#
# ##############################################################################################
# #### DFS
# total_time = 0
# t0 = time.time()
#
# #DO DFS ON PUZZLE
# solution = dfs(puzzle, finalPuzzle)
#
# t1 = time.time()
# total_time += t1 - t0
# print('Puzzle solved using depth first search in: ', total_time, 'seconds.')
# file = open("DFS_SOLUTION.txt", "w")
# file.write("------SOLUTION PATH-------"+"\n")
# for item in solution:
#     file.write(str(item) + "\n")
# file.write(str(len(solution)))
# file.close()
#
# file = open("DFS_SEARCH.txt", "w")
#
# file.write("------SEARCH PATH-------" + "\n")
# for item in searchPath:
#     file.write(str(item) + "\n")
# file.write(str(len(searchPath)) + "\n")
#
# file.close()
#
# ##############################################################################################
# print("Done")
# searchPath.clear()
# solutionPath.clear()
# searchList.clear()

##########################################################################




##################################
#ANALITYC

searchAlgo = ["IDFS","A*H1",'A*H2', "DFS"]
searchData = {
    #AVG sol, Total sol, AVG sea, total sea, avg no sol, total no sol , avg ex time, total ext time, avg cost, total cost
searchAlgo[0]: [0,0,0,0,0,0,0,0,0,0],
searchAlgo[1]: [0,0,0,0,0,0,0,0,0,0],
searchAlgo[2]: [0,0,0,0,0,0,0,0,0,0],
searchAlgo[3]: [0,0,0,0,0,0,0,0,0,0]
}

iteration = 0
while True:
    if iteration > 4:
     break
    print(iteration)
    puzzle = [[1,2,3],
              [4,5,6],
              [7,9,8]]

    a_file = open("input.txt")
    lines_to_read = [iteration]
    a=[]
    for position, line in enumerate(a_file):

        if position in lines_to_read:
            a= [int(s) for s in line.split(',')]

    k=0
    #print(a)
    for i, item  in enumerate(puzzle):
        for j , pos in enumerate(item):
            item[j] = a[k]
            k+=1


    #print(puzzle)
    print("IDFS")
    total_time = 0
    t0 = time.time()

    # DO DFS ON PUZZLE
    solution = id_dfs(puzzle, finalPuzzle)

    t1 = time.time()
    total_time += t1 - t0
    print('Puzzle solved using iterative deepening search in', total_time, 'seconds.')
    # AVG sol, Total sol, AVG sea, total sea, avg no sol, total no sol , avg ex time, total ext time, avg cost, total cost
    if(solution[0][0] != "No solution"):
        searchData["IDFS"][0] = (searchData["IDFS"][0]*20 + (len(solution[0][0])-1))/20 #AVG sol
        searchData["IDFS"][1] = searchData["IDFS"][1] + (len(solution[0][0])-1)  # total sol
        searchData["IDFS"][2] = (searchData["IDFS"][2]*20 + (len(searchPath)-1))/20 # avg search
        searchData["IDFS"][3] = searchData["IDFS"][3] + (len(searchPath)-1)  # total sea
        searchData["IDFS"][6] = (searchData["IDFS"][6]*20 + total_time) / 20  # avg exec time
        searchData["IDFS"][7] = searchData["IDFS"][7] + total_time  # total exec tiem
        searchData["IDFS"][8] = (searchData["IDFS"][8]*20 + (len(solution[0][0])-1)) / 20  # avg cost
        searchData["IDFS"][9] = searchData["IDFS"][9] + (len(solution[0][0])-1)  # total cost
    if(solution[0][0] == "No solution"):
        searchData["IDFS"][4] = (searchData["IDFS"][4]*20 + 1)/20    #AVG no solution
        searchData["IDFS"][5] = searchData["IDFS"][5] + 1 #Total no sol
        searchData["IDFS"][6] = (searchData["IDFS"][6]*20 + 60) / 20  # avg exec time
        searchData["IDFS"][7] = searchData["IDFS"][7] + 60  # total exec tiem



    print(searchData["IDFS"][7])

    file = open("IDDFS_SOLUTION.txt", "w")
    file.write("------SOLUTION PATH-------" + "\n")
    for item in solution[0][0]:
        file.write(str(item) + "\n")
    file.write(str(len(solution[0][0])))
    file.close()

    file = open("IDDFS_SEARCH.txt", "w")

    file.write("------SEARCH PATH-------" + "\n")
    for item in searchPath:
        file.write(str(item) + "\n")
    file.write(str(len(searchPath)) + "\n")

    file.close()

    ###############################################################################################
    print("A*")
    total_time = 0
    t0 = time.time()

    start = State(puzzle, 0, 0, heur(puzzle))

    solution = astar(start, finalPuzzle)

    t1 = time.time()
    total_time += t1 - t0
    print('Puzzle solved using A* H1 search in', total_time, 'seconds.')

    # AVG sol, Total sol, AVG sea, total sea, avg no sol, total no sol , avg ex time, total ext time, avg cost, total cost
    if(solution != "No solution"):
        searchData["A*H1"][0] = (searchData["A*H1"][0]*20 + (len(solution)-1))/20 #AVG sol
        searchData["A*H1"][1] = searchData["A*H1"][1] + (len(solution)-1)  # total sol
        searchData["A*H1"][2] = (searchData["A*H1"][2]*20 + (len(searchList)-1))/20 # avg search
        searchData["A*H1"][3] = searchData["A*H1"][3] + (len(searchList)-1)  # total sea
        searchData["A*H1"][6] = (searchData["A*H1"][6]*20 + total_time) / 20  # avg exec time
        searchData["A*H1"][7] = searchData["A*H1"][7] + total_time  # total exec tiem
        searchData["A*H1"][8] = (searchData["A*H1"][8]*20 + (len(solution)-1)) / 20  # avg cost
        searchData["A*H1"][9] = searchData["A*H1"][9] + (len(solution)-1)  # total cost
    if(solution == "No solution"):
        searchData["A*H1"][4] = (searchData["A*H1"][4]*20 + 1)/20    #AVG no solution
        searchData["A*H1"][5] = searchData["A*H1"][5] + 1 #Total no sol
        searchData["A*H1"][6] = (searchData["A*H1"][6]*20 + 60) / 20  # avg exec time
        searchData["A*H1"][7] = searchData["A*H1"][7] + 60  # total exec tiem


    file = open("Astar_SOLUTION_H1.txt", "w")
    file.write("------SOLUTION PATH-------" + "\n")
    for item in solution:
        file.write(str(item) + "\n")
    file.write(str(len(solution)) + "\n" + "\n")

    # file.write("------SEARCH PATH-------" + "\n")
    # for item in searchList:
    #     file.write(str(item) + "\n")
    # file.write(str(len(searchList)))

    file.close()

    file = open("Astar_SEARCH_H1.txt", "w")

    file.write("------SEARCH PATH-------" + "\n")
    for item in searchList:
        file.write(str(item) + "\n")
    file.write(str(len(searchList)) + "\n")

    file.close()

    searchPath.clear()
    solutionPath.clear()
    searchList.clear()
    ###############################################################################################

    ##### A* H2
    print("A* h2")
    total_time = 0
    t0 = time.time()

    start = State(puzzle, 0, 0, heur2(puzzle))

    solution = astar2(start, finalPuzzle)

    t1 = time.time()
    total_time += t1 - t0
    print('Puzzle solved using A* H2 search in', total_time, 'seconds.')

    # AVG sol, Total sol, AVG sea, total sea, avg no sol, total no sol , avg ex time, total ext time, avg cost, total cost
    if (solution != "No solution"):
        searchData["A*H2"][0] = (searchData["A*H2"][0] * 20 + (len(solution) - 1)) / 20  # AVG sol
        searchData["A*H2"][1] = searchData["A*H2"][1] + (len(solution) - 1)  # total sol
        searchData["A*H2"][2] = (searchData["A*H2"][2] * 20 + (len(searchList) - 1)) / 20  # avg search
        searchData["A*H2"][3] = searchData["A*H2"][3] + (len(searchList) - 1)  # total sea
        searchData["A*H2"][6] = (searchData["A*H2"][6] * 20 + total_time) / 20  # avg exec time
        searchData["A*H2"][7] = searchData["A*H2"][7] + total_time  # total exec tiem
        searchData["A*H2"][8] = (searchData["A*H2"][8] * 20 + (len(solution) - 1)) / 20  # avg cost
        searchData["A*H2"][9] = searchData["A*H2"][9] + (len(solution) - 1)  # total cost
    if (solution == "No solution"):
        searchData["A*H2"][4] = (searchData["A*H2"][4] * 20 + 1) / 20  # AVG no solution
        searchData["A*H2"][5] = searchData["A*H2"][5] + 1  # Total no sol
        searchData["A*H2"][6] = (searchData["A*H2"][6] * 20 + 60) / 20  # avg exec time
        searchData["A*H2"][7] = searchData["A*H2"][7] + 60  # total exec tiem


    file = open("Astar_SOLUTION_H2.txt", "w")
    file.write("------SOLUTION PATH-------" + "\n")
    for item in solution:
        file.write(str(item) + "\n")
    file.write(str(len(solution)) + "\n" + "\n")

    # file.write("------SEARCH PATH-------" + "\n")
    # for item in searchList:
    #     file.write(str(item) + "\n")
    # file.write(str(len(searchList)))

    file.close()

    file = open("Astar_SEARCH_H2.txt", "w")

    file.write("------SEARCH PATH-------" + "\n")
    for item in searchList:
        file.write(str(item) + "\n")
    file.write(str(len(searchList)) + "\n")

    file.close()

    searchPath.clear()
    solutionPath.clear()
    searchList.clear()


    ###############################################################################################
    print("DFS")
    total_time = 0
    t0 = time.time()

    #DO DFS ON PUZZLE
    solution = dfs(puzzle, finalPuzzle)

    t1 = time.time()
    total_time += t1 - t0
    print('Puzzle solved using depth first search in', total_time, 'seconds.')

    # AVG sol, Total sol, AVG sea, total sea, avg no sol, total no sol , avg ex time, total ext time, avg cost, total cost
    if(solution[0][0][0]!= "No solution"):
        searchData["DFS"][0] = (searchData["DFS"][0]*20 + (len(solution[0][0])-1))/20 #AVG sol
        searchData["DFS"][1] = searchData["DFS"][1] + (len(solution[0][0])-1)  # total sol
        searchData["DFS"][2] = (searchData["DFS"][2]*20 + (len(solution[0][0])-1))/20 # avg search
        searchData["DFS"][3] = searchData["DFS"][3] + (len(solution[0][0])-1)  # total sea
        searchData["DFS"][6] = (searchData["DFS"][6]*20 + total_time) / 20  # avg exec time
        searchData["DFS"][7] = searchData["DFS"][7] + total_time  # total exec tiem
        searchData["DFS"][8] = (searchData["DFS"][8]*20 + (len(solution[0][0])-1)) / 20  # avg cost
        searchData["DFS"][9] = searchData["DFS"][9] + (len(solution[0][0])-1)  # total cost
    if(solution[0][0][0] == "No solution"):
        searchData["DFS"][4] = (searchData["DFS"][4]*20 + 1)/20    #AVG no solution
        searchData["DFS"][5] = searchData["DFS"][5] + 1 #Total no sol
        searchData["DFS"][6] = (searchData["DFS"][6]*20 + 60) / 20  # avg exec time
        searchData["DFS"][7] = searchData["DFS"][7] + 60  # total exec tiem



    file = open("DFS_SOLUTION.txt", "w")
    file.write("------SOLUTION PATH-------"+"\n")
    for item in solution:
        file.write(str(item) + "\n")
    file.write(str(len(solution)))
    file.close()

    file = open("DFS_SEARCH.txt", "w")

    file.write("------SEARCH PATH-------" + "\n")
    for item in searchPath:
        file.write(str(item) + "\n")
    file.write(str(len(searchPath)) + "\n")

    file.close()
    print("Done")
    ###############################################################################################



    iteration += 1
print("avg sol, total sol, avg search, total search, avg no sol, total no sol , avg exe time, total exe time, avg cost, total cost")
print (searchData["IDFS"])
print (searchData["A*H1"])
print (searchData["A*H2"])
print (searchData["DFS"])
