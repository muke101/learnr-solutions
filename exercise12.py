for i in range(1,101): #the question said 1 to 100, so we must specify to start at 1, not 0
    if i % 5 == 0 and i % 3 == 0: #this case must be the very first one, as otherwise a number that is a multiple of both 3 and 5 will always be caught by one of the other two if statements first, which will then end the if checks, as only one block of an if-else-if chain will get executed
        print(i,'fizzbuzz')
    elif i % 3 == 0:
        print(i,'fizz')
    elif i % 5 == 0:
        print(i,'buzz')

"""
output:
3 fizz
5 buzz
6 fizz
9 fizz
10 buzz
12 fizz
15 fizzbuzz
18 fizz
20 buzz
21 fizz
24 fizz
25 buzz
27 fizz
30 fizzbuzz
33 fizz
35 buzz
36 fizz
39 fizz
40 buzz
42 fizz
45 fizzbuzz
48 fizz
50 buzz
51 fizz
54 fizz
55 buzz
57 fizz
60 fizzbuzz
63 fizz
65 buzz
66 fizz
69 fizz
70 buzz
72 fizz
75 fizzbuzz
78 fizz
80 buzz
81 fizz
84 fizz
85 buzz
87 fizz
90 fizzbuzz
93 fizz
95 buzz
96 fizz
99 fizz
100 buzz
"""
