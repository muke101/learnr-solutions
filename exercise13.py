l = [] 

for i in range(101):
    if i % 2 != 0:
        l.append(i)

for i in l: #remember we can take any 'iterable' object and loop over it's contents directly
    if i % 5 == 0:
        l.remove(i)

print(l)

#output: the list [1, 3, 7, 9, 11, 13, 17, 19, 21, 23, 27, 29, 31, 33, 37, 39, 41, 43, 47, 49, 51, 53, 57, 59, 61, 63, 67, 69, 71, 73, 77, 79, 81, 83, 87, 89, 91, 93, 97, 99]

