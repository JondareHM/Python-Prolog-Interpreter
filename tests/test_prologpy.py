from prologpy import Solver


def test_simple_goal_query():

    rules_text = """

        brother_sister(joe, monica, 1).
        brother_sister(eric, erica, 1).
        brother_sister(jim, rebecca, 1).

    """

    goal_text = """

        brother_sister(jim, rebecca, 1).

    """

    solver = Solver(rules_text)
    solution = solver.find_solutions(goal_text)

    assert solution


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

    goal_text = """

        malf(X, T).

    """

    solver = Solver(rules_text)
    solution = solver.find_solutions(goal_text)

    assert solution
