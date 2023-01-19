import sys

input = sys.stdin.readline
mission_num = int(input())
result_list = []
q_front = 0
q_rear = 0
for i in range(mission_num):
    mission = input().split()
    if mission[0] == "push":
        result_list.append(mission[1])
        q_front += 1
    elif mission[0] == "front":
        if q_front != q_rear:
            print(result_list[q_rear])
        else:
            print("-1")
    elif mission[0] == "back":
        if q_front != q_rear:
            print(result_list[-1])
        else:
            print("-1")
    elif mission[0] == "pop":
        if q_front > q_rear:
            print(result_list[q_rear])
            q_rear += 1
        else:
            print("-1")
    elif mission[0] == "empty":
        if q_front != q_rear:
            print("0")
        else:
            print("1")
    elif mission[0] == "size":
        print(q_front - q_rear)



