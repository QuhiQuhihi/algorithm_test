import os

class solution:
    
    def __init__(self):
        self.message = "Let's Go"
        # This algorithm shows (N^2 + N)/2 complexity
        
        # required input
        self.array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


    def selection_sort(self, array):

        for i in range(len(array)):
            
            min_index = i # 가장 작은 원소의 인덱스
            for j in range(i+1, len(array)):
                if array[min_index] > array[j]:
                    min_index = j
            array[i], array[min_index] = array[min_index], array[i] # 스와프
        
        print(array)



    def run(self):
        self.selection_sort(array = self.array)

    
if __name__ == "__main__":
    answer = solution()
    answer.run()
