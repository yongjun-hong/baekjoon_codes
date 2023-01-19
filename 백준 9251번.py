import sys
input = sys.stdin.readline

list1,list2 = input().strip(),input().strip()

len_list1, len_list2 = len(list1),len(list2)
table = [[0] * (len_list2 + 1) for _ in range(len_list1 + 1)]   
for i in range(1,len_list1 + 1):
    for e in range(1,len_list2 + 1):
        if list1[i-1] == list2[e-1]:
            table[i][e] = table[i-1][e-1] + 1
        else:
            table[i][e] = max(table[i][e-1], table[i-1][e])
print(table[-1][-1])
