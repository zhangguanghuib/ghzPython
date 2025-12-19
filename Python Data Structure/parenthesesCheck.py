import Stack

def matches(open, close):
    opens = '([{'
    closers = ')]}'
    return opens.index(open) == closers.index(close)

def parenthesesCheck(symbolString):
    stack = Stack.Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in '([{':
            stack.push(symbol)
        else:
            if stack.isEmpty():
                balanced = False
            else:
                top = stack.pop()
                if not matches(top, symbol):
                    balanced = False
        index = index + 1
    
    if balanced and stack.isEmpty():
        return True
    else:
        return False
    
if __name__ == '__main__':
    print(parenthesesCheck('({[]})'))  # True
    print(parenthesesCheck('((()))'))  # True
    print(parenthesesCheck('(()'))      # False
    print(parenthesesCheck('())'))      # False
    print(parenthesesCheck('([)]'))     # False
    print(parenthesesCheck('()()'))     # True