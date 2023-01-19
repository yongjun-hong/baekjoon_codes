import sys
import heapq
# input = sys.stdin.readline

# nums_people,compare = map(int,input().split())
# in_degree = [0] * (nums_people+1)
# graph = [[] for _ in range(nums_people+1)]

# for _ in range(compare):
#     a,b = map(int,input().split())
#     in_degree[b] += 1
#     graph[a].append(b)

# height = []
# for i in range(1,(nums_people+1)):
#     if in_degree[i] == 0:
#         heapq.heappush(height,i)
# # print(height)
# while height:
#     m = heapq.heappop(height)
#     print(m, end=' ')

#     for e in graph[m]:
#         in_degree[e] -= 1
#         if in_degree[e] == 0:
#             height.append(e)
print(sys.version)