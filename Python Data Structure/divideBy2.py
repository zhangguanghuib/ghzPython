import Stack

def divideBy2(decNumber):
    remStack = Stack.Stack()

    while decNumber > 0:
        rem = decNumber % 2 # 求余数
        remStack.push(rem)
        decNumber = decNumber // 2 # 整除
    
    binString = ''
    while not remStack.isEmpty():
        binString = binString + str(remStack.pop())
    
    return binString

if __name__ == '__main__':
    print(divideBy2(42))  # 101010
    print(divideBy2(10))  # 1010
    print(divideBy2(233)) # 11101001
