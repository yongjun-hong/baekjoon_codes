import sys
from collections import deque
input = sys.stdin.readline
num = int(input())

for i in range(num):
    pure_number = []
    reverse = 0
    error = 0
    mission = input()
    mis_num = int(input())
    pure_number = deque(input().rstrip()[1:-1].split(","))
    if mis_num == 0:
        pure_number = deque()

    for e in range(len(mission)):
        if mission[e] == "R":
            reverse += 1
        elif mission[e] == "D":
            if len(pure_number) > 0:
                if reverse % 2 == 1:
                    pure_number.pop()
                else:
                    pure_number.popleft()
            else:
                print("error")
                error += 1
                break
    if error == 0:
        if reverse % 2 == 1:
            pure_number.reverse()
            print('['+','.join(pure_number)+']')
        else:
            print('['+','.join(pure_number)+']')