class MinStack:

    def __init__(self):
        self.stack = [] # val,minVal
        

    def push(self, val: int) -> None:
        prev = self.stack[-1][1] if self.stack else float('inf')
        self.stack.append([val,min(val,prev)])

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
