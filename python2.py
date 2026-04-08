from math import sqrt
mylist =[]
tot=0
n=int(input('enter the number of items:'))
print('enter',n,'the items:')
for i in range(n):
    item =int (input())
    mylist += [item]#append()
    tot += item
    mean = tot / n
    tot = 0
    for item in mylist:
        tot += (item-mean)*(item-mean)
        var =tot/n
        std =sqrt(var)
        print("mean=",mean)
        print("variance=",var)
        print("standard deviation=",std)
