# script1.py
def greet():
    print("Hello from script1!")

for i in range(5):
    greet()

# script1.py: Simple Addition Function
def add(a, b):
    return a + b

print("Sum:", add(5, 3))



for i in range(100):
    print(i)


for i in range(100):
    if i % 9 == 0:  # Check highest multiple first
        print(f"{i} divided by 9")
    elif i % 6 == 0:
        print(f"{i} divided by 6")
    elif i % 3 == 0:
        print(f"{i} divided by 3")
    else:
        print(f"{i} is others")




