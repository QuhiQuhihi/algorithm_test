import os
import sys

class solution:
    
    def __init__(self):
        self.message = "Let's Go"
        # basic method to determine whether it is cyclical
        # Spanning Tree(신장트리)
        # Find spanning tree with minumum cost
        # 모든 간선에 대하여 정렬을 수행한 뒤에, 
        # 가장 거리가 짧은 간선부터 집합에 포함시키면 됨

        # This algorithm shows O(E*logE) complexity

        # v = 노드의 개수, e = 간선의 개수 
        self.v = 7    # v = 노드의 개수
        self.e = 9    # e  = 간선의 개수
        # self.input = sys.stdin.readline
        # v, e = map(int, input().split())

        # edges info (a, b, cost)
        self.link = [
            [1,2,29],
            [1,5,75],
            [2,3,35],
            [2,6,34],
            [3,4,7 ],
            [4,6,23],
            [4,7,13],
            [5,6,53],
            [6,7,25]
        ]
        self.parent = [0] * (self.v+1) # 부모 테이블 초기화
        self.edges = []
        self.result = 0

        # 부모 테이블상에서, 부모를 자기 자신으로 초기화
        for i in range(1, self.v+1):
            self.parent[i] = i
        

        # 모든 간선에 대한 정보를 입력받기
        for i in range(self.e):
            a, b, cost = self.link[i][0], self.link[i][1], self.link[i][2]
            # 비용순으로 정렬하기 위해서, 튜플의 첫 번째 원소를 비용으로 설정
            self.edges.append((cost,a,b))

        # # union 연산을 각각 수행
        # for i in range(self.e):
        #     a,b = self.link[i][0], self.link[i][1] 
        #     self.union_parent(self.parent, a, b)



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



    def kruskal(self):
        parent = self.parent
        result = self.result
        edges = self.edges

        # 간선을 비용순으로 정렬
        edges.sort()

        for edge in edges:
            cost, a, b = edge[0], edge[1], edge[2]
            # 싸이클이 발생하지 않는 경우에는 집합에만 포함
            if self.find_parent(parent=parent, x=a) != self.find_parent(parent=parent, x=b):
                self.union_parent(parent=parent, a=a, b=b)
                result += cost
        return result

    def run(self):
        result = self.kruskal()
        print(result)
    
if __name__ == "__main__":
    answer = solution()
    answer.run()
