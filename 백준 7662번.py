import sys
import heapq
input = sys.stdin.readline

num = int(input())
for i in range(num):
    max_heap = []
    min_heap = []
    visited = [False] * 1000000
    inside_num = int(input())
    for e in range(inside_num):
        mission,mis_num = map(str,input().split())
        if mission == 'I':
            heapq.heappush(min_heap,(int(mis_num),e))
            heapq.heappush(max_heap,(-(int(mis_num)),e))
            visited[e] = True
        elif mission == 'D':
                if int(mis_num) == -1:  
                    while min_heap and not visited[min_heap[0][1]] :
                        # print("11111111")
                        heapq.heappop(min_heap)
                    if min_heap:               
                        visited[min_heap[0][1]] = False
                        heapq.heappop(min_heap)
                else: 
                    while max_heap and not visited[max_heap[0][1]] :
                        # print("22222222222")
                        heapq.heappop(max_heap)
                    if max_heap:               
                        visited[max_heap[0][1]] = False
                        heapq.heappop(max_heap)
    
    # while min_heap and not visited[min_heap[0][1]]:
    #     heapq.heappop(min_heap)
    # while max_heap and not visited[max_heap[0][1]]:
    #     heapq.heappop(max_heap)
    if min_heap and max_heap:
        print(-(max_heap[0][0]),min_heap[0][0])
    else:
        print("EMPTY")


        import sys
import heapq
input = sys.stdin.readline

num = int(input())
for i in range(num):
    max_heap = []
    min_heap = []
    plus = 0
    inside_num = int(input())
    for e in range(inside_num):
        mission,mis_num = map(str,input().split())
        if mission == 'I':
            heapq.heappush(min_heap,int(mis_num))
            heapq.heappush(max_heap,-(int(mis_num)))
            plus += 1
        elif mission == 'D':
            if plus > 0:
                if int(mis_num) == -1:
                    heapq.heappop(min_heap)
                    plus -= 1
                else:
                    heapq.heappop(max_heap)
                    plus -= 1
            else:
                continue
    
    if plus > 0:
        min = heapq.heappop(min_heap)
        max = heapq.heappop(max_heap)
        print(-(max),min)
    else:
        print("EMPTY")