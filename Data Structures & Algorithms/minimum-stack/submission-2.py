class MinStack:

    def __init__(self):
        self.arr = []
        self.min_arr = []
        

    def push(self, val: int) -> None:
        self.arr.append(val)
        if self.min_arr:
            self.min_arr.append(min(self.min_arr[-1],val))
        else:
            self.min_arr.append(val)
        

    def pop(self) -> None:
        self.arr.pop()
        self.min_arr.pop()
        

    def top(self) -> int:
        return self.arr[-1]
        

    def getMin(self) -> int:
        return self.min_arr[-1]
        
