# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from environments import Environment
import numpy as np

class AbstractSolver(ABC):
    @abstractmethod
    def __init__(self, env: Environment):
        self.name = None
        self.env = env

    
    @abstractmethod
    def solve(self):
        pass