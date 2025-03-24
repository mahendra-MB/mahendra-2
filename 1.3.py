
"""remove duplicates"""


# l=[1,2,2,3,4,5,5,6,6,7]
#
# re_dupli=[]
#
# for i in l:
#     if i not in re_dupli:
#         re_dupli.append(i)
#
# print(re_dupli)

"""length of strings"""

# strings=['okay','always','trying','good-idea','we-achieve-best']
# length=[]
#
# for string in strings:
#     length.append(len(string))
# print(length)

"""2nd largest string"""
# strings=['okay','always','trying','good-idea','we-achieve-best']
#
# sorted=sorted(strings,key=len,reverse=True)
#
# second_largest=sorted[1]
#

# print(second_largest)

"""2nd largest string sorting function"""

# strings=['okay','always','trying','we-achieve-best','good-idea']
#
# largest=""
# second_largest=""
# #
# for i in strings:
#     if len(i)>len(largest):
#         second_largest=largest
#         largest=i
#     # elif len(i)>len(second_largest) and i!=largest:
#     #     second_largest=i
# print(largest)
# print(second_largest)



"""max value in the list"""

# numbers=[1,2,3,4,5,6]
# largest=max(numbers)
# print(largest)


"""max value in the list"""

# numbers=[1,2,6,4,7,5,8,3]
#
# largest=numbers[3]
#
# for number in numbers:
#     if number > largest:
#         largest=number
# print(largest)

"""max value in the list"""


# numbers=[1,2,3,4,5,6]
#
# largest=numbers[0]
#
# for i in range(1,len(numbers)):
#     if numbers[i]>largest:
#         largest=numbers[i]
# print(largest)

# numbers=[1,2,3,4,5,6]
# largest=numbers[0]
#
# for i in numbers:
#     if i >largest:
#         largest=i
# print(largest)


"""largest string"""

# strings=['one','twenty two','three','eleven']
#
# largest=""
#
# for string in strings:
#     if len(string)>len(largest):
#         largest=string
# print(largest)


# print(ord("a"),chr(45))

# s= ["aaaaabc","ac","b","","gjf"]
# print(sorted(s,key=len)[-2])

""""""

# s= [[10,1],[4,2],[3,12],[8,0]]
# print(sorted(s,key=sum))
# print(sorted(s,key= lambda x:x[0]))
# print(sorted(s))



# output [[8,0],[10,1],[4,2]]
