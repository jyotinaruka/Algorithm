def validParens(string):
    count = 0
    for c in string:
        if c == '(':
            count += 1
        if c == ')':
            count -= 1
        if count < 0:
            return False
    return True


print(validParens('(())(()))'))
print(validParens('(()())')
print(validParens('((()))')

print(validParens('))()()()((('))

