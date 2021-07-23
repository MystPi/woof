# woof
A lexer that turns your text into tokens. It's similar to YALL except that it's much simpler.

## Example
```py
from woof import Woof

lexer = Woof({
    # You provide the tokens in a dictionary:
    'NAME': r'[a-zA-Z_][a-zA-Z0-9_]*',
    'FLOAT': r'-?\d*\.\d+',
    'INT': r'-?\d+',
    
    'PLUS': r'\+',
    'MINUS': r'-',
    'TIMES': r'\*',
    'DIVIDE': r'/',
    
    'EQ': r'=',
    
    'LPAREN': r'\(',
    'RPAREN': r'\)'
},
map = {
    # These functions will be called on tokens that get matched, and will pass their re match object as the argument:
    'FLOAT': lambda x: float(x[0]),
    'INT': lambda x: int(x[0])
},
# This will simply ignore the matches of its regex:
ignore = r' ')

print(lexer.pretty(lexer.tokenize('x = 2 * (1 + 3)')))
```
