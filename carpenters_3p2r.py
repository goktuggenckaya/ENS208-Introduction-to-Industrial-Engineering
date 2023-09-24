# This example formulates and solves the carpenter's problem
#  maximize a xc + b xt + c xs
#  subject to
#          xc + 2 xt + 0.5 xs<= 50
#        2 xc +   xt + 0.5 xs<= 40
#          xc, xt, xs non-negative

from gurobipy import GRB, Model

# Create a new model
m = Model("carpenter")

# Create variables
xc = m.addVar(vtype=GRB.CONTINUOUS, name="xc")
xt = m.addVar(vtype=GRB.CONTINUOUS, name="xt")
xs = m.addVar(vtype=GRB.CONTINUOUS, name="xs")

# Add constraint
m.addConstr(xc + 2 * xt + 0.5 * xs<= 50, "rawmat")

# Add constraint
m.addConstr(2 * xc + xt + 0.5 * xs <= 40, "workhour")

# Set objective
m.setObjective(10 * xc + 15 * xt + 5 * xs, GRB.MAXIMIZE)

m.optimize()

for v in m.getVars():
    print(v.varName, v.x)

print('The optimal objective function value is', m.objVal)