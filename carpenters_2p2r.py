# This example formulates and solves the carpenter's problem
#  maximize a xc + b xt
#  subject to
#          xc + 2 xt <= 50
#        2 xc +   xt <= 40
#          xc, xt non-negative

from gurobipy import GRB, Model

# Create a new model
m = Model("refinery")

# Create variables
x1 = m.addVar(vtype=GRB.CONTINUOUS, name="refinery 1")
x2 = m.addVar(vtype=GRB.CONTINUOUS, name="refinery 2")

# Add constraint


# Add constraint
m.addConstr(x1 - 3*x2 <= 0, "high grade oil")
m.addConstr(2*x1 + 6*x2   <= 320, "medium grade oil")
m.addConstr(4*x1 + 1.25*x2  <= 180, "low grade oil")
m.addConstr(x1 >= 10, "4")

# m.addConstr(x1 + x2 + x3  <= 5, "liters")

# Set objective
m.setObjective( 18* x1 + 9 * x2, GRB.MAXIMIZE)

m.optimize()

for v in m.getVars():
    print(v.varName, v.x)

print('The optimal objective function value is', m.objVal)
