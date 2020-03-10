l = [] #remember we can't use list = [] as list is a keyword

for i in range(101):
    print(i)
    if i % 2 != 0 and i % 3 != 0:
        l.append(i)

print(l)

#output: 0 to 100 and the list [1, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41, 43, 47, 49, 53, 55, 59, 61, 65, 67, 71, 73, 77, 79, 83, 85, 89, 91, 95, 97]


