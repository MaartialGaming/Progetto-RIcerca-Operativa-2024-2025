from .abstract_solver import AbstractSolver
import numpy as np
import gurobipy as gp
from gurobipy import GRB


# noinspection PyPep8Naming
class solver_327795_327796(AbstractSolver):
    def __init__(self, env):
        super().__init__(env)
        self.name = 'solver_327795_327796'

    def solve(self):
        super().solve()

        weights = self.env.inst.weights
        service = self.env.inst.service
        distances = self.env.inst.distances

        num_warehouses = service.shape[0]
        num_supermarkets = service.shape[1]

        model = gp.Model("WarehousePlacement")

        # X[i] = 1 if warehouse i is built, 0 otherwise
        X = model.addVars(num_warehouses, vtype=GRB.BINARY, name="X")

        # Y[i,j] = 1 if the route goes from i to j, 0 otherwise
        Y = model.addVars(num_warehouses + 1, num_warehouses + 1, vtype=GRB.BINARY, name="Y")

        # S[i,k] = 1 if warehouse i serves supermarket k, 0 otherwise
        S = model.addVars(num_warehouses, num_supermarkets, vtype=GRB.BINARY, name="S")

        # Flow variables for MTZ subtour elimination
        u = model.addVars(num_warehouses + 1, vtype=GRB.CONTINUOUS, name="u")

        # Objective: minimize total cost
        construction_cost = weights['construction'] * gp.quicksum(X[i] for i in range(num_warehouses))

        missed_supermarket_cost = weights['missed_supermarket'] * gp.quicksum(
            (1 - gp.quicksum(S[i, k] for i in range(num_warehouses)))
            for k in range(num_supermarkets))

        travel_cost = weights['travel'] * gp.quicksum(
            distances[i, j] * Y[i, j]
            for i in range(num_warehouses + 1)
            for j in range(num_warehouses + 1))

        model.setObjective(construction_cost + missed_supermarket_cost + travel_cost, GRB.MINIMIZE)

        # Each supermarket must be served by at most one warehouse
        for k in range(num_supermarkets):
            model.addConstr(
                gp.quicksum(S[i, k] for i in range(num_warehouses)) <= 1,
                f"Supermarket_{k}_served_once")

        # A warehouse can only serve supermarkets if it's built
        for i in range(num_warehouses):
            for k in range(num_supermarkets):
                model.addConstr(
                    S[i, k] <= X[i],
                    f"Warehouse_{i}_serves_{k}_only_if_built")
                model.addConstr(
                    S[i, k] <= service[i, k],
                    f"Warehouse_{i}_can_only_serve_authorized_{k}")

        # Vehicle must leave and return to depot (node 0)
        model.addConstr(
            gp.quicksum(Y[0, j] for j in range(1, num_warehouses + 1)) == 1,
            "Leave_depot_once")
        model.addConstr(
            gp.quicksum(Y[i, 0] for i in range(1, num_warehouses + 1)) == 1,
            "Return_to_depot_once")

        for j in range(1, num_warehouses + 1):
            model.addConstr(
                gp.quicksum(Y[i, j] for i in range(num_warehouses + 1) if i != j) == X[j - 1],
                f"Flow_in_{j}")
        model.addConstr(
            gp.quicksum(Y[j, i] for i in range(num_warehouses + 1) if i != j) == X[j - 1],
            f"Flow_out_{j}")

        # MTZ subtour elimination constraints
        for i in range(1, num_warehouses + 1):
            for j in range(1, num_warehouses + 1):
                if i != j:
                    model.addConstr(
                        u[i] - u[j] + num_warehouses * Y[i, j] <= num_warehouses - 1,
                        f"MTZ_{i}_{j}")

        # Only visit built warehouses
        for i in range(1, num_warehouses + 1):
            model.addConstr(
                gp.quicksum(Y[j, i] for j in range(num_warehouses + 1) if j != i) == X[i - 1],
                f"Visit_warehouse_{i}_if_built")

        model.optimize()

        X_sol = np.zeros(num_warehouses, dtype=int)
        for i in range(num_warehouses):
            if X[i].X > 0.5:
                X_sol[i] = 1

        Y_sol = np.zeros((num_warehouses + 1, num_warehouses + 1), dtype=int)
        for i in range(num_warehouses + 1):
            for j in range(num_warehouses + 1):
                if Y[i, j].X > 0.5:
                    Y_sol[i, j] = 1

        return X_sol, Y_sol
