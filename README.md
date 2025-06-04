---
Operational Research Project 2024/2025
---

# Description

You have been commissioned by the renowned poultry company *Polli Tech of N.I. & Co.* to design a distribution chain for the commercialization of its products. Specifically, the company requests you to determine the optimal placement (from a set of possible locations) of warehouses for goods, which are intended to distribute their products to nearby supermarkets.

Each warehouse has a construction cost and can serve a certain subset of supermarkets. Each supermarket not served by any warehouse results in an economic loss for the company. Finally, the placement of the warehouses must account for the transportation cost of goods from the company to the warehouses themselves, which is carried out using a single vehicle that departs from the company, visits each warehouse, and returns to the company every day.

# Data

Each problem instance consists of the following files:

-   `weights.json`: contains the costs the company may incur, which are:
    -   `’construction’`: daily cost due to the construction and maintenance of a warehouse (assume the construction cost is not a one-time payment but amortized over time).
    -   `’missed_supermarket’`: daily penalty for a supermarket not served by any warehouse.
    -   `’travel’`: fuel cost per kilometer traveled.

-   `service.csv`: a matrix where each row refers to a possible warehouse location and each column to a supermarket. If a warehouse can serve a certain supermarket, the corresponding matrix element is `1`; otherwise, it is `0`.

-   `distances.csv`: a distance matrix between possible warehouse locations and between possible warehouse locations and the company. For both rows and columns, the first element refers to the company, while the others refer to the warehouses, in the same order as in `service.csv`. Each element of the matrix (which is not necessarily symmetric) represents the distance in kilometers from the location in the row to the location in the column.

# Task

Using **Python** as the programming language and **GUROBI** as the solver, develop a linear programming model to solve the problem.

# Technical Requirements

The project must be completed in groups of 1-3 people.

The solver must consist of a single file named `solver_XXXXXX_YYYYYY_ZZZZZZ.py`, where `XXXXXX`, `YYYYYY`, and `ZZZZZZ` are the student IDs of the group members. For example, if a group consists of two people with student IDs `123456` and `654321`, the file should be named `solver_123456_654321.py`. If a student with ID `999999` decides to work individually, the file should be named `solver_999999.py`.

The file must contain a class that inherits from the `AbstractSolver` class and must be named exactly as the file that contains it. For example, students with IDs `123456` and `654321` will have a file named `solver_123456_654321.py` containing the class `class solver_123456_654321(AbstractSolver):`.

In this class, you must implement the `solve()` method, which should take no input (the necessary data is available in `self.inst`) and must return, in order, the vector `X` and the matrix `Y` as output.

The vector `X` is a binary vector with a length equal to the total number of possible warehouse locations. Each element is `1` (or `True`) if a warehouse is built in that location, and `0` (or `False`) otherwise.

The matrix `Y` is a binary matrix where both dimensions are equal to the number of possible warehouse locations plus one (so it has the same dimensions as the distance matrix in `distances.csv`). The first row and column refer to the company, while the remaining rows and columns refer to the possible warehouse locations. The generic element `i,j` of the matrix is `1` (or `True`) if the vehicle’s route includes the path from `i` to `j`, and `0` (or `False`) otherwise.

# Testing

To test the solver, follow these steps:

-   Place the file inside the `solvers` folder.
-   Update the `solvers/__init__.py` file by importing the solver and adding the class name to `__all__`.
-   Replace the `DummySolver` in `main.py` with your solver.
-   Run `main.py` to use the solver.
-   Run `evaluator.py` to see the total cost of the solution found by the solver.

# Important Note

The submitted solvers will be evaluated exactly as described in the previous section, using the same tools provided during development. Therefore, if `main.py` or `evaluator.py` produce an error (due to incorrect file name, class name, output format, or any other reason) when executed, the project will automatically receive **0 points**.

# Deadline

The project must be submitted via the **Elaborati** section of the Teaching Portal (one submission per group) by **23:59 on 30/06/2025**.
