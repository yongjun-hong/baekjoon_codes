import sys
import heapq
input = sys.stdin.readline

num = int(input())
time = []
for i in range(num):
    time.append(list(map(int,input().split())))
time.sort()

nums_people = []
used_computer = [0] * num
used_computer[0] = 1
com = 0
heapq.heappush(nums_people,(time[0][1],0))
for i in range(1,num):
    if nums_people[0][0] > time[i][0]:
        com += 1
        heapq.heappush(nums_people,(time[i][1],com))
        used_computer[com] += 1
    else:
        abc = nums_people[0][1]
        used_computer[abc] += 1
        heapq.heappop(nums_people)
        heapq.heappush(nums_people,(time[i][1],abc))
        

print(len(nums_people))
for i in range(len(nums_people)):
    print(used_computer[i],end=' ')