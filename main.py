from src.Graph  import *
from src.Solver import *
from src.Parser import *

def testRandomGraphs():
    size = [10,20,30,40,50]
    nblocked = [10,20,30,40,50]
    solver = Solver() 
    for s,nb in zip(size,nblocked): 
        g = generateRandomGraph(s,s,nb)
        print(g)
        print(solver.writeOutput(solver.bfsSolver(g)))

        
#testRandomGraphs()
p = Parser()
initX, initY, endX, endY, width, length, initOrientation, listBlocked =p.parseFile("examples/ex1.txt")
g = Graph(initX, initY, endX, endY, width, length, initOrientation, listBlocked)
g.createGraph()
solver = Solver()
print(solver.writeOutput(solver.bfsSolver(g)))
