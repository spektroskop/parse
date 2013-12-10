from parse import *

parse_string = char('"') >> \
               many(noneof('"')) >= (lambda x:
               char ('"') >> \
               unit(x))

parse_number = some(digit) >= (lambda x:
               unit(int(x)))

symbol = oneof("!#$%&|*+-/:<=>?@^_~")

initial = alpha + symbol

subsequent = alpha + digit + symbol

boolean = char("#") >> \
          oneof("tf") >= (lambda x:
          unit(x == "t"))

identifier = initial >= (lambda x:
             many(subsequent) >= (lambda y:
             unit(x + y)))

parse_atom = boolean + identifier

parse_expr = parse_atom + parse_string + parse_number

