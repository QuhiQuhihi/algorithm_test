import os
import sys

class solution:
    
    def __init__(self):
        self.message = "Let's Go"

        # This algorithm shows O(2^N) complexity
        

    def fibo(self,  x):

        if x == 1 or x == 2:
            return 1
        else:
            return self.fibo(x-1) + self.fibo(x-2)

 

    def run(self):
        result = self.fibo(x=6)
        print(result)
    
if __name__ == "__main__":
    answer = solution()
    answer.run()
