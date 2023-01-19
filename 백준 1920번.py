import sys
input = sys.stdin.readline

num_1 = int(input())   
input_list = list(map(int,input().split()))

num_2 = int(input())
find_list = list(map(int,input().split()))

input_list.sort()
def binary_search(start,end,data,target):
    while start <= end:
        mid = (start + end)//2
        if data[mid] == target:
            return 1
        elif data[mid] > target:
            end = mid - 1
        elif data[mid] < target:
            start = mid + 1
    return 0
for i in find_list:
    if binary_search(0,(num_1-1),input_list,i) == 1:
        print('1')
    else:
        print('0')