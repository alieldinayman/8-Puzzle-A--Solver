tree = {'1,1': ' ',  # 1
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

empty = (0, 0)
trees = []
goalFound = False

class TreeChildren:

    def TreePrint(self, tree):
        for i in range(1, 4):
            for j in range(1, 4):
                print(tree[str(i) + ',' + str(j)] + ' ', end='')
                if j % 3 == 0:
                    print('\n', end='')
        #print('')

    def TreeScan(self, tree, one, two, three, four, five, six, seven, eight, nine):
        global empty
        scanned = [one, two, three, four, five, six, seven, eight, nine]
        count = 0
        for i in range(1, 4):
            for j in range(1, 4):
                tree[str(i) + ',' + str(j)] = scanned[count]
                count += 1
                if tree[str(i) + ',' + str(j)] == ' ':
                    empty = (i, j)
        self.FindChildren(tree)

    def FindChildren(self, tree):
        global empty
        print("\nChildren: \n")

        if empty[0] > 1:
            treeN = dict(tree)
            treeN[str(empty[0]) + ',' + str(empty[1])], treeN[str(empty[0]-1)+','+str(empty[1])] =\
                treeN[str(empty[0]-1)+','+str(empty[1])], treeN[str(empty[0]) + ',' + str(empty[1])]
            self.TreePrint(treeN)
            self.ComputeCost(treeN)
            trees.append(treeN)

        if empty[0] < 3:
            treeN = dict(tree)
            treeN[str(empty[0]) + ',' + str(empty[1])], treeN[str(empty[0]+1)+','+str(empty[1])] =\
                treeN[str(empty[0]+1)+','+str(empty[1])], treeN[str(empty[0]) + ',' + str(empty[1])]
            self.TreePrint(treeN)
            self.ComputeCost(treeN)
            trees.append(treeN)

        if empty[1] > 1:
            treeN = dict(tree)
            treeN[str(empty[0]) + ',' + str(empty[1]-1)], treeN[str(empty[0])+','+str(empty[1])] =\
                treeN[str(empty[0])+','+str(empty[1])], treeN[str(empty[0]) + ',' + str(empty[1]-1)]
            self.TreePrint(treeN)
            self.ComputeCost(treeN)
            trees.append(treeN)

        if empty[1] < 3:
            treeN = dict(tree)
            treeN[str(empty[0]) + ',' + str(empty[1]+1)], treeN[str(empty[0])+','+str(empty[1])] =\
                treeN[str(empty[0])+','+str(empty[1])], treeN[str(empty[0]) + ',' + str(empty[1]+1)]
            self.TreePrint(treeN)
            self.ComputeCost(treeN)
            trees.append(treeN)

        print('')
        print(trees)

    def ComputeCost(self, tree):
        miscost, mancost = 0, 0
        for i in range(1, 4):
            for j in range(1, 4):
                if tree[str(i)+','+str(j)] != goal[str(i)+','+str(j)]:
                    miscost += 1
                    for x in range(1, 4):
                        for y in range(1, 4):
                            if goal[str(x)+','+str(y)] == tree[str(i) + ',' + str(j)]:
                                mancost += abs(x-i) + abs(y-j)
        print("Misplaced Tile Distance = " + str(miscost))
        print("Manhattan Distance = " + str(mancost) + "\n")

        if miscost == 0 and mancost == 0:
            print("GOAL FOUND!")
            goalFound = True
            
        #return miscost, mancost

    @staticmethod
    def ComputeCostStatic(tree):
        miscost, mancost = 0, 0
        for i in range(1, 4):
            for j in range(1, 4):
                if tree[str(i)+','+str(j)] != goal[str(i)+','+str(j)]:
                    miscost += 1
                    for x in range(1, 4):
                        for y in range(1, 4):
                            if goal[str(x)+','+str(y)] == tree[str(i) + ',' + str(j)]:
                                mancost += abs(x-i) + abs(y-j)
        print("Misplaced Tile Distance = " + str(miscost))
        print("Manhattan Distance = " + str(mancost) + "\n")

        if miscost == 0 and mancost == 0:
            print("GOAL FOUND!")
            goalFound = True
            
        return miscost, mancost


if __name__ == '__main__':
    print("Enter your tree values: ")
    Tree = TreeChildren()
    treeN = Tree.TreeScan(tree)
    print("Tree: \n")
    Tree.TreePrint(treeN)
    Tree.FindChildren(treeN)
    x = input()
    print(trees)
