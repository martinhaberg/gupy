from gurobipy import *

model = read("afiro.mps")

model.optimize()

model.Objval

model.printAttr('X')