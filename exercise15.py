l = [] 

for i in range(101):
    if i % 2 != 0:
        l.append(i)

for i in l: #remember we can take any 'iterable' object and loop over it's contents directly
    if i % 5 == 0:
        l.remove(i)

print(l[-5:]) #if we put a -, we go backwards in the list

#output: the list [89, 91, 93, 97, 99]

