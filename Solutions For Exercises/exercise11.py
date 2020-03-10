for i in range(1,101): #the question said 1 to 100, so we must specify to start at 1, not 0
    if i % 5 == 0 and i % 3 == 0: #this case must be the very first one, as otherwise a number that is a multiple of both 3 and 5 will always be caught by one of the other two if statements first, which will then end the if checks, as only one block of an if-else-if chain will get executed
        print('fizzbuzz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')

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
