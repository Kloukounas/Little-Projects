
list1 = [4, 5, 6]
list2 = [1, 2, 3]

def sub(list1, list2):
    list3 = []
    for i in range(len(list1)):
        list3.append(list1[i] - list2[i])
    return list3


list3 = sub(list1, list2)

print(list3)
