import Stack

def baseConverter(decNumber, base):

    digits = '0123456789ABCDEF' 

    remStack = Stack.Stack()

    while decNumber > 0:
        rem = decNumber % base
        remStack.push(rem)
        decNumber = decNumber // base

    newString = ''
    while not remStack.isEmpty():
        newString = newString + digits[remStack.pop()]
        
    return newString

if __name__ == '__main__':
    print(baseConverter(42, 2))  # 101010
    print(baseConverter(10, 2))  # 1010
    print(baseConverter(233, 2)) # 11101001
    print(baseConverter(42, 16)) # 2A
    print(baseConverter(10, 16)) # A
    print(baseConverter(233, 16))# E9
