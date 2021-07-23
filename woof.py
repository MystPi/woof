class Token:
    def __init__(self, type: str, value):
        self.type  = type
        self.value = value
        
    def __repr__(self):
        return f'<Token type: {self.type}, value: {self.value!r}>'


class Woof:
    def __init__(self, rules: dict, map: dict = {}, ignore: str = ''):
        self.rules  = rules
        self.map    = map
        self.ignore = ignore
        
    def tokenize(self, string: str):
        import re
        rest: str = string
        ret: list = []
        
        while rest:
            match = False
            for name, regex in self.rules.items():
                result = re.match(regex, rest)
                if result:
                    rest = rest[len(result[0]):]
                    if name in self.map:
                        ret.append(Token(name, self.map[name](result)))
                    else:
                        ret.append(Token(name, result[0]))
                    match = True
                    break
            if not match:
                if self.ignore:
                    result = re.match(self.ignore, rest)
                    if result:
                        rest = rest[len(result[0]):]
                        match = True
                if not match:
                    print(f'Invalid token[s] in {rest!r}')
                    rest = rest[1:]
        
        return ret
        
    @classmethod
    def pretty(cls, l: list):
        return '\n'.join(list(map(str, l)))
