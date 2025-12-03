class Solver:
    def __init__(self):
        self.directionDict = {
            'nord':0,
            'ouest':1,
            'sud':2,
            'est':3
        }

    def bfsSolver(self,graph): # bfs algo in a not-weighted directed graph gives shortest path -> 
                               # O(V + E) = O(length*width)
        currX = graph.currX
        currY = graph.currY
        currOrientation = graph.currOrientation

        idx = (currX, currY, currOrientation)

        queue = [idx]
        visited = []
        bestPath = dict()
        finalOrientation = None
        while len(queue) > 0:
            node = queue.pop(0)
            if (node[0],node[1]) in graph.blockedList:
                raise Exception("Error: here")
            if (node[0], node[1]) == (graph.endx , graph.endy):
                finalOrientation = node[2]
                break
            if node in visited:
                continue
            visited.append(node)
            queue.extend(graph.Nodes[node].next)
            if node not in bestPath.keys():
                bestPath[node] = [node]
            for nd in graph.Nodes[node].next:
                id = (nd[0],nd[1],nd[2])
                if id not in bestPath.keys():
                    bestPath[id] = bestPath[node] + [nd]
        return bestPath[(graph.endx,graph.endy,finalOrientation)]

    def writeOutput(self, bestPath, filename=None):
        print(type(bestPath))
        outStr = f"{len(bestPath)-1} "
        for i in range(len(bestPath)):
            if i == len(bestPath) - 1:
                break
            currX, currY, currOrientation = bestPath[i]
            nextX, nextY, nextOrientation = bestPath[i+1]
            if currOrientation == nextOrientation:
                outStr += f'a{max(abs(currX - nextX),abs(currY - nextY))} '
            else: 
                if (self.directionDict[nextOrientation] - self.directionDict[currOrientation]) == 1: 
                    outStr += "G "
                else:
                    outStr += "D "
        outStr = outStr.strip()
        if filename is not None: 
            with open(filename,"+w") as f:
                f.write(outStr)
        else: 
            print(outStr)
        return outStr

