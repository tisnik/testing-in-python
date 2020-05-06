"""Implementace logiky aplikace, kterou budeme testovat."""


def function1():
    """První funkce, která volá funkci druhou."""
    print("function1 called")
    return function2()


def function2():
    """Druhá funkce, kterou v testech nahradíme mockem."""
    print("function2 called")
    return "function 2"
