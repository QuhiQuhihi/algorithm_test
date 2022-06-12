import os
import sys

class solution:
    
    def __init__(self):
        self.message = "Let's Go"
        # 암기 추천

        # This algorithm shows O(N) complexity
        
        # 이진 탐색은 데이터가 무작위 일때는 사용할 수 없지만,
        # 데이터가 종렬되어 있다면 매우 빠르게 사용할 수 있음

        # 이진 탐색은 탐색 범위를 절반씩 좁혀가며 데이터를 탐색함.

        # required input
        self.array = [0,2,4,6,8,10,12,14,16,18,20]
        self.target = 4


    def binary_search_recurisve(self, array, target, start, end):
        # This method deploy recursive method

        n = len(array)

        if start > end:
            return None
        
        mid = (start + end)//2
        
        # 찾은 경우 중간점 인덱스 반환 (인덱스는 0부터 시작)
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            return self.binary_search_recurisve(array, target, start, mid-1)
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        elif array[mid] < target:
            return self.binary_search_recurisve(array, target, start, mid+1)
        else:
            print("wrong")
        
    
    def binary_search_loop(self, array, target, start, end):
        
        while start <= end:
            mid = (start + end) // 2

            # 찾은 경우 중간점 인덱스 반환 (인덱스는 0부터 시작)
            if array[mid] == target:
                return mid
            # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
            elif array[mid] > target:
                end = mid - 1
            # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
            elif array[mid] < target:
                start = mid + 1
            else:
                return None
 

    def run(self):
        result = self.binary_search_recurisve(array = self.array, target=self.target, start=0, end=len(self.array)-1)
        print(result)
        result = self.binary_search_loop(array = self.array, target=self.target, start=0, end=len(self.array)-1)
        print(result)
    
if __name__ == "__main__":
    answer = solution()
    answer.run()
