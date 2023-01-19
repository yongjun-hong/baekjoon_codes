# import sys
# input = sys.stdin.readline
# num = int(input())
# mission_num = list(map(int, input().split()))
# count = 0
# sorted_list = sorted(mission_num)
# for i in mission_num:
#     for e in range(len(mission_num)):
#         if e >= 1:
#             if sorted_list[e] != sorted_list[e-1]:
#                 if i > sorted_list[e]:
#                     count += 1
#         elif e == 0:
#             if i > sorted_list[e]:
#                     count += 1  
#     print(count,end=' ')
#     count = 0
import sys
#보통 input()으로 문자열 값을 입력받지만 반복문으로 여러 줄을 입력받아야 할 때는 시간 초과 문제가 발생할 수 있다고 한다.
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
new_a = sorted(set(a)) #set을 사용하면 중복되지 않은 값을 구할수 있다.
dictionary = {new_a[i] : i for i in range(len(new_a))} #딕셔너리에 '숫자 : new_a에서의 인덱스'로 저장
 
for i in a:                          #기존 a를 돌며
    print(dictionary[i], end = ' ') 
