N,K = map(int,input().split())
def NoJosep(n,k):
    people_list = []
    josep_list = []
    remove_index = 0
    for i in range(1,n+1):
        people_list.append(i)
    while len(people_list) > 0:
        remove_index += k-1
        remove_index %= len(people_list)
        josep_list.append(str(people_list.pop(remove_index)))
    return josep_list

josep_list = NoJosep(N,K)
print("<%s>" %(", ".join(map(str,josep_list))))