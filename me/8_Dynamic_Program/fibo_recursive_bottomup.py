import os
import sys

class solution:
    
    def __init__(self):
        self.message = "Let's Go"
        # Fibonacci in Bottom up approach
        # use DP table 

        self.x = 6
        self.d = [0] * (self.x)
        

    def fibo(self, x):
        
        self.d[0] = 1
        self.d[1] = 1

        for i in range(2, self.x):
            self.d[i] = self.d[i-1] + self.d[i-2]
        
        return self.d[self.x - 1]

 

    def run(self):
        result = self.fibo(x=self.x)
        print(result)
    
if __name__ == "__main__":
    answer = solution()
    answer.run()
