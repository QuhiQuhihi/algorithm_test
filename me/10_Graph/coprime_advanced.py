import os
import sys

class solution:
    
    def __init__(self):
        self.message = "Let's Go"
        # basic method to determine whether it is coprime

        # This algorithm shows O(V) complexity

        # v = 노드의 개수, e = 간선의 개수 
        self.v = 6    # v = 노드의 개수
        self.e = 4    # e  = 간선의 개수
        # self.input = sys.stdin.readline
        # v, e = map(int, input().split())

        self.link = [
            [1,4],
            [2,3],
            [2,4],
            [5,6],
        ]
        self.parent = [0] * (self.v+1) # 부모 테이블 초기화

        # 부모 테이블상에서, 부모를 자기 자신으로 초기화
        for i in range(1, self.v+1):
            self.parent[i] = i
        

        # union 연산을 각각 수행
        for i in range(self.e):
            a,b = self.link[i][0], self.link[i][1] 
            self.union_parent(self.parent, a, b)



    # 특정 원소가 속한 집합을 찾기
    def find_parent(self, parent, x):
        # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
        if parent[x] != x:
            return self.find_parent(parent, parent[x])
        return parent[x]
    
    # 두 원소가 속한 집합을 합치기(합집합)
    def union_parent(self, parent, a, b):
        a = self.find_parent(parent, a)
        b = self.find_parent(parent, b)

        if a < b:
            parent[b] = a
        else:
            parent[a] = b



    def coprime(self):
        # 각 원소가 속한 집합 출력
        result = {}
        for i in range(1, self.v + 1):
            result[i] = self.find_parent(self.parent, i)

        return result



    def run(self):
        result = self.coprime()
        print(result)
    
if __name__ == "__main__":
    answer = solution()
    answer.run()
