from .abstract_solver import AbstractSolver
import numpy as np

class DummySolver(AbstractSolver):
    def __init__(self, env):
        super().__init__(env)
        self.name = 'DummySolver'
    
    def solve(self):
        super().solve()

        print('\n-------------------------------------------------------------------')
        print('THIS IS A DUMMY SOLVER THAT IS ACTUALLY NOT SOLVING THE PROBLEM')
        print('instead, it prints the instance data so you know how to retrieve it')
        print(self.env.inst.weights)
        print(self.env.inst.service)
        print(self.env.inst.distances)
        print('-------------------------------------------------------------------\n')

        N_deposits = self.env.inst.service.shape[0]

        X = np.random.randint(0, 2, N_deposits)
        constructions = np.nonzero(X)[0]
        Y = np.zeros((N_deposits + 1, N_deposits + 1))
        Y[0, constructions[0] + 1] = 1
        for idx in range(len(constructions) - 1):
            Y[constructions[idx] + 1,constructions[idx+1] + 1] = 1
        Y[constructions[-1] + 1, 0] = 1

        return X, Y