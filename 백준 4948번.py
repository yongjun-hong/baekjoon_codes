import sys,math,time
input = sys.stdin.readline
# start = time.time()
prime_number_true = [False,False]+[True] * 270000
for i in range(2,int(math.sqrt(270000))):
    if prime_number_true[i] == True:
        for e in range(i*2,270000,i):
            prime_number_true[e] = False

while True:
    num = int(input())
    if num == 0:
        break
    else:
        count = 0
        for i in range(num + 1,(num * 2)+1):
            if prime_number_true[i] == True:
                count += 1
    print(count)
    # end = time.time()
    # print(f"{end - start:.5f} sec")