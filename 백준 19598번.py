import sys
import heapq

input = sys.stdin.readline
num = int(input())
lecture,heap = [],[]
num_of_classroom = 1
for _ in range(num):
    start,end = map(int,input().split())
    lecture.append((start,end))
lecture.sort()
heapq.heappush(heap,lecture[0][1])
for i in range(1,num):
    if heap[0] > lecture[i][0]:
        heapq.heappush(heap,lecture[i][1])
        num_of_classroom += 1
    else:
        heapq.heappop(heap)
        heapq.heappush(heap,lecture[i][1])
print(num_of_classroom)