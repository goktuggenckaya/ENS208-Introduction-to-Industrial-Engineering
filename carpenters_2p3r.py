# This example formulates and solves the carpenter's problem
#  maximize a xc + b xt
#  subject to
#          xc + 2 xt <= 50
#        2 xc +   xt <= 40
#          xc +   xt <= 28
#          xc, xt non-negative

from gurobipy import GRB, Model

# Create a new model
m = Model("carpenter")

# Create variables
xc = m.addVar(vtype=GRB.CONTINUOUS, name="xc")
xt = m.addVar(vtype=GRB.CONTINUOUS, name="xt")

# Add constraint
m.addConstr(xc + 2 * xt <= 50, "rawmat")

# Add constraint
m.addConstr(2 * xc + xt  <= 40, "workhour")

# Add constraint
m.addConstr(xc + xt  <= 28, "glue")

# Set objective
m.setObjective(10 * xc + 15 * xt, GRB.MAXIMIZE)

m.optimize()

for v in m.getVars():
    print(v.varName, v.x)

print('The optimal objective function value is', m.objVal)