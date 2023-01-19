import sys
input = sys.stdin.readline

num = int(input())
positive_num = []
negative_num = []
result = 0
for _ in range(num):
    number = int(input())
    if number > 1:
        positive_num.append(number)
    elif number == 1:
        result += 1
    else:
        negative_num.append(number)
positive_num.sort(reverse=True)
negative_num.sort()


if len(positive_num) % 2 == 1:
    for i in range(0,(len(positive_num)//2)):
        first = positive_num.pop(0)
        second = positive_num.pop(0)
        result += first * second
    result += positive_num.pop()
    
else:
    for i in range(0,(len(positive_num)//2)):
        first = positive_num.pop(0)
        second = positive_num.pop(0)
        result += first * second
if len(negative_num) % 2 == 1:
    for i in range(0,(len(negative_num)//2)):
        first = negative_num.pop(0)
        second = negative_num.pop(0)
        result += first * second
    result += negative_num.pop(0)
else:
    for i in range(0,(len(negative_num)//2)):
        first = negative_num.pop(0)
        second = negative_num.pop(0)
        result += first * second
print(result)
        