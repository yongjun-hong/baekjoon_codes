import sys

n = int(input())
card = list(map(int, sys.stdin.readline().split()))
card.sort()
m = int(input())
check = list(map(int, sys.stdin.readline().split()))

def binary_search(target,data,start,end):

    while(start <= end):
        mid = (start + end)//2
        if data[mid] == target:
            return 1
        elif data[mid] < target:
            start = mid + 1
        else:     
            end = mid-1
    return 0

for i in range(m):
    print(binary_search(check[i],card,0,n-1),end=' ')

