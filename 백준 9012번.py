import sys
input = sys.stdin.readline
def stack(data):
    stack_list = []
    for i in range(len(data)):
        if data[i] == '(':
            stack_list.append('(')
        else:
            if len(stack_list) > 0:
                stack_list.remove('(')
            else:
                return "NO"
    if len(stack_list) > 0:
        return 'NO'
    else:
        return 'YES'


num = int(input())
for _ in range(num):
    data = list(input())
    data.remove('\n')
    print(stack(data))

