node = {'1,1': ' ',  # 1
        '1,2': ' ',  # 2
        '1,3': ' ',  # 3
        '2,1': ' ',  # 8
        '2,2': ' ',  # NULL
        '2,3': ' ',  # 4
        '3,1': ' ',  # 7
        '3,2': ' ',  # 6
        '3,3': ' '}  # 5

goal = {'1,1': ' ',  # 1
        '1,2': ' ',  # 2
        '1,3': ' ',  # 3
        '2,1': ' ',  # 8
        '2,2': ' ',  # NULL
        '2,3': ' ',  # 4
        '3,1': ' ',  # 7
        '3,2': ' ',  # 6
        '3,3': ' '}  # 5

import time

nodes = [] #PRIORITY QUEUE: TAKES TUPLES OF (GRID, DEPTH, SCORE, NODEID, PARENTID)
visited = [] #VISITED NODES: TAKES TUPLES OF NODES THAT HAVE BEEN TRAVERSED FROM THE QUEUE

goalFound = False
nodeID = 0 #UNIQUE IDs FOR EACH NODE IN THE MST

class NodeChildren:

    def NodePrint(self, nodeID):
        #LOCATE THE NODE IN QUEUE OR IN VISITED
        node = []
        for i in range(len(visited)):
            if visited[i][3] == nodeID: #IF IT CURRENTLY EXISTS IN VISITED
                node = visited[i]
                
        if node == []: #STILL EMPTY (DIDN'T FIND IT IN VISITED)
            for i in range(len(nodes)):
                if nodes[i][3] == nodeID: #IF IT CURRENTLY EXISTS IN QUEUE (NODES)
                    node = nodes[i]
                
        for i in range(1, 4):
            for j in range(1, 4):
                print(node[0][str(i) + ',' + str(j)] + ' ', end='')
                if j % 3 == 0:
                    print('\n', end='')
                    
        print("Manhattan Distance = " + str(node[2]-node[1]) + "\n----------------------------") #MANHATTAN DIST. = SCORE - DEPTH
        #print("Misplaced Tile Distance + Depth = " + str(miscost))

    def RootScan(self, goal):
        global nodeID
        for i in range(1, 4):
            for j in range(1, 4):
                node[str(i) + ',' + str(j)] = input()
        print('')
        mancost, miscost = self.ComputeCost(node, 0, goal)
        nodes.append((node, 0, mancost, nodeID, None))
        nodeID += 1
        return node

    def GoalScan(self):
        for i in range(1, 4):
            for j in range(1, 4):
                goal[str(i) + ',' + str(j)] = input()
        return goal

    def ComputeCost(self, node, depth, goal):
        global goalFound
        miscost, mancost = 0, 0
        for i in range(1, 4):
            for j in range(1, 4):
                if node[str(i)+','+str(j)] != goal[str(i)+','+str(j)]:
                    miscost += 1
                    if  node[str(i)+','+str(j)] != ' ':
                        for x in range(1, 4):
                            for y in range(1, 4):
                                if goal[str(x)+','+str(y)] == node[str(i) + ',' + str(j)]:
                                    mancost += abs(x-i) + abs(y-j)
                                    break

        if miscost == 0 and mancost == 0:
            goalFound = True
            
        return (mancost + depth), (miscost + depth)

    def FindNewMin(self):
        nodes.sort(key=lambda x:x[2])
        return nodes[0]

    def CheckVisited(self, grid):
        for i in range(len(visited)):
            if visited[i][0] == grid:
                #print(grid)
                #print("was visited before\n")
                return True
        return False

    def ProcessChild(self, grid, currDepth, parentID):
        if self.CheckVisited(grid) is False:
            global nodeID
            mancost, miscost = self.ComputeCost(grid, currDepth+1, goal)
            nodes.append((grid, currDepth+1, mancost, nodeID, parentID)) #STITCH A NEW CHILD
            nodeID += 1

    def FindChildren(self, parent, goal):
        #DEFINING DEPTH
        parent = nodes[0]
        currDepth = parent[1]
        parentID = parent[3]

        #REMOVING PARENT AND ADDING TO VISITED
        if parent in nodes:
            visited.append(parent)
            nodes.remove(parent)
        
        #FINDING EMPTY
        for i in range(1, 4):
            for j in range(1, 4):
                if parent[0][str(i) + ',' + str(j)] == ' ':
                    empty = (i, j)
                
        if empty[1] > 1: #UP
            #MAKE A NEW GRID
            grid = dict(parent[0])
            grid[str(empty[0]) + ',' + str(empty[1]-1)], grid[str(empty[0])+','+str(empty[1])] =\
                grid[str(empty[0])+','+str(empty[1])], grid[str(empty[0]) + ',' + str(empty[1]-1)]
            #CHECK IF GRID WAS VISITED BEFORE AND MAKE A CHILD OF IT IF NOT
            self.ProcessChild(grid, currDepth, parentID)
            
        if empty[1] < 3: #DOWN
            grid = dict(parent[0])
            grid[str(empty[0]) + ',' + str(empty[1]+1)], grid[str(empty[0])+','+str(empty[1])] =\
                grid[str(empty[0])+','+str(empty[1])], grid[str(empty[0]) + ',' + str(empty[1]+1)]
            self.ProcessChild(grid, currDepth, parentID)

        if empty[0] < 3: #RIGHT
            grid = dict(parent[0])
            grid[str(empty[0]) + ',' + str(empty[1])], grid[str(empty[0]+1)+','+str(empty[1])] =\
                grid[str(empty[0]+1)+','+str(empty[1])], grid[str(empty[0]) + ',' + str(empty[1])]
            self.ProcessChild(grid, currDepth, parentID)
                
        if empty[0] > 1: #LEFT
            grid = dict(parent[0])
            grid[str(empty[0]) + ',' + str(empty[1])], grid[str(empty[0]-1)+','+str(empty[1])] =\
                grid[str(empty[0]-1)+','+str(empty[1])], grid[str(empty[0]) + ',' + str(empty[1])]
            self.ProcessChild(grid, currDepth, parentID)

    def FindParent(self, child, path):
        for i in range(len(visited)):
            if child[4] == visited[i][3]: #IF THE CHILD'S PARENT ID IS THE PARENT'S ID
                path.append(visited[i]) #APPEND THE PARENT IN THE PATH

    
