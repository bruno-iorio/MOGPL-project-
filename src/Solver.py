class Solver:
    def __init__(self):
        self.directionDict = {
            'nord':0,
            'ouest':1,
            'sud':2,
            'est':3
        }

    def bfsSolver(self,graph): # bfs algo in a not-weighted directed graph gives shortest path
        currX = graph.currX 
        currY = graph.currY
        currOrientation = graph.currOrientation

        idx = (currX, currY, currOrientation)

        queue = [graph.Nodes[idx]]
        visited = []
        bestPath = dict()
        finalOrientation = None
        while len(queue) > 0: 
            node = queue.pop()
            if (node.x, node.y) == (graph.endX , graph.endY):
                id = (node.x,node.y,node.orientation)
                bestPath[id].append(id)
                finalOrientation = node.orientation
                break
            if node in visited:
                continue
            else:
                visited.append(node)
            queue.extend(node.next)
            for nd in node.next:
                id = (nd.x,nd.y,nd.orientation)
                if id not in bestPath:
                    bestPath[id] = []
                bestPath[id].append((node.x, node.y, node.orientation))
        return bestPath[(graph.endX,graph.endY,finalOrientation)]

    def writeOutput(bestPath, graph,filename=None):
        outStr = f"{len(bestPath)-1} "
        for i in range(len(bestPath)):
            if i == len(bestPath) - 1:
                break
            currX, currY, currOrientation = bestPath[i]
            nextX, nextY nextOrientation = bestPath[i+1]
            if currOrientation == nextOrientation:
                outStr += f'a{max(abs(currX - nextX),abs(currY - nextY)} '
            else: 
                if (directionDict[nextOrientation] - directionDict[currOrientation]) > 0: 
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

