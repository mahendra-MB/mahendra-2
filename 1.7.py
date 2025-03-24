""""""

"""replace key """
# my_dict1={'a':1,'b':2,'c':3}
# my_dict1['d']=my_dict1.pop('c')
# print(my_dict1)



"""prime numbers"""

# limit=100
#
# for j in range(2,limit+1):
#     is_prime=True
#     for i in range(2,int(j**.5)+1):
#         if j%i==0:
#             is_prime=False
#             break
#     if is_prime:
#         print(j)
#
# limit=100
#
# for j in range(2,limit+1):
#     is_prime=True
#     for i in range(2,j):
#         if j%i==0:
#             is_prime=False
#             break
#     if is_prime:
#         print(j)


"""dictionary comprehension"""

# squares={x:x**2 for x in range(6)}
# print(squares)

# lists=[1,2,3,4,5,6,7]
# add=list(map(lambda x:x+5,lists))
# print(add)


# lists=[1,2,3,4,5,6,7]
# even=list(map(lambda x:x+10 ,filter(lambda x:x%2==0,lists)))
# print(even)

# lists=[1,2,3,4,5,6,7,8]
# even=[x+10 for x in lists if x%2==0]
# print(even)

# lists=[1,2,3,4,5,6,7,8]
# even=[]

# for x in lists:
#     if x%2==0:
#         even.append(x+10)
# print(even)


# lists=[1,2,3,4,5,6,7,8,9]
# even=[]
#
# for i in lists:
#     if i%2==0:
#         even.append(i*10)
# print(even)



# lists=[1,2,3,4,5,6,7,8,9,20]
#
# even=[]
# i=0
# while i<len(lists):
#     if lists[i]%2==0:
#         even.append(lists[i]+10)
#     i+=1
# print(even)

# def my_funcion(*args,**kwargs):
#     print("args:",args)
#     print("kwargs:",kwargs)
# my_funcion(1,2,3,4,5,name="mahendra",age=25)

# x = 10
# if 5 < x < 20:
#     print("x is between 5 and 20")


# def sum_numbers(*args):
#     return sum(args)
# print(sum_numbers(10,6,7))


# def math_func(a,b,c,d):
#     add=a+b+c+d
#     mul=a*b*c*d
#     return add,mul
# result=math_func(5,7,8,4)
# print(result)


#
# def math_func(a,b,c,d):
#     add=a+b+c+d
#     mul=a*b*c*d
#     print( add,mul)
# math_func(5,7,8,4)



# set=[1,2,3,4,5,6,7,8]
# print(set)


# def math_function(a,b,c,d):
#     add=a+b+c+d
#     mul=a*b*c*d
#     print(f"sum:{add},product:{mul}")
# math_function(5,5,5,5)



import pandas as pd


import os


import pandas as pd


# Load the CSV file into a DataFrame
df = pd.read_csv(r'/csvvv.csv')

# Display the first 5 rows to check the data
# print(df.head())

# print(df.describe())
#

# print(df.isnull().sum())  # This will give the number of missing values per column


# electronics_df = df[df['Product_Category'] == 'Electronics']
# print(electronics_df)

# selected_columns = df[['Product_Name', 'Price']]
# print(selected_columns)

# selected_columns = df[['Quantity', 'Price_per_Unit']]
# print(selected_columns)

# selected_columns  = df['Price'] * 1.1
# print(selected_columns)

# print(df.columns)
#
#
# selected_columns = df[['Quantity', 'Price_per_Unit']]
# print(selected_columns)

# print(df.head())

# print("Total Quantity:", df['Quantity'].sum())
# print("Total Price:", df['Total_Price'].sum())


# low_shipping_cost = df[df['Shipping_Cost'] < 6]
# print(low_shipping_cost)

# max_price = df['Total_Price'].max()
# min_price = df['Total_Price'].min()
# print("Max Price:", max_price)
# print("Min Price:", min_price)

# print("Total Quantity:", df['Quantity'].sum())
# print("Total Price:", df['Total_Price'].sum())

# print(df.describe())

# inventory = []
#
# def add_product(name, price, quantity):
#     inventory.append({"name": name, "price": price, "quantity": quantity})
#
# def remove_product(name):
#     inventory[:] = [product for product in inventory if product["name"] != name]
#
# def display_inventory():
#     for product in inventory:
#         print(f"Product: {product['name']}, Price: {product['price']}, Quantity: {product['quantity']}")
#
# add_product("Laptop", 1500, 10)

# add_product("Phone", 800, 5)
# display_inventory()
#
forecast=[]

def add_forecast(day,temperature,condition):
        forecast.append({"day":day,"temperature":temperature,"condition":condition})

def display_forecast():
        for day in forecast:
                print(f"day:{day['day']}, temperature:{day['temperature']}, condition:{day['condition']}")

add_forecast('monday',28,'sunny')
add_forecast('tuesday',30,'cool')
add_forecast('wednesday',31,'winter')
display_forecast()
