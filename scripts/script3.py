# script3.py: Check Even or Odd
def is_even(n):
    return n % 2 == 0

for i in range(1, 6):
    print(f"{i} is {'Even' if is_even(i) else 'Odd'}")
