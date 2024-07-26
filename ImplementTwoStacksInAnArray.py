class TwoStacks:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    # Function to push an integer into stack 1
    def push1(self, x):
        self.s1.append(x)
       

    # Function to push an integer into stack 2
    def push2(self, x):
        self.s2.append(x)
        
        

    # Function to remove an element from top of stack 1
    def pop1(self):
        if len(self.s1) < 1:
            return -1
        return self.s1.pop()

    # Function to remove an element from top of stack 2
    def pop2(self):
        if len(self.s2) < 1:
            return -1
        return self.s2.pop()

