# Tail Recursion
def factorial(n,product=1):
    if n==0:
        return product
    return factorial(n-1,product*n)
print(factorial(10))
# Head Recursion
def print_numbers(a):
    if a == 0:
        return
    print_numbers(a-1)
    print(a)
print_numbers(10)