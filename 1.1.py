"""1/1/2025"""


"""
*******multithreading****************----
is a programming concept that allows a program to execute multiple tasks 
simultaneously using threads .thread is a smallest unit of a program 
that can run independently.it enhances performance and efficiency ,
especially in tasks that can run concurrently.
---it suitable for tasks that are I/O-bound 
____threads are lightweight and have less overhead compared to processes
----overhead refers time,memory or computational power .
"""
"------------------------------------------"


"""
*******multiprocessing******** -------
it is programming technique where a program is  divided  into multiple 
processes that run simultaneously across one or more CPU cores.
-----it is suitable for CPU-bound .
-----processes are more heavyweight than threads but avoid 
the global interpreter lock(GIL) in python.
---tasks run parallely.
"""
"---------------------------------------"

"---------------------------------------"
"""
*******concurrency*****
it refers to the ability of a program to execute multiple tasks or
processes in overlapping time periods.
"""



"-------------------------------------------"
"""
***metadata*****@@@
it refers to  data about data .it provides additional context ,
information about a set of data,helping to describe ,explain ,
or manage it more  efficiently
"""
"---------------------------------------------"

"""
****GLOBAL INTERPRETER LOCK(GIL)******
global interpreter lock is a mechanism used in python (some programming 
languages)  , that allows only one thread to execute python bytecode at 
a time ,even on multi-core systems.this lock is necessary because python 
memory management is not thread-safe.
---it helps avoid issues with memory management in CPython(the standard
 python implementation )

"""

"--------------------------------------------------"


"""
********parallelism******

parallelism is the simultaneous execution of multiple tasks or processors 
to speed up computation. 
in parallelism ,tasks are divided into smaller subtasks and these subtasks
 are executed at the same time on multiple processors  

"""

"-----------------------------------------------------"

"""
*****websocket*******

a websocket is a communication protocol that enables full-duplex,
real-time communication between a client(usually a browser) and a server. 
.it allows continuous ,bidirectional data  exchange without the need to 
repeatedly request updates.primarily used in interactive applications 
that require frequent updates or real-time communication.

--it repeatedly establishing new http connections 

----uses  in
live sport scores
stock trading
chat applications
collaborative tools
time-sensitive applications
"""


"--------------------------------------------------------------"

"""What is Synchronization?
synchronization in computing refers ti=o the coordination of the execution
 of multiple threads or processes to ensure that they operate correctly ands 
 share resources safely.when multiple threads or processes access shared 
 resources  

"""


""" 
**what is data pipeline**
a data pipe line is a series of processes that move data from one system to
 another.it extracts, transforms ,loads  (ETL) data for storage and analysis.
 it automates data flow, making it easier to manage large datasets.

-------
***what data processing
data processing is the process of collecting ,organizing, and transforming 
raw data into meaningful information  . it involves steps like cleaning ,
filtering errors ,converting data types, sorting and analyzing the data 
to make it useful for  decision-making or further analysis. 


how to analyze data?
data analysis involves cleaning ,inspecting,and processing data to extract 
meaningful insights or patterns .tool s like sql, python commonly used 
for this.



"""


"""string methods"""

# string="mahendra is name"
# stringg=["d","g"]
#
# print(string.upper())

# print(string.lower())
# print(string.strip())
# print(string.replace("is","good"))
# print(string.split())
# print(''.join(stringg))
# print(string.find("name"))
# print(string.count("mahendra"))
# print(string.startswith("mahendra"))
# print(string.endswith("name"))
# print(string.capitalize())
# print(string.title())
# print(string.isalpha())
# print(string.isalnum())
# print(string.isalnum())
# print(string.isdigit())
# print(string.swapcase())
# print(string.ljust(100))
# print(string.rjust(25))
# print(string.isspace())
# print(string.center(25))





"""list methods"""

list=[1,2,3,4,5,6,7,8,99,99,100,99,99,99,100,100]
# list.append(10)
# print(list)
#
# list.extend([222,333,444])
# print(list)

# listt=list.count(100)
# print(listt)

# print(list.count(99))




# list.insert(5,1055)
# print(list)

# list.remove(1)
# print(list)









"""tuple methods"""


# tuple=(1,2,3,4,5,5,5,6,7,8,9,10,15,20,25,33,69)
# tuple.count(5)
# print(tuple)

# print(tuple.index(6))

# print(tuple[5:15:2])
# print(tuple[3:10:3])


# n = 8  # Number of rows

# Loop to print the number triangle
# for i in range(1, n + 1):
#     # Print leading spaces to center the triangle
#     print(" " * (n - i), end="")
#
#     # Print multiples of i in each row
#     for j in range(1, i + 1):
#         print(i * j, end=" ")
#
#     # Move to the next line after each row
#     print()
#
#
import threading
# import time
#
# # Function to simulate a task
# def task1():
#     print("Task 1 starting...")
#     time.sleep(2)  # Simulating a delay of 2 seconds
#     print("Task 1 completed!")

# Another function to simulate a task
# def task2():
#     print("Task 2 starting...")
#     time.sleep(1)  # Simulating a delay of 1 second
#     print("Task 2 completed!")
#
# # Create threads for the tasks
# thread1 = threading.Thread(target=task1)
# thread2 = threading.Thread(target=task2)
#
# # Start the threads
# thread1.start()
# thread2.start()
#
# # Wait for both threads to finish
# thread1.join()
# thread2.join()
#
# print("Both tasks completed.")



# l = [1, 2, 2, 3, 4, 5, 5, 6, 7, 7]
# output = sorted(set(l))
# print(output)
#
#
# l = [1, 2, 2, 3, 4, 5, 5, 6, 7, 7]
# unique_elements = []
# for num in l:
#     if num not in unique_elements:
#         unique_elements.append(num)
#
# print(unique_elements)
#
#

# l = [1, 2, 2, 3, 4, 5, 5, 6, 7, 7]
# output = []
# for i in l:
#     if i not in output:
#         output.append(i)
# print(output[:5])  # Take only the first 5 unique elements



# l = [1, 2, 2, 3, 4, 5, 5, 6, 7, 7]
# output = []
# count = 0
#
# for i in l:
#     if i not in output:
#         output.append(i)
#         count += 1
#     if count == 5:  # Stop after 5 unique elements
#         break
#
# print(output)
#
# print(l[:6])
#
#


# strings = ["apple", "banana", "grape", "orange", "kiwi"]
# sorted_strings = sorted(strings, key=len)  # Sort by length of strings
# second_largest = sorted_strings[-2]  # Second largest string
# print(second_largest)





# list=[1,2,2,3,3,4,5,6,6]
#
# remove=[]
#
# for i in list:
#     if i not in remove:
#         remove.append(i)
#     if len(remove)==5:
#         break
# print(remove)

