# woof
A lexer that turns your text into tokens.

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
# OPTIONAL: These functions will be called on tokens that get matched, and will pass their re match object as the argument:
map = {
    'FLOAT': lambda x: float(x[0]),
    'INT': lambda x: int(x[0])
},
# OPTIONAL: This will simply ignore the matches of its regex:
ignore = r' ')

print(lexer.pretty(lexer.tokenize('x = 2 * (1 + 3)')))
```
## Usage
```py
# Import woof
from woof import Woof

# Create the Woof class
lexer = Woof(
    # Token definitions
    {
        'TOKEN_NAME': r'some regex here'
    },
    # Token map (optional)
    map = {
        'TOKEN_NAME': some_function_or_lambda_with_one_parameter
    },
    # Ignore regex (optional)
    ignore = r' +'
)

# Tokenize a string
tokens = lexer.tokenize('string')
```
