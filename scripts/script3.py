# script3.py: Check Even or Odd
def is_even(n):
    return n % 2 == 0

for i in range(1, 6):
    print(f"{i} is {'Even' if is_even(i) else 'Odd'}")


# Print numbers from 1 to 20 and classify them
for i in range(1, 21):
    if i % 2 == 0 and i % 3 == 0:
        print(f"{i} is divisible by both 2 and 3")
    elif i % 2 == 0:
        print(f"{i} is even")
    elif i % 3 == 0:
        print(f"{i} is divisible by 3")
    else:
        print(f"{i} is an odd number")

print("\n--- Counting using a while loop ---\n")

# Using while loop to count down from 10 to 1
count = 10
while count > 0:
    print(f"Countdown: {count}")
    count -= 1

print("\nLoop finished!\n")

# Nested loops to print a simple pattern
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

print("\nProgram Completed!")
