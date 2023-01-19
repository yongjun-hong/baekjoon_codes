import sys
input = sys.stdin.readline
while True:
    num = list(input())
    num.remove('\n')
    if num[0] == '0':
        break
    else:
        if num[:] == num[::-1]:
            print("yes")
        else:
            print("no")