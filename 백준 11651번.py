import sys
input = sys.stdin.readline

result = []
num = int(input())
for i in range(num):
    a,b = map(int,input().split())
    result.append([b,a])
result = sorted(result)
for i in range(len(result)):
    print(result[i][1],result[i][0])
