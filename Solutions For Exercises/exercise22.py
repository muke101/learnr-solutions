def isFactorOf5(x):
    if x % 5 == 0:
        return True
    else:
        return False

def isFactorOf3(x):
    if x % 3 == 0:
        return True
    else:
        return False

def ifFactor(x,f): #bonus function - why repeat code if we can contain all the same logic in one extensible function?
    if x % f == 0:
        return True
    else:
        return False

def fizzbuzz(n):
    for i in range(1,n): 
        if isFactorOf3(i) and isFactorOf5(i):
            print('fizzbuzz')
        elif isFactorOf3(i):
            print('fizz')
        elif isFactorOf5(i):
            print('buzz')

fizzbuzz(100)

"""
output:
fizz
buzz
fizz
fizz
buzz
fizz
fizzbuzz
fizz
buzz
fizz
fizz
buzz
fizz
fizzbuzz
fizz
buzz
fizz
fizz
buzz
fizz
fizzbuzz
fizz
buzz
fizz
fizz
buzz
fizz
fizzbuzz
fizz
buzz
fizz
fizz
buzz
fizz
fizzbuzz
fizz
buzz
fizz
fizz
buzz
fizz
fizzbuzz
fizz
buzz
fizz
fizz
buzz
"""
