import os
import sys

class solution:
    
    def __init__(self):
        self.message = "Let's Go"
        # Advanced method to determine whether it is coprime

        # This algorithm shows less than O(V) complexity

        # Use Path Compression technique to reduce complexity

        # v = 노드의 개수, e = 간선의 개수 
        self.v = 3    # v = 노드의 개수
        self.e = 3    # e  = 간선의 개수
        # self.input = sys.stdin.readline
        # v, e = map(int, input().split())

        self.link = [
            [1,2],
            [1,3],
            [2,3]
        ]
        self.parent = [0] * (self.v+1) # 부모 테이블 초기화

        # 부모 테이블상에서, 부모를 자기 자신으로 초기화
        for i in range(1, self.v+1):
            self.parent[i] = i
        
        # union 연산을 각각 수행
        for i in range(self.e):
            a,b = self.link[i][0], self.link[i][1] 
            self.union_parent(self.parent, a, b)

        self.cycle = False # 싸이클 발생
        

        # # union 연산을 각각 수행
        # for i in range(self.e):
        #     a,b = self.link[i][0], self.link[i][1] 
        #     self.union_parent(self.parent, a, b)



    # 특정 원소가 속한 집합을 찾기 --> 여기를 개선 !!!
    def find_parent(self, parent, x):
        # find 함수를 재귀적으로 호출한 뒤에 부모 테이블 값을 갱신.

        # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
        if parent[x] != x:
            return self.find_parent(parent, parent[x])
        
        ## basic
        # return x
        
        ## Advanced
        # 이럴 경우, 각 노드가 find 함수 호출한 이후에, 해당 노드의 루트 노드가 바로 부모 노드가 됨.
        return parent[x]

    
    # 두 원소가 속한 집합을 합치기(합집합)
    def union_parent(self, parent, a, b):
        a = self.find_parent(parent, a)
        b = self.find_parent(parent, b)

        if a < b:
            parent[b] = a
        else:
            parent[a] = b



    def coprime_cycle(self):

        # union 연산을 각각 수행
        for i in range(self.e):
            a,b = self.link[i][0], self.link[i][1] 

            # 싸이클이 발생한 경우 종료
            if self.find_parent(self.parent, a) == self.find_parent(self.parent, b):
                self.cycle = True
                break
            # 싸이클이 발생하지 않았다면 합집합(union) 수행
            else:
                self.union_parent(self.parent, a, b)
        
        if self.cycle:
            print("싸이클이 발생했습니다")
        else:
            print("싸이클이 발생하지 않았습니다")



    def run(self):
        result = self.coprime_cycle()
        print(result)
    
if __name__ == "__main__":
    answer = solution()
    answer.run()
