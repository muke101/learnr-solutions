def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)

def factorial_better(n,t): #bonus function - this is a more efficient implementation due to some specifics on how computers work. Don't worry about it unless you're interested, but the basic idea is that if you pass the running total of the factorial in the argument of the funciton itself, it doesn't have to 'memorize' the running result for the whole chain of function calls, but instead can just worry about one function at a time, as it's all self contained. This means that the program would use the same amount of memory (ram) for factorial(10000) as it would for factorial(5)!
    if n == 1:
        return t
    else:
        return factorial(n-1,t*n)

print(factorial(5))

#output: 120
