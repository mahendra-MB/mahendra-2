# script5.py: Factorial Calculation
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print("Factorial of 5:", factorial(5))
