fibo = []
def fibonacci(end):
    for i in range(end+1):
        if i == 0:
            num = 0
        elif i == 1 or i == 2:
            num = 1
        else:
            num = fibo[-1] + fibo[-2]
        fibo.append(num)
    
num1 = int(input())
fibonacci(num1)
print(fibo[-1])
