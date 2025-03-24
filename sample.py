"""string methods"""
""" string is  a sequence of characters  ,it is  immutable , 
strings can defined using 
 single quotations
 double quotations
 triple quotations
 string supports indexing and slicing"""


# string="My name is  Mahendra"

# print(string.upper())
#
# print(string.lower())

"""it removes ay leading and trailing spaces of the string"""
# print(string.strip())

# print(string.replace("My","yes"))

# print(string.split())

"""find method returns the index of first occurence of the specified substring  """
# print(string.find("name"))

"""count returns the no of occurences of a substring"""
# print(string.count("name"))

# print(string.capitalize())

# print(string.title())

# print(string.startswith("My"))

# print(string.endswith("Mahendra"))


# print(string.isalpha())

# print(string.isdigit())

# print(string.isalnum())

# print(string.islower())
#
# print(string.isupper())

# print(string.swapcase())

# print(string.center(20))

# print(string.isspace())

# print(string.ljust(100))
#
# print(string.rjust(100))



""""""




"""list is ordered ,collection of items,it is mutable,
it supports indexing and slicing 
it allows duplicates
we can modify a list after creation"""



"""methods of list"""
# list=[1,2,3,4]
# list.append(6)
# print(list)
#
# list.extend([1,2,3])
# print(list)
#
# list.insert(5,99)
# print(list)
#
# list.remove(4)
# print(list)

# list.reverse()
# print(list)
#
# list.copy()
# print(list)
#
# list.pop()
# print(list)
#
#
# list.sort()
# print(list)

# list2=list.count(2)
# print(list2)

# list.clear()
# print(list)

# index_3=list.index(3)
# print(index_3)

# list.insert(2,99)
# print(list)

# print(max(list))
#
# print(min(list))
#
#
# print(sum(list))



"""list comprehension"""

# squares=[x**2 for x in range(5)]
# print(squares)



"""tuple methods"""

# tuple=(1,2,3,4,2,3,3,3,5)


"""it returns the no of occurences of the value"""
# print(tuple.count(3))

"""it returns the index of the value"""

# print(tuple.index(5))

"""dictionary methods"""



"""dictionary comprehension"""

"""it is a concise way to create dictionary"""
# squares={x:x**2 for x in range(7)}
# print(squares)




"""set methods"""

""""""

"""set comprehensions"""

# squares={x**2 for x in range(5)}
# print(squares)


"""iterator"""

"""iterator is a special type of object in python that enables you to access elements of a collection one at a time"""

# numbers=[1,2,3,4,5,6,7]
#
# iterator=iter(numbers)
"""ACCESS elements one by one"""
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))


"""An iterator is a special type of object in Python that enables you to access elements of a collection one at a time. ."""

"""Examples of collections are lists, tuples, dictionaries, sets, strings, etc."""

"""---iterators are used for lazy evaluation"""

"""---common iterable objects like list,tuple,and dictionaries  can be converted to iterators using the iter() function"""

# Example of an iterator in Python

# A simple list
# numbers = [1, 2, 3, 4, 5]

# Get the iterator object
# numbers_iterator = iter(numbers)

# Access elements one by one using next()
# print(next(numbers_iterator))  # Output: 1
# print(next(numbers_iterator))  # Output: 2
# print(next(numbers_iterator))  # Output: 3
# print(next(numbers_iterator))  # Output: 4
# print(next(numbers_iterator))  # Output: 5

# If we call next() again, it will raise StopIteration
# print(next(numbers_iterator))  # Uncomment to see the exception


"""conditional statements ,,if ,elif,else"""




"""for loop"""

"""while loop"""

"""functions"""
"""function is a block of organised and reusable code that performs a specific task
functions break complex code into smaller,manageable parts
function is defined by using def keyword.
"""
# def greet(name):
#     return f"Hello, {name}!"
#
# # Calling the function
# print(greet("Alice"))  # Output: Hello, Alice!

# def greet(name):
#     return f"hello ,{name}"
#
# #calling the function
#
# print(greet("mahendra"))


# def arithmetic_operation(a,b):
#     print(a+b)
#     print(a*b)
#     print(a%b)
#     print(a/b)
#     print(a==b)
#
# arithmetic_operation(5,3)


# def say_hello():
#     print("welcome to python learning")
#
# say_hello()


"""function with parameters"""

# def square(number):
#     print(number*number)
#
# result=square(10)
#

