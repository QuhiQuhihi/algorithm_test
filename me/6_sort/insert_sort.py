import os

class solution:
    
    def __init__(self):
        self.message = "Let's Go"
        # 데이터를 하나씩 확인하며, 각 데이터를 적절한 위치에 삽입하면 어떨까?
        # 현재의 데이터가 거의 정렬되 있다면 매우 빠르게 작동. 최선의 경우 O(N)

        # This algorithm shows O(N^2) complexity
        
        # required input
        self.array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


    def insert_sort(self, array):

        # Start from index 0+1 (Second one), by assuming that first is 

        for i in range(0+1, len(array)):
            
            for j in range(i,0,-1):
                # 한칸씩 왼쪽으로 이동
                if array[j] < array[j-1]:
                    array[j], array[j-1] = array[j-1], array[j]
                # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
                else:
                    break

            
        print(array)



    def run(self):
        self.insert_sort(array = self.array)

    
if __name__ == "__main__":
    answer = solution()
    answer.run()
