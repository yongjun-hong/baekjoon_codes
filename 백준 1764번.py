import sys
import numpy as np
input = sys.stdin.readline
hear, see = map(int,input().split())
hear_list = []
see_list = []
for i in range(hear):
    a = input()
    hear_list.append(a)
for i in range(see):
    a = input()
    see_list.append(a)
hear_list.sort()

def binary_search(start,end,data,target):
    while start <= end:
        mid = (start + end)//2
        if data[mid] == target:
            return target
        elif target > data[mid]:
            start = mid + 1
        else:
            end = mid-1
    return None
result_list = []
for i in see_list:
    if binary_search(0,hear-1,hear_list,i) is not None:
        result_list.append(i)

result_list.sort()
print(len(result_list))
for i in result_list:
    print(i,end="")