# def square(number):
#     return number+number
#
# result=square(9)
# print("square of number is:",result)


"""function with default parameters"""

# def greet(name="mahendra"):
#     print(f"hello ,{name}!have a great day")
# greet("shankar")
# greet()

"""function with multiple parameters"""

# def calculate_area(length,width):
#     area=length*width
#     return area
# length=5
# width=4
# area=calculate_area(length,width)
# print(f"the area of rectangle with length {length} and width {width} is: {area}")


# def arithmetic_operations(a,b):
#     sum=a+b
#     mul=a*b
#     div=a/b
#     dif=a-b
#     return sum,mul,div,dif
# a,b=10,5
# results=arithmetic_operations(a,b)
# print(f"sum:{results[0]},mul:{results[1]},div:{results[2]},dif:{results[3]}")

# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial (n-1)
# print(factorial(5))

"""lambda"""


"""map with lambda"""


"""filter with lambda"""


"""reduce with lambda"""


"""generator"""


"""decorator"""


""" oops"""

"""class"""

"""---class is a blueprint/plan",,it defines  how an object will look and behave"""
"""---object is created by a blueprint of a class"""

"""Attributes are variables that belong to an object. They define the state or properties of an object."""

"""Methods are functions defined within a class that operate on its attributes. They define the behavior of the objects."""

#   define a class


# class dog:
#
# # constructor to initialize the attributes
#     def __init__(self,name,breed):
#         self.name=name
#         self.breed=breed
#
# #     method to display dog's info
#     def bark(self):
#         print(f"{self.name}, the {self.breed} ,says woof!")
#
# # accessing attributes and calling methods
# dog1=dog("steet dog","indian")
# dog2=dog("german shephard","germany")
#

#
# print(dog1.name)
# print(dog2.breed)
#
# dog1.bark()
# dog2.bark()


"""exception handling"""

"""file handling"""




""""""
# list1=["ia","ma"]
# list2=["m","hendra"]
# list4=' '.join(list1+list2)
# print(list4)
#
# list1 = ["ia", "ma"]
# list2 = ["m", "hendra"]
#
# # Directly concatenate the corresponding elements from both lists
# result = list1[0] + list2[0] + ' ' + list1[1] + list2[1]
#
# print(result)  # Output: "iam mahendra"

#
# list1 = ["Hello", "Good", "How", "Are", "You", "Doing", "Today", "I", "Hope", "Everything"]
# list2 = ["John", "Alice", "Bob", "Charlie", "Sarah", "James", "Emily", "Michael", "David", "Anna"]
#
# # Concatenate corresponding strings using a loop
# result = ' '.join([list1[i] + ' ' + list2[i] for i in range(10)])
#
# print(result)


# name=['na','mahe']
# names=['me','ndra']
# result=' '.join([name[i]+''+names[i] for i in range(2)])
# print(result)


# list1 = ["Hello", "Good", "How", "Are", "You", "Doing", "Today", "I", "Hope", "Everything"]
# list2 = ["John", "Alice", "Bob", "Charlie", "Sarah", "James", "Emily", "Michael", "David", "Anna"]
#
# # Use zip to pair elements from both lists and concatenate them
# result = ' '.join([a + ' ' + b for a, b in zip(list1, list2)])
#
# print(result)


# list1=['m','na','i','mahe']
# list2=['y','me','s','ndra']
# result=' '.join([a+b for a,b in zip(list1,list2)])
# print(result)


# list1=[1,2,3,6,8,9,10,1,25]
# list2=[36,5,6,9,65,8,9,6,6]
# result=[a+b for a,b in zip(list1,list2)]
# print(result)


# list1 = [1, 2, 3, 6, 8, 9, 10, 1, 25]
# list2 = [36, 5, 6, 9, 65, 8, 9, 6, 6]
#
# result = []
# for i in range(len(list1)):
#     result.append(list1[i] + list2[i])
#
# print(result)


# list1=[1,2,3,4,5,6,7,8,9]
# list2=[9,8,7,6,5,4,3,2,1]
#
# result=[]
# for i in range(len(list1)):
#     result.append(list1[i]+list2[i])
# print(result)


"""practise"""

# list=[1,2,3,4,5,6,8,9]
# print(list[1:3])

# print(list[:3])

# print(list[2:])

# print(list[-3:])

"""step -------skipping one value """
# print(list[::2])


"""reverse the entire list"""
# print(list[::-1])

# print(list[2:-2])

# list[2:3]=[77,99]
# print(list)

