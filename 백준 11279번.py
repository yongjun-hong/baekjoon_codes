import heapq
import sys
heap = []
number = int(input())
for i in range(number):
    mis_num = int(sys.stdin.readline())
    if mis_num != 0:
        heapq.heappush(heap,(-num))
    else:
        try:
            num = (-1 * heapq.heappop(heap))
            print(num)
        except:
            print("0")
