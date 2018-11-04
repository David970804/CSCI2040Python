class Stack(object):
    def __init__(self):
        self.storage = []
    def push (self, newValue):
       self.storage.append( newValue )
    def top(self):
        return self.storage[len(self.storage) - 1]
    def pop(self):
        result = self.top()
        self.storage.pop()
        return result
    def isEmpty(self):
        return len(self.storage) == 0

class CalculatorEngine(object):
    def __init__(self):
        self.dataStack = Stack()
    def pushOperand (self, value):
        self.dataStack.push( value )
    def currentOperand ( self ):
        return self.dataStack.top()
    def performBinary (self, fun ):
        right = self.dataStack.pop()
        left = self.dataStack.pop()
        self.dataStack.push( fun(left, right))
    def doAddition (self):
        self.performBinary(lambda x, y: x + y)
    #lambda creates a function object with arguments x and y, expressions x + y
    def doSubtraction (self):
        self.performBinary(lambda x, y: x - y)
    def doMultiplication (self):
        self.performBinary(lambda x, y: x * y)
    def doDivision (self):
        try:
            self.performBinary(lambda x, y: x / y)
        except ZeroDivisionError:
            print (" divide by 0!")
            exit(1)
    def doTextOp (self, op):
        if (op == '+'): self.doAddition()
        elif (op == '-'): self.doSubtraction()
        elif (op == '*'): self.doMultiplication()
        elif (op == '/'): self.doDivision()

class RPNCalculator(object):
    def __init__(self):
        self.calcEngine = CalculatorEngine()
    def eval (self, line):
        words = line.split(" ")
        for item in words:
            if item in '+-*/':
                self.calcEngine.doTextOp( item )
            elif item == '%':
                right = self.calcEngine.dataStack.pop()
                left = self.calcEngine.dataStack.pop()
                self.calcEngine.dataStack.push(left%right)
            else:
                self.calcEngine.pushOperand( int (item))
        return self.calcEngine.currentOperand()
    def run(self):
        while True:
            line =  input("type an expression: ")
            if len(line) == 0:
                break
            print (self.eval( line ))
x = RPNCalculator()
