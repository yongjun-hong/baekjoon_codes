# import sys
# input = sys.stdin.readline
# num, max_height = map(int,input().split())
# thing = []
# for i in range(num):
#     thing.append(list(map(int,input().split())))
# print(thing)

# def junseo(max,thing):
#     for i in range(len(thing)):

n, k = map(int, input().split())  # n: 물품의 수, k: 가방에 넣을 수 있는 최대 무게
dp = [[0] * (k+1) for _ in range(n+1)]
m = [[0, 0]]
for i in range(n):
    w, v = map(int, input().split())  # w: 각 물건의 무게, v: 물건의 가치
    m.append([w, v])

for i in range(1, n+1):
    w = m[i][0] # 무게
    v = m[i][1] # 가치
    for j in range(1, k+1):
        if j < w: #현재 배낭의 허용무게보다 물건의 무게가 더 높다면 넣지 않는다.
            dp[i][j] = dp[i-1][j] 
        else: #아니라면 더 가치있는것을 남긴다.
            dp[i][j] = max(dp[i-1][j-w] + v, dp[i-1][j]) 
print(dp[n][k])

# import sys
# read = sys.stdin.readline

# N, K = map(int, read().split())
# cache = [0] * (K+1)

# for _ in range(N):
#     w, v = map(int, read().split())
#     for j in range(K, w-1, -1):
#         cache[j] = max(cache[j], cache[j-w] + v)
# print(cache)