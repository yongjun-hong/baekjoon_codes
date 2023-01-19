import sys
num = int(sys.stdin.readline())

for i in range(num):
    string = sys.stdin.readline().strip().split()
    for word in string:
        print(word[::-1],end=" ")