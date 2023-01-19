#1
# num_list = [1,5,7,15,16,22,28,29]
# def get_odd_num(num_list):
#     result_list = []
#     for i in num_list:
#         if i % 2 == 1:
#             result_list.append(i)
#     return result_list
# print(get_odd_num(num_list))
# 주어진 리스트
# num_list = [1, 5, 7, 15, 16, 22, 28, 29]

# def get_odd_num(num_list):
#     # TODO
#     result=[]
#     for n in num_list:
#         if n % 2 == 1:
#             result.append(n)
#     return result
        
        
# print(get_odd_num(num_list))
#2
# sentence = "way a is there will a is there where"
# def reverse_sentence(sentence):
#     result = str.split(sentence,' ')
#     result = result[::-1]
#     return result
# print(' '.join(reverse_sentence(sentence)))

#3
# score = [(100,100),(95,90),(55,60),(75,80),(70,70)]
# def get_avg(score):
#     score_list = []
#     for i in score:
#         average_term = 0
#         average_term = average_term + i[0] + i[1]
#         average_term /= 2
#         score_list.append(average_term)
#     return score_list
# result_list = get_avg(score)
# for i in range(len(result_list)):
#     print(i+1,"번, 평균:",result_list[i])

#4
# dict_first = {'사과':30,'배':15,'감':10,'포도':10}
# dict_second = {'사과':5,'감':25,'배':15,'귤':25}
# def merge_dict(dict_first,dict_second):
#     result_dict = {}
#     result_dict['감'] = dict_first['감'] + dict_second['감']
#     result_dict['귤'] = dict_second['귤']
#     result_dict['배'] = dict_first['배'] + dict_second['배']
#     result_dict['사과'] = dict_first['사과'] + dict_second['사과']
#     result_dict['포도'] = dict_first['포도']
#     return result_dict
# print(merge_dict(dict_first,dict_second))

#5
# import re
# inputs = "cat32dog16cow5"
# def find_string(inputs):
#     newstring = re.sub(r'[0-9]+', ' ', inputs)
#     return newstring
# string_list = find_string(inputs)
# print(string_list)

    
# inputs = "cat32dog16cow5"
# def find_string(inputs):
#     result_string = []
#     result_string.append(inputs[0:3])
#     result_string.append(inputs[5:8])
#     result_string.append(inputs[10:13])
#     return result_string
# print(find_string(inputs))

ex = [1,2,3,4,5]
print(list(map(lambda x: x+x, ex)))
# print((map(lambda x: x+x, ex)))
# f = lambda x: x ** 2
# # print(map(f, ex))
# for i in map(f, ex):
#     print(i)    