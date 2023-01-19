import sys
input = sys.stdin.readline

num_house,router = map(int,input().split())
house = []
for _ in range(num_house):
    house.append(int(input()))
house.sort()
def binary_search(start,end,house,router):
    while start <= end:
        count = 1
        mid = (start + end) // 2
        front_house = house[0]
        for i in range(1,len(house)):
            if house[i] >= front_house + mid:
                count += 1
                front_house = house[i]
        if count >= router:
            start = mid + 1
            global result
            result = mid
        else:
            end = mid-1
start = 1
end = house[-1] - house[0]
binary_search(start,end,house,router)
print(result)
        

