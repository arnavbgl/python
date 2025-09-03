from array import array

#array create
arr1 = array('i',[1,2,5,3,5,7,9])
print(arr1)

#array traverse
for i in range(len(arr1)):
    print(arr1[i])

#access individual element through index

def accesselement(array, index):
    print(array[index])

accesselement(arr1,2)

#append the value
arr1.append(222)

#insert the value at particular index

arr1.insert(3,333)

print(arr1)