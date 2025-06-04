from instances import *
from environments import *
from solvers import *
from solutions import *

instance_name = 'dummy_problem'

inst = Instance(instance_name)
env = Environment(inst)
solver = solver_327795_327796(env)

X, Y = solver.solve()

sol = Solution(X, Y)
sol.write(instance_name)
