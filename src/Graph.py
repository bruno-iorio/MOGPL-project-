n = 0 
left = 1 
down = 2 
right = 3

class Node:
    def __init__(self,x,y, orientation):
        self.x = x 
        self.y = y
        self.next = []
        self.orientation = orientation

class Graph:
    def __init__(self, initx, inity, endx, endy, width, length, initialOrientation, blockedList):
        if (initx < 0 or initx >= width):
            raise Exception("GraphCreationError: invalid initx value!")
        if (inity < 0 or inity >= length):
            raise Exception("GraphCreationError: invalid inity value!")
        if ((initx, inity) in blockedList):
            raise Exception("GraphCreationError: invalid initial position!")
        if (endx < 0 or endx>= width):
            raise Exception("GraphCreationError: invalid endx value!")
        if (endy < 0 or endy >= length):
            raise Exception("GraphCreationError: invalid endy value!")
        if ((endx, endy) in blockedList):
            raise Exception("GraphCreationError: invalid final position!")
        self.currX = initx
        self.currY = inity
        self.currOrientation = initialOrientation
        self.endx  = endx
        self.endy  = endy
        self.width = width
        self.length = length
        self.blockedList = blockedList
        self.Nodes = dict()

    def createGraph(self):
        for i in range(len(self.width)):
            for j in range(len(self.length)):
                if (i,j) not in self.blockedList:
                    for dir in ['sud','nord','est','ouest']:
                        self.Nodes[(i,j,dir)] = Node(i,j,dir)
        for idx in list(self.Nodes.keys()):
            self.addNeighbors(idx)
    
    def addNeighbors(self,idx):
        x, y, dir = idx
        if dir == "nord":
            for k in range(1,4):
                if y - k >= 0 and (x, y-k) not in self.blockedList: 
                    self.Nodes[idx].next.append((x,y-k,dir))
            self.Nodes[idx]next.extend([(x,y,'est'), (x,y,'ouest')])
        if dir == "est":
            for k in range(1,4):
                if x + k <= self.width - 1 and (x+k, y) not in self.blockedList:
                    self.Nodes[idx].next.append((x+k,y,dir))
            self.Nodes[idx]next.extend([(x,y,'nord'), (x,y,'sud')])
        if dir == "sud":
            for k in range(1,4):
                if y+k <= self.length and (x, y+k) not in self.blockedList:
                    self.Nodes[idx].next.append((x,y+k,dir))
            self.Nodes[idx]next.extend([(x,y,'ouest'), (x,y,'est')])
        if dir == "ouest":
            for k in range(1,4):
                if x - k >= 0 and (x-k, y) not in self.blockedList:
                    self.Nodes[idx].next.append((x-k,y,dir)) 
            self.Nodes[idx]next.extend([(x,y,'nord'), (x,y,'sud')])

    def printGraph(self):
        pass



