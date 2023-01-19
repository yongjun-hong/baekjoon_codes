import sys
import heapq
input = sys.stdin.readline

vertex,edge = map(int,input().split()) # 정점, 간선
in_degree = [0] * (vertex+1) 
graph = [[] for _ in range(vertex+1)]

for _ in range(edge):
    a,b = map(int,input().split())
    in_degree[b] += 1
    graph[a].append(b)

height = []
for i in range(1,(vertex+1)):
    if in_degree[i] == 0:
        heapq.heappush(height,i)
while height:
    m = heapq.heappop(height)
    print(m, end=' ')

    for e in graph[m]:
        in_degree[e] -= 1
        if in_degree[e] == 0:
            height.append(e)