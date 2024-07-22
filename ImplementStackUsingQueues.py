class MyStack:

    def __init__(self):
        self.q = []

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        if len(self.q)==0:
            return null
        else :
           return self.q.pop()

    def top(self) -> int:
        return self.q[-1]