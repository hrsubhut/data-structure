class MinStack(object):
    #here what we try we use tuple and store value with mini value (0,1)so over 1 place

    def __init__(self):
        self.stack = []
        
    def push(self, value):
        if not self.stack:
            self.stack.append((value,value))
        else:
            current_min =self.stack[-1][1]
            self.stack.append((value,min(value,current_min)))


    def pop(self):
        return self.stack.pop()
        

    def top(self):
        return self.stack[-1][0]
        

    def getMin(self):
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()