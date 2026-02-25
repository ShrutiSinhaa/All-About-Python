# factorial value for 5 is 5*4*3*2*1 [what is factorial value]
n=int(input("Enter a number: "))
def factorial(n):
    if n == 0:
        return 1
    else :
        return n * factorial(n-1)
print("factorial value of", n, "is", factorial(n))