"""select the entire list"""
# print(list[::])

"""reverse the entire list"""
# print(list[::-1])
"""from index 8 by skipping one value from reverse side"""
# print(list[8:1:-1])
"""reverse every second element """
# print(list[::-2])




# liss=[1,2,3,4,5,6,7,8,9]
# lisss=['a','b','c','d','e','f','g','h']
# result=[str(x)+y for x,y in zip(liss[::2],lisss[::2])]
# print(result)



# listt=[10,20,30,40,50,60,70]
# listtt=[1,2,3,4,5,6,7]
# result=[x+y for x,y in zip(listt,listtt)]
# print(result)
# result1=[x-y for x,y in zip(listt,listtt)]
# print(result1)

# result2=[x*y  for x,y in zip(listt,listtt)]
# print(result2)
#
# result3=[x/y for x,y in zip(listt,listtt)]
# print(result3)


# list1=[1,2,3,4,5,6,7]
# result=["even" if x%2==0 else "odd" for x in list1]
# print(result)



# list2d=[[1,2,3],[4,5,6]]
# result=[item for sublist in list2d for item in sublist]
# print(result)


# listt=[[1,2,3,4,5,6],['name','raju']]
# result=[item for sublist in listt for item in sublist]
# print(result)

# t1=[1,2,3,4,5]
# t2=['a','b','c','d','e']
# result=[(x,y) for x,y in zip(t1,t2)]
# print(result)

# tt=(1,2,3,4,5)
# ttt=('a','b','c','d','f')
# result=[[x,y] for x,y in zip(tt,ttt)]
# print(result)

# dict1=[1,2,3,4]
# dict2=['mahendra','raju','krishna','venkat']
# result={x:{x,y} for x,y in zip(dict1,dict2)}
# print(result)

# result={x:y for x,y in zip(dict1,dict2)}
# print(result)


# numbers=[1,2,3,4]
# names=['sanjana','danusri','devi']
# result={num:name for num,name in zip(numbers,names)}
# print(result)

# numbers=[1,2,3,4,5,6,7,8]`
# names=['sanjana','dhanu','de`vi','raju','krishna','venkat']

# result={num:name for num,name in zip(numbers,names) if num%2==0 }
# print(result)

# resultt={num:name for num,name in zip(numbers,names) if len(name)>5}
# print(resultt)

# num1=[1,2,3,4,5]
# num2=[10,20,30,40,50]
#
# resultt={x:y for x,y in zip(num1,num2) if x%2==1 }
# print(resultt)


# keys=['a','b','c']
# result={key:0 for key in keys}
# print(result)


# keys=['a','b','c']
# result={key:0 for key in keys}
# print(result)



# numbers=[1,2,3,4,5]
#
# result={num:('even' if num%2==0 else 'odd') for num in numbers}
# print(result)


# num=[1,2,3,4,5,6]
# result={num:('even' if num%2==0 else 'odd')for num in num}
# print(result)


# student=['mahendra','raju','vennkat']
# score=[85,90,95]
# result={students:scores for students,scores in zip(student,score)}
# print(result)



"""advance list comprehensions"""

# numbers=[1,2,3,4,5,6]
# result=[x for x in numbers if x%2==0 and x>5 ]
# print(result)
#
# even_largest=[x for x in range(20) if x%2==1 and x>10]
# print(even_largest)

# numbers = [1, 2, 3]
# letters = ['a', 'b', 'c']
# result = [(num, letter) for num, letter in zip(numbers, letters)]
# print(result)

#
# class Animal:
#     def __init__(self,name,sound):
#         self.name=name
#         self.sound=sound
#
#     def speak(self):
#         print(f"{self.name} says {self.sound}")
#
#
# class Dog (Animal):
#     def __init__(self,name,sound,breed):
#         super().__init__(name,sound)
#         self.breed=breed
#
#
#     def display_breed(self):
#         print(f"{self.name} is a {self.breed} breed")
#
# dog=Dog("Rex","woof","german shepherd")
#
# dog.speak()
# dog.display_breed()



# class car:
#     def __init__(self,make,model,year):
#         self.make=make
#         self.model=model
#         self.year=year
#
#         # method to display information about the car
#     def display_info(self):
#         print(f"car :{self.year} {self.make} {self.model}")
#
# my_car=car("toyota","corolla",2020)
#
# my_car.display_info()

"""1/1/2025"""
"""multithreading is programming concept """