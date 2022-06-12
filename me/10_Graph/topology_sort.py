import os
import sys
from collections import deque

class solution:
    
    def __init__(self):
        self.message = "Let's Go"
        # 위상정렬
        # This algorithm has O(V+E) has complexity
        
        # 순서가 정해져 있는 일련의 작업을 차례대로 수행해야 할 때 사용
        # 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것

        # 1. 진입 차수가 0인 노드를 큐에 넣는다
        # 2. 큐가 빌때까지 다음의 과정을 반복한다
        # 2_1. 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다
        # 2_2. 새롭게 진입차수가 0이 된 노드를 큐에 넣는다

        # 큐에서 원소가 v번 추출되기 전에 큐가 비어버리면 사이클이 발생한 것.

        # v = 노드의 개수, e = 간선의 개수 
        self.v = 7    # v = 노드의 개수
        self.e = 8    # e  = 간선의 개수
        # self.input = sys.stdin.readline
        # v, e = map(int, input().split())

        # edges info (a, b, cost)
        self.link = [
            [1,2],
            [1,5],
            [2,3],
            [2,6],
            [3,4],
            [4,7],
            [5,6],
            [6,4]
        ]
        self.indegree = [0] * (self.v+1) # 부모 테이블 초기화
        # 각 노드의 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
        self.graph = [[] for i in range(self.v + 1)]

        # 방향 그래프의 모든 간선에 대한 정보를 입력받기
        for i in range(self.e):
            a, b = self.link[i][0], self.link[i][1]
            self.graph[a].append(b) # 정점 A에서 B로 이동 가능

            # 진입 차수를 1 증가
            self.indegree[b] += 1


    def topology_sort(self):

        result = [] # 알고리즘 수행 결과를 담을 리스트
        q = deque() # 큐 기능을 위한 deque 라이브러리 사용
        
        graph = self.graph
        indegree = self.indegree


        # 처음 시작할 때는 진입 차수가 0인 노드를 큐에 삽입
        for i in range(1, self.v + 1):
            if indegree[i] == 0:
                q.append(i)
            
        # 큐가 빌 때까지 반복
        while q:
            # 큐에서 원소 꺼내기
            now = q.popleft()
            result.append(now)
            # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
            for i in graph[now]:
                indegree[i] -= 1
                #새롭게 진입차수가 0이 되는 노드를 큐에 삽입
                if indegree[i] == 0:
                    q.append(i)

        return result

    def run(self):
        result = self.topology_sort()
        print(result)
    
if __name__ == "__main__":
    answer = solution()
    answer.run()
