import sys
import heapq
input = sys.stdin.readline

str_list = []
num = int(input())
for _ in range(num):
    str_input = input()
    str_list.append((len(str_input),str_input))
str_list.sort()
    # heapq.heappush(str_list,(len(str_input),str_input))
result_list = []
result_list.append(str_list[0][1])
for i in range(1,num):
    if str_list[i][1] == str_list[i-1][1]:
        continue
    else:
        result_list.append(str_list[i][1])
for i in range(len(result_list)):
    print(result_list[i],end='')