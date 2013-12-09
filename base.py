from aux import *

class parser:
    def __init__(self, value):
        self.value = value

    def __call__(self, i):
        return self.value(i)

    def bind(self, other):
        return parser(lambda i: concat([other(v)(o) for (v, o) in self(i)]))

    def plus(self, other):
        return parser(lambda i: self(i) + other(i))

    def then(self, other):
        return self.bind(lambda _: other)

    def __ge__(self, other):
        return self.bind(other)

    def __rshift__(self, other):
        return self.then(other)

    def __add__(self, other):
        return self.plus(other)


