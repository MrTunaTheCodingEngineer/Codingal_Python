def factorial(x):
    '''this is a recrusial function to find the
    factorial of an intiger'''

    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)
    
print(factorial.__doc__)
print("the factorial of 6 is: ", factorial(6))
print("the factorial of 12 is: ", factorial(12))
print("the factorial of 24 is: ", factorial(24))
print("the factorial of 36 is: ", factorial(36))
print("the factorial of 48 is: ", factorial(48))
print("the factorial of 60 is: ", factorial(60))






