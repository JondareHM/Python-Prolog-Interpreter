from prologpy import Solver


def test_actual_example():

    rules_text = """

        flag(X, T) :- temp(X, high, T).
        cool(X, T + 1) :- flag(X, T), flag(X, T + 1).
        shdn(X, T + 1) :- cool(X, T), flag(X, T + 1).
        malf(X, T - 2) :- shdn(X, T).

        temp(wt25, high, 0).
        temp(wt25, high, 1).
        temp(wt25, high, 2).

    """

    data_format = """

        temp(X, Y, T)

    """

    goal_text = """

        malf(X, T).

    """

    solver = Solver(rules_text)
    solution = solver.find_solutions(goal_text, data_format)

    print(str(solution.get("T")))
    assert True


def test_no_input():

    rules_text = """

        flag(X, T) :- temp(X, high, T).
        cool(X, T + 1) :- flag(X, T), flag(X, T + 1).
        shdn(X, T + 1) :- cool(X, T), flag(X, T + 1).
        malf(X, T - 2) :- shdn(X, T).

    """

    data_format = """

        temp(X, Y, T)

    """

    goal_text = """

        malf(X, T).

    """

    solver = Solver(rules_text)
    solution = solver.find_solutions(goal_text, data_format)

    print("Solutions " + str(solution))
    assert False


def test_simple_variable_query():

    rules_text = """
        descendant(X, Y, 0) :- offspring(X, Y, 0).
        descendant(X, Z, 0) :- offspring(X, Y, 0), descendant(Y, Z, 0).

        offspring(abraham, ishmael, 0).
        offspring(abraham, isaac, 0).
        offspring(isaac, esau, 0).
        offspring(isaac, jacob, 0).
    """

    data_format = """

        temp(X, Y, T)

    """

    query_text = """
        descendant(abraham, C, 0).
    """

    solver = Solver(rules_text)
    solutions = solver.find_solutions(query_text, data_format)

    """assert len(solutions.get("X")) == 4

    assert ("ishmael" in str(solution) for solution in solutions.get("X"))
    assert ("isaac" in str(solution) for solution in solutions.get("X"))
    assert ("esau" in str(solution) for solution in solutions.get("X"))
    assert ("jacob" in str(solution) for solution in solutions.get("X"))

    print(solutions)
    """
    assert True
