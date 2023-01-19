# import sys,heapq
# input = sys.stdin.readline

# nums_of_prob, hint = map(int,input().split())
# prob = []
# prob_hint = []
# problem = []
# for i in range(hint):
#     a,b = map(int,input().split())
#     heapq.heappush(prob_hint,(a,b))

# for i in range(nums_of_prob):
#     prob.append(i)
# while prob_hint:
#     a,b = heapq.heappop(prob_hint)
#     for i in
# print(' '.join(map(str,problem)))


import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
in_degree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())

    in_degree[b] += 1 # 간선의 개수를 하나 추가시킨다.
    graph[a].append(b)

queue = []

for i in range(1, n + 1):
    if in_degree[i] == 0: # in_degree가 0이라는 뜻은 연결된 간선의 개수가 없다는 것이다.
        heapq.heappush(queue, i)

while queue:
    current = heapq.heappop(queue)
    print(current, end=" ")

    for g in graph[current]:
        in_degree[g] -= 1

        if in_degree[g] == 0:
            heapq.heappush(queue, g)

#위상정렬에 대해 알아보기