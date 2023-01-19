import sys
input = sys.stdin.readline

num,minus_num = map(int,input().split())
mission_num = list(input())
stack = []
mis = minus_num
for n in mission_num:
    while stack and n > stack[-1] and mis > 0:
        stack.pop(-1)
        mis -= 1
    stack.append(n)
print(''.join(stack[:num-minus_num]))