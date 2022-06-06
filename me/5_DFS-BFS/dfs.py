import os

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

    def dfs(self, graph, v, visited):
        # 현재 노드를 방문 처리
        visited[v] = True
        print(v, end=' ')
        
        # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
        for i in graph[v]:
            if not visited[i]:
                self.dfs(graph, i, visited)

    def run(self):
        self.dfs(graph = self.graph, v=1, visited = self.visited)

    
if __name__ == "__main__":
    answer = solution()
    answer.run()
