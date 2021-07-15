from itertools import islice

n = int(input())
arr = list(map(int, input().split()))
brr = iter(arr)
arr = [list(islice(brr, n)) for _ in range(n)]
print(arr)


#Another method
#The shape tool gives a tuple of array dimensions and can be used to change the dimensions of an array.
import numpy
n = list(map(int,input().split()))
change_array = numpy.array(n)
change_array.shape = (3, 3)#First 3 is row and 2nd 3 is column
print (change_array)


#The reshape tool gives a new shape to an array without changing its data. It creates a new array and does not modify the original array itself.

import numpy
n = list(map(int,input().split()))
my_array = numpy.array([n)
print numpy.reshape(my_array,(3,2))
