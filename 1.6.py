
"""6/1/2025"""

inventory=['apples','bananas','cherries']

# inventory.append('oranges')
# print(inventory)

# inventory.extend(['grapes','guavas'])
# print(inventory)

# inventory.insert(1,'staberries')
# print(inventory)

# inventory.remove('bananas')
# print(inventory)

# inventory.clear()
# print(inventory)

# inventory.copy()
# print(inventory)

# inventory.pop()
# print(inventory)

# inn=inventory.index('bananas')
# print(inn)

# inven=inventory.count('bananas')
# print(inven)

# inventory.sort()
# print(inventory)

# inventory.reverse()
# print(inventory)

# print(min(inventory))
#
# print(max(inventory))

# numbers=[1,2,3,4,5,6]
# print(sum(numbers))

# def simple_generator():
#     yield 'first yield'
#     yield 'second yield'
#
# gen=simple_generator()
#
# print(next(gen))

# def simple_generator():
#     yield "First Yield"
#     yield "Second Yield"
#
# # Create the generator object
# gen = simple_generator()
#
# # Use a for loop to iterate through the generator
# for value in gen:
#     print(value)


"""generator"""
# def simple_generator():
#     yield 1
#     yield 2
#
# gen=simple_generator()
# print(next(gen))
# print(next(gen))



"""decorator"""
# def simple_decorator(func):
#     def wrapper():
#         print("before")
#         func()
#         print("after")
#     return wrapper
# @simple_decorator
# def decorator():
#     print("function")
# decorator()

# def simple_decorator(func):
#     def wrapper():
#         print("before function execution")
#         func()
#         print("after function execution")
#     return wrapper
# @simple_decorator
# def say_hello():
#     print("hello world")
# say_hello()


"""string methods"""

# name='Quick tech technologies'

# print(name.upper())
# print(name.lower())

# print(name.strip())

# print(name.replace('Quick','andhra'))
#
# print(name.split())

# word=s=['python','is','easy']
#
# print(' '.join(word))

# print(name.find('Quick'))

# print(name.count('Quick'))

# print(name.startswith('Quick'))

# print(name.endswith('technologies'))

# print(name.capitalize())

# print(name.title())

# print(name.isalnum())

# print(name.isalpha())

# print(name.isdigit())

# print(name.isupper())

# print(name.isupper())

# print(name.swapcase())

# print(name.center(35))


"""tuple methods"""

# tuplee=('one','one','two')

# print(tuplee.count('one'))

# print(tuplee.index('one'))

"""swapping values"""

# a=10
# b=5
#
# a,b =b,a
#
# print(a,b)

"""list comprehensions"""
# squares=[x**2 for x in range(10)]
# print(squares)

"""dictionary comprehension"""
# square_dict={x:x**2 for x in range(5)}
# print(square_dict)


"""zip to combine lists"""
# names=['narendra','raju','loknath']
# scores=[95,90,87]
#
# print(dict(zip(names,scores)))

"""asterisks"""
# a,*b,c=[1,2,3,4,5]
#

# print('a:',a)
# print('b:',b)
# print('c:',c)



"""basic functionalities of int"""

x=10
y=int("20")   # converts string to integer
z=int(3.14)   #converts float to integer (truncates decimal part)

"""mathematical operations"""

a=5+3     #addition
b=10-2    #subtraction
c=4*7     #multiplication
d=10/2    #division (result is float)
e=10//3   #floor division (result is integer)
f=2**3    #exponentiation
g=10%3    #modulus (remainder)


"""comparison operators"""
x,y=5,10

# print(x==y)    # equality
# print(x!=y)    # not equal
# print(x<y)     #less than
# print(x>y)     # greater than
# print(x <=y)   # less than or equal to
# print(x >=y)   #greater than or equal to


"""bitwise operators"""
a = 5&3     #and
print(a)
b = 5|3     #OR
print(b)
c = 5^3     #NOR
print(c)
d = ~5      #NOT
print(d)
e = 5<<1    #left shift
print(e)
f = 5>>1    #Right shift
print(f)

# x=10
# print(x.bit_length())

# print(x.is_integer())


# x=255
# print(format(x,'x'))
# print(format(x,'b'))

