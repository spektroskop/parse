from base import *
from aux import *

def unit(v):
    return parser(lambda i: [(v, i)])

one = parser(lambda i: [(i[0], i[1:])] if i else [])

none = parser(lambda _: [])

def many(p):
    return some(p) + unit("")

def some(p):
    return p >= (lambda x:
           many(p) >= (lambda y:
           unit(x + y)))

def satisfy(p):
    return one >= (lambda x: unit(x) if p(x) else none)

def char(c):
    return satisfy(eqp(c))

digit = satisfy(str.isdigit)
alpha = satisfy(str.isalpha)
alnum = satisfy(str.isalnum)
upper = satisfy(str.isupper)
lower = satisfy(str.islower)
space = satisfy(str.isspace)

def oneof(s):
    return satisfy(containsp(s))

def string(s):
    if not s:
        return unit("")
    else:
        return char(s[0]) >> (string(s[1:]) >> unit(s))
