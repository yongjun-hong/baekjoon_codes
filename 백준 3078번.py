import sys
from collections import deque
input = sys.stdin.readline
friends, gap = map(int,input().split())
friends_length = []
freineds_list = deque([])
alpha = [0] * 21
result = 0
for _ in range(friends):
    friends_length.append(len(input().strip()))
for i in friends_length:
    alpha[i] += 1
    freineds_list.append(i)
    if len(freineds_list) > gap + 1:
        pop_friend = freineds_list.popleft()
        alpha[pop_friend] -= 1
    result += (alpha[i] -1)
print(result)
