def fizzbuzz(n):
    for i in range(1,n): 
        if i % 5 == 0 and i % 3 == 0: 
            print('fizzbuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
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
