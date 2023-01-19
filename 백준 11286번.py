import sys
import heapq
heap = []
input = sys.stdin.readline

num = int(input())
for i in range(num):
    x = int(input())
    if x != 0:
        heapq.heappush(heap,(abs(x),x))
    else:
        if len(heap) > 0: 
            min = heapq.heappop(heap) 
            print(min[1])
        else:
            print("0")

min = heapq.heappop(heap) 
print(min[1])