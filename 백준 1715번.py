import sys
import heapq
input = sys.stdin.readline
heap = []
num = int(input())
for i in range(num):
    heapq.heappush(heap,int(input()))
result_list = []
while heap:
    if len(heap) == 1:
        break
    else:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        third = first + second
        result_list.append(third)
        heapq.heappush(heap,third)
result = 0
for i in range(len(result_list)):
    result += result_list[i]
print(result)