import os
import sys

class solution:
    
    def __init__(self):
        self.message = "Let's Go"
        # Fibonacci in Top down approach
        # use cache = memorization

        self.x = 6
        self.d = [0] * (self.x + 1)
        

    def fibo(self, x):
        
        print(f'f(x={x})', end=' ')

        if x == 1 or x == 2:
            return 1

        if self.d[x] != 0:
            return self.d[x]

        self.d[x] =  self.fibo(x-1) + self.fibo(x-2)
        return self.d[x]

 

    def run(self):
        result = self.fibo(x=self.x)
        print(result)
    
if __name__ == "__main__":
    answer = solution()
    answer.run()