if __name__ == '__main__':
    #INITILAZING THE ROOT NODE
    Node = NodeChildren()
    print("Enter your goal node values, each in a line: ")
    goal = Node.GoalScan()
    print("Enter your root node values, each in a line: ")
    node = Node.RootScan(goal)
    node = Node.FindNewMin()
    Node.FindChildren(node, goal )
    
    # ----BEGIN ITERATING---- #
    iterations = 0
    tick = time.time()
    while goalFound is False:
        if iterations >= 1000:
            print("Tree is unsolvable.")
            exit(0)
        node = Node.FindNewMin() #SORT THE QUEUE TO GET THE MINIMUM ON TOP
        Node.FindChildren(node, goal)
        iterations+=1
    tock = time.time()
    goal = Node.FindNewMin() #OBTAIN THE GOAL NODE IF FOUND

    #MAKE THE PATH FROM ROOT TO GOAL
    path = [goal]
    for i in range(goal[1]): #THE DEPTH OF THE GOAL (THE LENGTH OF THE PATH)
        Node.FindParent(path[i], path)
    print("Root Node: \n----------")
    for node in reversed(path):
        Node.NodePrint(node[3])
    print("Moves to reach the Goal Node: " + str(goal[1])+
          "\nNumber of Traversed Nodes: " + str(len(visited))+
          "\nTime elapsed by the algorithm: " + str(format(tock-tick, '0.3f')) + "s")
    
