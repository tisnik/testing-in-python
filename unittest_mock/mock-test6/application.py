"""Implementace logiky aplikace, kterou budeme testovat."""


class Application:
    def __init__(self):
        pass

    def method1(self):
        """První metoda, která volá metodu druhou."""
        print("method1 called")
        return self.method2()

    def method2(self):
        """Druhá metoda, kterou v testech nahradíme mockem."""
        print("method2 called")
        return "method 2"
