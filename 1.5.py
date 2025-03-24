""""""

"""5/01/2025"""
"""dictionary methods"""

# my_dict={"name":"mahendra","age":25,"city":"kakinada"}
# print(my_dict.keys())

# print(my_dict.values())

# print(my_dict.items())

# my_dict.update({"country":"india"})
# print(my_dict)

# my_dict.pop('age')
# print(my_dict)

# my_dict.popitem()
# print(my_dict)

# my_dict.setdefault("gender","male")
# print(my_dict)

# my_dict.clear()
# print(my_dict)

# my_dict.copy()
# print(my_dict.copy())

# my_dict=["name","age","city"]
# my_dict1=dict.fromkeys(my_dict,'known')
# print(my_dict1)


# my_dict={'name':"mahendra","age":25,"city":"kakinada"}
# my_dict["location"]=my_dict.pop("city")
# print(my_dict)


# my_dict["city"]="rajamahendravaram"
# print(my_dict)

# del my_dict['city']
# my_dict["country"]='india'
# print(my_dict)



# l=[0,1,2,2,3,4,5,6,6,7,8,8]
#
# dd=[]
#
# for i in l:
#     if i not in dd:
#         dd.append(i)
# print(dd)


# string=["one",'five','seven','twenty-one','hundred']
#
# largest=''
# second_largest=''
#
# for i in string:
#     if len(i)>len(largest):
#         second_largest=largest
#         largest=i
#
#     elif len(i)>len(second_largest) and len(i)!=len(largest):
#         second_largest=i
# print(largest)
# print(second_largest)


"""max value in list"""

# numbers=[1,5,4,3,2]
#
# max_value=numbers[0]
#
# for i in numbers:
#     if i >max_value:
#         max_value=i
# print(max_value)


"""based on index 1 sort nested list """
# nested_list=[[10,1],[5,2],[7,5],[2,0]]
# sort=sorted(nested_list,key=lambda x:x[1])
# print(sort)


"""fibonacci sequence"""

# limit=10
# a,b=0,1
# print("fibonacci sequence")
# for i in range(limit):
#     print(a)
#     a,b=b,a+b

"""pattern"""
# rows=6
# for i in range(1,rows):
#     print(i*"*")

# for i in range(rows-1,0,-1):
#     print(i*'*')

# for i in range(1,rows):
#     print(' '*(rows-i)+"*"*(2*i-1))

# for i in range(rows-1,0,-1):
#     print(' '*(rows-i)+"*"*(2*i-1))
#     print(' '*(rows-1)+'*')

# for i in range(1,rows):
#     print(' '*(rows-i)+"*"*(2*i-1))
#     print(' '*(rows-1)+"*")


"""armstrong number ---- 153,370,371,9474   """

# armstrong_number=153

# digits=str(armstrong_number)
# n=len((digits))
# total=0
# for digit in digits:
#     total+=int(digit)**n
# if total==armstrong_number:
#  print("number is armstrong_number")
# else:
#     print("number is not armstrong_number")

# orders=['order1','order2','order3']
# orders.append('order4')
# print(orders)


# tasks=['task1','task2']
# tasks.extend(['task3','task4'])
# print(tasks)


# taskss=['task1','task2','task3']
# taskss.insert(2,'final task')
# print(taskss)

"""def"""

# def say_hello():
#     print("hello world")
# say_hello()

'''train me to do real time projects on python ,
give everything real time examples to master the python
from today onwards also to crack interview ,, 
first start with  '''

# inventory = {
#     "item1": 10,
#     "item2": 5,
#     "item3": 8
# }
#
# # Display the inventory
# for item, quantity in inventory.items():
#     print(f"{item}: {quantity} units")
#
# # Calculate total stock
# total_stock = 0
# for quantity in inventory.values():
#     total_stock += quantity
#
# print(f"Total stock: {total_stock} units")


# students = {
#     "John": [85, 90, 78],
#     "Alice": [92, 88, 91],
#     "Bob": [79, 85, 88]
# }
#
# for student, grades in students.items():
#     average_grade = sum(grades) / len(grades)
#     print(f"{student}'s average grade: {average_grade}")

# start,end=10,50
#
# for num in range(start,end+1):
#     is_prime=True
#     for i in range(2,num):
#         if num%i==0:
#             is_prime=False
#             break
#     if is_prime:
#         print("primes:",num)



# number=10
# if number >19:
#     print("number is big")
# elif number <11:
#     print("number is less")

