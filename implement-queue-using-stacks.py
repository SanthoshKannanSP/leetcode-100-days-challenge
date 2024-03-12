class MyQueue:

    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def push(self, x: int) -> None:
        while self.output_stack:
            self.input_stack.append(self.output_stack.pop())
        self.input_stack.append(x)
        while self.input_stack:
            self.output_stack.append(self.input_stack.pop())

    def pop(self) -> int:
        return self.output_stack.pop()

    def peek(self) -> int:
        return self.output_stack[-1]

    def empty(self) -> bool:
        return not bool(self.output_stack)