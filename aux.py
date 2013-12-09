import functools
import operator

def concat(x):
    return [i for s in x for i in s]

def containsp(x):
    return functools.partial(operator.contains, x)

def eqp(x):
    return functools.partial(operator.eq, x)

