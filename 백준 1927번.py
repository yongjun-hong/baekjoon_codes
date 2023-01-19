import heapq
import sys
input = sys.stdin.readline
heap = []
num = int(input())
for i in range(num):
    heap_num = int(input())
    if heap_num != 0:
        heapq.heappush(heap,heap_num)
    else:
        try:
            result_num = heapq.heappop(heap)
            print(result_num)
        except:
            print("0")