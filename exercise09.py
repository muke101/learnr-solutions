l = [] #remember we can't use list = [] as list is a keyword

for i in range(101):
    print(i)
    if i % 2 != 0 and i % 3 == 0:
        l.append(i)

print(l)

#output: 0 to 100 and the list [3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99]

