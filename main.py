import numpy as np

#concept of array slicing
#[start: end: step]

linear_array = np.array([1,2,3,4,5,6,7,8])

print(linear_array[0:3]) #goes up to 3 starting from 0

print(linear_array[:5]) #automatically starts from 5 if theres no number before that

print(linear_array[::2]) #print every second number 

print(linear_array[::-1]) #it will go back in reverse 

multi_array = np.array([[1,2,3] , [4,5,6] , [7,8,9]])

print(multi_array)

#slicing multidimensional array

print(multi_array[0:2,0:2]) #row slicing, column slicing

print(multi_array[0:2, 1:3])

matrix = np.array(np.arange(0,49).reshape(7,7))
print(matrix)

print("After slicing into 3*3 matrix")
print(matrix[3:5, 2:5])

#mathematical computations on array
#print even numbers
k = np.array([1,2,3,4,5,6,7,8,9,10])
even_array = k[k%2==0]
print(even_array)

#compare the value
bool_array = k[k==5]

print(bool_array) #only the value 5 is true

#selection by indexes

print(k[[2,4,6]]) #selectin the values by index numbers


f = np.array([1,2,3,4,5,6,7,8,9,10])

print(f[[0,1,2,3,4]])

