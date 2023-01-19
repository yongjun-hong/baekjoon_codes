# print ("구구단 몇 단을 계산할까요(1~9)?")
# x = 1
# while (True):
#     x = int(input())
#     if x == 0: break
#     if not(1 <= x <= 9):
#         print ("잘못 입력하셨습니다", "1부터 9사이 숫자를 입력해주세요")
#         continue
#     else:
#         print ("구구단 " + str(x) +"단을 계산합니다.")
#         for i in range(1,10):
#             print (str(x) + " X " + str(i) + " = " + str(x*i))
#         print ("구구단 몇 단을 계산할까요(1~9)?")
# print ("구구단 게임을 종료합니다")
def addition(x, y):
    return x+y
def multiplication(x, y):
    return x*y
def divided_by_2(x):
    return x/2
if __name__ == '__main__':
    print(addition(10,5))
    print(multiplication(10,5))
    print(divided_by_2(50))