node = {'1,1': ' ',  # 1
        '1,2': ' ',  # 2
        '1,3': ' ',  # 3
        '2,1': ' ',  # 8
        '2,2': ' ',  # NULL
        '2,3': ' ',  # 4
        '3,1': ' ',  # 7
        '3,2': ' ',  # 6
        '3,3': ' '}  # 5

goal = {'1,1': '1',  # 1
        '1,2': '2',  # 2
        '1,3': '3',  # 3
        '2,1': '8',  # 8
        '2,2': ' ',  # NULL
        '2,3': '4',  # 4
        '3,1': '7',  # 7
        '3,2': '6',  # 6
        '3,3': '5'}  # 5

nodes = [] #TAKES TUPLES OF (NODE, DEPTH, SCORE)
visited = [] #TAKES NODES

goalFound = False

class NodeChildren:

    def NodePrint(self, index):
        for i in range(1, 4):
            for j in range(1, 4):
                print(nodes[index][0][str(i) + ',' + str(j)] + ' ', end='')
                if j % 3 == 0:
                    print('\n', end='')
        print("Manhattan Distance = " + str(nodes[index][2]-nodes[index][1]))
        #print("Misplaced Tile Distance + Depth = " + str(miscost))

    def RootScan(self):
        for i in range(1, 4):
            for j in range(1, 4):
                node[str(i) + ',' + str(j)] = input()
        print('')
        print("Root Node: \n")
        mancost, miscost = self.ComputeCost(node, 0)
        nodes.append((node, 0, mancost))
        return node

    def ComputeCost(self, node, depth):
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

    def CheckVisited(self, node):
        for i in range(len(visited)):
            if visited[i] == node:
                #print(node)
                #print("was visited before\n")
                return True
        return False

    def ProcessChild(self, child, currDepth):
        if self.CheckVisited(child) is False:
            mancost, miscost = self.ComputeCost(child, currDepth+1)
            nodes.append((child, currDepth+1, mancost))
            self.NodePrint(nodes.index((child, currDepth+1, mancost)))

    def FindChildren(self, parent):
        #DEFINING DEPTH
        parent = nodes[0]
        currDepth = parent[1]

        #REMOVING PARENT AND ADDING TO VISISTED
        if parent in nodes:
            visited.append(parent[0])
            nodes.remove(parent)
        
        #FINDING EMPTY
        for i in range(1, 4):
            for j in range(1, 4):
                if parent[0][str(i) + ',' + str(j)] == ' ':
                    empty = (i, j)
        
        print("----------------------------------------------------------")         
        print("Eligible Unvisisted Children: ")
        print("----------------------------------------------------------")
        
        if empty[1] > 1: #UP
            #MAKE A NEW CHILD
            child = dict(parent[0])
            child[str(empty[0]) + ',' + str(empty[1]-1)], child[str(empty[0])+','+str(empty[1])] =\
                child[str(empty[0])+','+str(empty[1])], child[str(empty[0]) + ',' + str(empty[1]-1)]
            #CHECK IF CHILD WAS VISITED BEFORE
            self.ProcessChild(child, currDepth)
            
        if empty[1] < 3: #DOWN
            child = dict(parent[0])
            child[str(empty[0]) + ',' + str(empty[1]+1)], child[str(empty[0])+','+str(empty[1])] =\
                child[str(empty[0])+','+str(empty[1])], child[str(empty[0]) + ',' + str(empty[1]+1)]
            self.ProcessChild(child, currDepth)

        if empty[0] < 3: #RIGHT
            child = dict(parent[0])
            child[str(empty[0]) + ',' + str(empty[1])], child[str(empty[0]+1)+','+str(empty[1])] =\
                child[str(empty[0]+1)+','+str(empty[1])], child[str(empty[0]) + ',' + str(empty[1])]
            self.ProcessChild(child, currDepth)
                
        if empty[0] > 1: #LEFT
            child = dict(parent[0])
            child[str(empty[0]) + ',' + str(empty[1])], child[str(empty[0]-1)+','+str(empty[1])] =\
                child[str(empty[0]-1)+','+str(empty[1])], child[str(empty[0]) + ',' + str(empty[1])]
            self.ProcessChild(child, currDepth)

    
if __name__ == '__main__':
    #INITILAZING THE ROOT NODE
    Node = NodeChildren()
    print("Enter your root node values: ")
    node = Node.RootScan()
    Node.NodePrint(0)
    node = Node.FindNewMin()
    Node.FindChildren(node)
    print("----------------------------------------------------------")
    print("Nodes in Queue: ")
    print("----------------------------------------------------------")
    for node in nodes:
        print(node)
    print("\nNumber of Trees: " + str(len(nodes)) + "\n")
    
    #   ----BEGIN ITERATING---- #
    i = 0
    while goalFound is False:
        #x = input() #FOR DEBUGGING
        i+=1
        print("----------------------------------------------------------------------")
        print("                             Iteration: " + str(i))
        print("----------------------------------------------------------------------")
        print('')
        print("New Minimum Tree: \n")
        node = Node.FindNewMin()
        Node.NodePrint(0)
        Node.FindChildren(node)
        node = Node.FindNewMin() #SORT AGAIN AFTER FINDING CHILDREN
        print('')
        print("----------------------------------------------------------")
        print("Nodes in Queue: ")
        print("----------------------------------------------------------")
       # for node in nodes: #FOR DEBUGGING
       #     print(node)
        print("\nNumber of Nodes: " + str(len(nodes)) + "\n")
    print("----------------------------------------------------------")
    print("Goal Node Found: ")
    print("----------------------------------------------------------")
    node = Node.FindNewMin()
    Node.NodePrint(0)
    print("\nNumber of Visited Nodes: " + str(len(visited)))
    
