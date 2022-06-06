import os
import sys
import heapq

class solution:
    
    def __init__(self):
        self.message = "Let's Go"
        # floyd_warshall

        # 방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드를 선택하는 과정 반복
        # 한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾는 것으로 이해

        # This algorithm shows O(N^3) complexity
        # V = number of nodes, E = number of lines
        # 각 노드에 대한 현재까지의 최단 거리 정보를 항상 1차원 리스트에 저장하며 리스트를 계속 갱신함



        # n = 노드의 개수, m  = 간선의 개수를 입력받기
        self.n = 4     # n = 노드의 개수
        self.m = 7    # m  = 간선의 개수
        # self.input = sys.stdin.readline
        # n, m = map(int, input().split())

        # [a,b,c] = a번 노드에서 b번 노드로 가는 비용이 c라는 의미
        self.link = [
            [1,2,4],
            [1,4,6],
            [2,1,3],
            [2,3,7],
            [3,1,5],
            [3,4,4],
            [4,3,2],
        ]

        INF = int(1e9)

        # 2차원 리스트(그래프 표현)을 만들고, 모든 값을 무한으로 초기화
        self.graph = [[INF] * (self.n + 1) for _ in range(self.n + 1)]
        # 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
        for a in range(1, self.n+1):
            for b in range(1, self.n+1):
                if a == b:
                    self.graph[a][b] = 0

        # 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
        for l in self.link:
            a, b, c = l[0], l[1], l[2]
            self.graph[a][b] = c
        


    def floyd_warshall(self):

        graph = self.graph

        # 점화식에 따라 플로이드 워셀 알고리즘을 수행
        for k in range(1, self.n+1):
            for a in range(1, self.n+1):
                for b in range(1, self.n+1):
                    graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
        
        return graph

    def print_result(self, graph_result):
        INF = int(1e9)
        graph = graph_result
        
        for a in range(1, self.n+1):
            print(" ")
            for b in range(1, self.n+1):
                # 도달할 수 없는 경우, 무한(INF)이라고 출력
                if graph[a][b] == INF:
                    print("INFINITY", end=' ')
                else:
                    print(graph[a][b], end=' ')


    def run(self):
        result = self.floyd_warshall()
        self.print_result(graph_result=result)

        # print(result)
    
if __name__ == "__main__":
    answer = solution()
    answer.run()
