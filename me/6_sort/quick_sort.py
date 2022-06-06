import os

class solution:
    
    def __init__(self):
        self.message = "Let's Go"
        # 기준 데이터를 설정하고 그 기준보다 큰 데이토와 작은 데이터의 위치를 바꾸면 어떰?

        # This algorithm shows O(N * logN) complexity
        
        # required input
        self.array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
        # 모든 원소의 값이 0보다 크거나 같다고 가정


    def count_sort(self, array):

        # 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
        count = [0] * (max(array)+1)
        result = []

        for i in range(len(array)):
            count[array[i]] += 1 # 값 데이터에 해당하는 인덱스 값 증가
        
        # 리스트에 기록된 정렬 정보 확인
        for i in range(len(count)):
            for j in range(count[i]):
                result.append(i)

        return result



    def run(self):
        result = self.count_sort(array = self.array)
        print(result)
    
if __name__ == "__main__":
    answer = solution()
    answer.run()
