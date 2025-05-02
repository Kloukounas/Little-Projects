
def mul_list(mylist):
    for i in range(len(mylist)):
        mylist[i] = mylist[i] * mylist[i]

mylist = [1, 2, 3]

mul_list(mylist)
print(mylist)