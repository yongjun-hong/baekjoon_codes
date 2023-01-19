import sys
input = sys.stdin.readline
n,m = map(int,input().split())
input_ch = []
search_ch = []
for i in range(n):
    a = input()
    input_ch.append(a)
for i in range(m):
    a = input()
    search_ch.append(a)
input_ch.sort()
def binary_search(start,end,data,target):
    while start <= end:
        mid = (start + end)//2
        if target == data[mid]:
            return 1 
        elif target > data[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 0
result = 0
for i in range(m):
    if binary_search(0,n-1,input_ch,search_ch[i]) == 1:
        result += 1
print(result)
