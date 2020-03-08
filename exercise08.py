l = [] #remember we can't use list = [] as list is a keyword

for i in range(101):
    print(i)
    if i % 2 != 0:
        l.append(i)

print(l)

#output: 0 to 100 and the list [1,3,5,7,...,95,97,99]
