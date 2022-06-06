import os
import sys
import heapq

class solution:
    
    def __init__(self):
        self.message = "Let's Go"
        # dijkstra enhanced version - heap

        # 파이썬 heapq 라이브러리에서 tuple을 원소로 받을 경우, 첫번째 원소를 기준으로 우선 순위를 구성
        # (거리, 노드번호) --> 거리를 기준으로 heapq 정렬
        # heapq를 사용시 get_smallest_node() 함수가 필요없음.

        # 방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드를 선택하는 과정 반복
        # 한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾는 것으로 이해

        # This algorithm shows O(E*logV) complexity
        # V = number of nodes, E = number of lines
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
        


    def dijkstra(self, start_node):

        distance = self.distance
        graph = self.graph

        q = []

        # 시작 노드로 가기 위한 최단 경로는 0으로 설정하며, 큐에 삽입
        heapq.heappush(q, (0, start_node))
        distance[start_node] = 0

        # 큐가 비어있지 않다면
        while q:
            # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
            dist, now = heapq.heappop(q)
            # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
            if distance[now] < dist:
                continue

            # 현재 노드와 연결된 다른 인접한 노드들을 확인
            for i in graph[now]:
                cost = dist + i[1]
                # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
                
        return distance


    def run(self):
        result = self.dijkstra(start_node=self.start)
        print(result)
    
if __name__ == "__main__":
    answer = solution()
    answer.run()
