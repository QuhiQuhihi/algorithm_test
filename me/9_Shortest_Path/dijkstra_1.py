import os
import sys
import heapq

class solution:
    
    def __init__(self):
        self.message = "Let's Go"
        # dijkstra simple version

        # 방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드를 선택하는 과정 반복
        # 한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾는 것으로 이해

        # This algorithm shows O(V^2) complexity
        # V = number of nodes
        # 각 노드에 대한 현재까지의 최단 거리 정보를 항상 1차원 리스트에 저장하며 리스트를 계속 갱신함



        # n = 노드의 개수, m  = 간선의 개수를 입력받기
        self.n = 6     # n = 노드의 개수
        self.m = 11    # m  = 간선의 개수
        self.start = 1 # 시작 포인트 설정
        # self.input = sys.stdin.readline

        # [a,b,c] = a번 노드에서 b번 노드로 가는 비용이 c라는 의미
        self.link = [
            [1,2,2],
            [1,3,5],
            [1,4,1],
            [2,3,3],
            [2,4,2],
            [3,2,3],
            [3,6,5],
            [4,3,3],
            [4,5,1],
            [5,3,1],
            [5,6,2],
        ]

        INF = int(1e9)

        # n = 노드의 개수, m  = 간선의 개수를 입력받기
        # n, m = map(int, input().split())

        # 시작 노드 번호를 입력받기
        # start = int(input())
        start = self.start

        # 각 노드의 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
        self.graph = [[] for i in range(self.n + 1)]
        # 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
        self.visited = [False] * (self.n + 1)
        # 최단 거리 테이블을 모두 무한으로 초기화
        self.distance = [INF] * (self.n + 1)

        # 모든 간선 정보를 입력받기
        for l in self.link:
            a, b, c = l[0], l[1], l[2]
            self.graph[a].append((b, c))
        
    # heapq를 사용시 get_smallest_node() 함수가 필요없음.
    def get_smallest_node(self, distance, visited):
        INF = int(1e9)
        min_value = INF
        index = 0 # 가장 최단 거리가 짧은 노드 (인덱스)
        for i in range(1, self.n+1):
            if distance[i] < min_value and not visited[i] :
                min_value = distance[i]
                index = i
        return index

    def dijkstra(self, start_node):

        distance = self.distance
        visited = self.visited
        graph = self.graph


        # 시작 노드에 대해서 초기화
        distance[start_node] = 0
        visited[start_node] = True

        for j in graph[start_node]:
            distance[j[0]] = j[1]
        
        # 시작 노드를 제외한 전체 n-1개 노드에 대해 반복
        for i in range(self.n-1):
            # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문 처리
            now = self.get_smallest_node(distance = distance, visited = visited)
            visited[now] = True
            
            # 현재 노드와 연결된 다른 노드를 확인
            for j in graph[now]:
                cost = distance[now] + j[self.start]
                # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                if cost < distance[j[0]]:
                    distance[j[0]] = cost
                
        return distance


    def run(self):
        result = self.dijkstra(start_node=self.start)
        print(result)
    
if __name__ == "__main__":
    answer = solution()
    answer.run()
