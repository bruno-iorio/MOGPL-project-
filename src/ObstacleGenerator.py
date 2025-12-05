import gurobipy as gp
from gurobipy import GRB
import random

model = gp.Model()
M = 10
N = 10
P = 12
weights = [[random.randint(0, 1000) for j in range(N)] for i in range(M)]

x = {}
for i in range(M):
    for j in range(N):
        x[i, j] = model.addVar(vtype=GRB.BINARY)

model.update()

model.setObjective(
    sum(weights[i][j] * x[i,j] for i in range(M) for j in range(N)),
    GRB.MINIMIZE
)

model.addConstr(sum(x[i,j] for i in range(M) for j in range(N)) == P)
for i in range(M):
    model.addConstr(
        gp.quicksum(x[i,j] for j in range(N)) <= 2*P // M
    )
for i in range(M):
    for j in range(N - 2):
        model.addConstr(
            x[i,j] + x[i,j+2] - x[i,j+1] <= 1
        )
# No 101 in columns
for j in range(N):
    for i in range(M - 2):
        model.addConstr(x[i,j] + x[i+2,j] - x[i+1,j] <= 1)

model.optimize()

# Get results
for i in range(M):
    for j in range(N):
        if x[i,j].X > 0.5:
            print(f"Obstacle at ({i}, {j})")


