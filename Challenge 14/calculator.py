import sys

def get_operands(stack):
    #Pop two operands from the stack and return them.
    return stack.pop(), stack.pop()

def op_plus(stack):
    x, y = get_operands(stack)
    stack.append(x + y)

def op_minus(stack):
    x, y = get_operands(stack)
    stack.append(y - x)

def op_multiply(stack):
    x, y = get_operands(stack)
    stack.append(x * y)

def op_divide(stack):
    x, y = get_operands(stack)
    stack.append(y / x)

def op_power(stack):
    x, y = get_operands(stack)
    stack.append(y ** x)

def op_mod(stack):
    x, y = get_operands(stack)
    stack.append(y // x)

def op_percentage(stack):
    x, y = get_operands(stack)
    stack.append(y % x)
    
def end(stack):
    pass
        


operators = {'+': op_plus,
             '-': op_minus,
             '*': op_multiply,
             '/': op_divide,
             '**': op_power,
             '//': op_mod,
             '%' : op_percentage,
             'q' : end}


        
stack =[]
inputstr = input('RPN expression:')
while inputstr.upper() !="Q":
    
    tokens = inputstr.strip().split()
    for token in tokens:
        if token in operators:
                        # Operate with the top two numbers on the stack
            operators[token](stack)
        else:
                        # We encountered a number: push it onto the top of the stack
            stack.append(float(token))

    # Output the answer
    print(stack[0])
    inputstr = input('RPN expression:')
