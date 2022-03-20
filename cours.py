from time import sleep
from client import run_client


def add(a,b):
    print(a+b)
    return
while True:
    run_client('en','go')
    sleep(3)

# # numbers = list()
# # for i in range(11):
# #     numbers.append(i)
# # numbers = [n for n in numbers if n%2 == 0]
# # print(numbers)
# # print((lambda x : x+2)(2))

# # age = int(input('Enter your age please'))
# # print('Votre age est %s'%age)
# #If statements
# import re
# from typing import Dict



# def fib(n):
# 	if n==1:
# 		return 1
# 	elif n==2:
# 		return 1
# 	else:
# 		return fib(n-1) + fib(n-2)
# def print_stars(N):
#     num = ''
#     for i in range(N):
#         num = num + '*'
#         print(num)
# if __name__ == '__main__':
# 	print(fib(10))
# print_stars(6)
# #built in data structures 10th March 2022
# #lists dictionaries sets tuples
# l = list()
# for i in range(1,21,2):
#     l.append(i)
# print(l)
# print('abcde fghij klmno pqrst uvwx yz'.split())
# d = dict()
# data = {
# 	"name":"Smauel Boateng",
#     "age":22,
#     "school":"ENSA-Marrakech"
# }
# d = data.copy()
# d.update(age=12,school='ENSA-Agadir')
# print(d)
# pattern = r'\bSamuel\b'
# me = 'Samuel'
# print(me)
# [5,3,5,6,8,45,2,0]
# s = lambda x:x
# print(dict())
# for i in range(1,21):
#     N = 7 * i
#     if N % 3 != 0:
#         print('*',end=' ')
#     else:
#         print(N,end='')
# t = (1,2,3,4,56,'',7,8,8)
# modifiedTuple = list(t)
# print(modifiedTuple)
# for i in t:
#     print(i)
# dict_of_list = {
# 	"towns":['Rabat','MArrakech','Casablanca','Meknes','Fez','Agadir',''],
#  "coodinates":[]
# }
# print(dict_of_list["towns"][5])
# A = {1,2,3,4,5,6,7,8,9,10}
# B = {4,5,6,7}
# print(A.issuperset(B))
# print(B.issubset(A))
# print(A.intersection(B))
# print(A.difference(B))
# print(B.difference(A))
# print(set())
# if set('abc'):
#     print('Yes')
# else:
#     print('No')

# print(dict({"name":'sam'}))
# import os,sys
# i = 0
# while True:
#     print('Not done')
#     i = i+1
#     if i == 500:
#         print(i)
#         sys.exit()
# import math
# import re
# pattern = r'Rabiaa'
# name = 'rabiaa:Boudribila'
# print(re.sub(pattern,'cutie',name))
# print("Rabiaa\t\t\t\t\t\t\t\t\t\t\t\t\tBou")
# res = name.split(':')
# print(res)
# print(":".join(res))
# d = {}
# d['name'] = 'Rabiaa'
# d['age'] = 23
# print(d)
# print(d.items())
# print(d.keys())
# print(d.values())
# def add(a,b):
#     return a+b
# def afficher_list(l):
#     for i in l:
#         print(i,end='\n')
# afficher_list([1,2,3,4,5])



        
        
