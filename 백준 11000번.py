import sys
import heapq
input = sys.stdin.readline

q = []
num = int(input())
for i in range(num):
    q.append(list(map(int,input().split())))
q.sort()

nums_of_classroom = []
heapq.heappush(nums_of_classroom,q[0][1])
for i in range(1,num):
    if nums_of_classroom[0] > q[i][0]:
        heapq.heappush(nums_of_classroom,q[i][1])
    else:
        heapq.heappop(nums_of_classroom)
        heapq.heappush(nums_of_classroom,q[i][1])

print(len(nums_of_classroom))