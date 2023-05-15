
def validate_brackets(string):
    stack = []
    bracket_pairs = {'(': ')', '[': ']', '{': '}'}
    
    for char in string:
        if char in bracket_pairs:
            stack.append(char)
        elif char in bracket_pairs.values():
            if not stack:
                return False
            opening_bracket = stack.pop()
            if char != bracket_pairs[opening_bracket]:
                return False
    
    return len(stack) == 0

print(validate_brackets("{}"))  # True
print(validate_brackets("{}(){}"))  # True
print(validate_brackets("()[[Extra Characters]]"))  # True
print(validate_brackets("(){}[[]]"))  # True
print(validate_brackets("{}{Code}[Fellows](())"))  # True
print(validate_brackets("[({}]"))  # False
print(validate_brackets("(]("))  # False
print(validate_brackets("{(})")) #False
