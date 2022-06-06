import os
from collections import deque

class solution:
    
    def __init__(self):
        self.message = "Let's Go"
                
        # required input
        self.graph = [
            [],
            [2,3,8],
            [1,7],
            [1,4,5],
            [3,5],
            [3,4],
            [7],
            [2,6,8],
            [1,7]
        ]
        self.visited = [False] * 9

    def bfs(self, graph, start, visited):
        # 큐 구현을 위한 deque라이브러리 사용
        quque = deque([start])
        # 현재 노드를 방문 처리
        visited[start] = True

        # 큐가 빌때까지 반복
        while quque:
            #큐에서 하나의 원소를 뽑아서 출력
            v = quque.popleft()
            print(v, end=' ')

            # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
            for i in graph[v]:
                if not visited[i]:
                    quque.append(i)
                    visited[i] = True

    def run(self):
        self.bfs(graph = self.graph, start = 1, visited = self.visited)

    
if __name__ == "__main__":
    answer = solution()
    answer.run()
