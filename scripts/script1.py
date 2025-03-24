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
    if i%3==0:
        print(f"{i} divided by 3")
    elif i%6==0:
        print(f"{i} divided by 5")
    elif i%9==0:
        print(f"{i} divided by 7")

