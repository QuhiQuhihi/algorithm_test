import os

class solution:
    
    def __init__(self):
        self.message = "Let's Go"

        # This algorithm shows O(N) complexity
        
        # required input
        self.array = ['aa','bb','cc','dd','ee','ff']
        self.target = 'cc'


    def sequential_search(self,  target, array):


        # 각 원소를 하나씩 확인하며
        for i in range(len(array)):
            if array[i] == target:
                return i # 현재 위치 반환 (인덱스는 0부터 시작함)
 

    def run(self):
        result = self.sequential_search(array = self.array, target = self.target)
        print(result)
    
if __name__ == "__main__":
    answer = solution()
    answer.run()
