class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.stackSize = 0
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if self.stackSize<self.maxSize:
            self.stack.append(x)
            self.stackSize+=1

    def pop(self) -> int:
        if self.stackSize==0:
            return -1
        else:
            self.stackSize-=1
            return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k,self.stackSize)):
            self.stack[i]+=val