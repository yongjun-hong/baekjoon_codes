num = int(input()) # 반복할 횟수값을 저장하는 변수
result = []
for i in range(num):
    a,b = map(int,input().split()) # 좌표 입력
    result.append((a,b))
result = sorted(result)
for i in range(len(result)):
    print(result[i][0],result[i][1])