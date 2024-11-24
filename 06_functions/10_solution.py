# recursive ek technique h function ki jisme hum function ko hi call krte rehte h function k ander hi

def factorial(n):
    if n == 0:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case

# Test the function
print(factorial(5))  # Output: 120
