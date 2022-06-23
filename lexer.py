import re

class Lexer:
    def __init__(self, rules):
        self.rules = rules

    def lex(self, code, add_unlexable = False, silent = False):
        matched = False
        results = []
        while code != '':
            matched = False
            for tokName, tokRegex in self.rules:
                if (match := re.match(tokRegex, code)):
                    results.append((tokName, code[:match.span()[1]]))
                    code = code[match.span()[1]:]
                    matched = True
                    break

            if not matched:
                if not silent:
                    print('Token unmatchable:', code[1])
                if add_unlexable:
                    results.append(('@Lexer.lexer~unlexable', code[1]))
                code = code[1:]

        return results

if __name__ == '__main__':
    lexer = Lexer([
        ('num', r'\d+'),
        ('letter', r'[a-zA-Z]')
    ])
    print(lexer.lex('noise22ask'))
