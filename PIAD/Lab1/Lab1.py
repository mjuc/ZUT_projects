
import random
import numpy
import decimal


# zadanie 1
array_1 = numpy.random.randint(0,100,(10,5))
diag_sum_1 = numpy.trace(array_1)
diag_1 = numpy.diag(array_1)
print(array_1)
print(diag_sum_1)
print(diag_1)

# zadanie 2

array_2_1 = numpy.random.normal(0,1.0,10)
array_2_2 = numpy.random.normal(0,1.0,10)
print(array_2_1)
print(array_2_2)
print(array_2_1*array_2_2)

# zadanie 3

array_3_1 = numpy.random.randint(0,100,15)
array_3_2 = numpy.random.randint(0,100,15)
a31 = numpy.reshape(array_3_1,(3,5))
a32 = numpy.reshape(array_3_2,(3,5))

print(array_3_1)
print(array_3_2)
print(a31)
print(a32)
print(a31+a32)

# zadanie 4

array_4_1 = numpy.random.randint(0,100,size=(4,5))
array_4_2 = numpy.random.randint(0,100,size=(5,4))
a43 = numpy.transpose(array_4_2)
print(array_4_1)
print(array_4_2)
print(a43)
print(array_4_1+a43)

# zadanie 5

array_5_1 = array_4_1[:,4]
array_5_2 = numpy.transpose(array_4_2[:,3])
print("tst")
print(array_5_1)
print(array_5_2)
print(array_5_1 + array_5_2)
print("tst_end")

# zadanie 6

array_6_1 = numpy.random.normal(5.0,(4,4))
array_6_2 = numpy.random.uniform(5.0,(4,4))
print(array_6_1)
print(array_6_2)
print(numpy.mean(array_6_1))
print(numpy.mean(array_6_2))
print(numpy.std(array_6_1))
print(numpy.std(array_6_1))
print(numpy.var(array_6_1))
print(numpy.var(array_6_1))

# zadanie 7

array_7_1 = numpy.random.normal(5.0,(4,4))
array_7_2 = numpy.random.uniform(5.0,(4,4))

print(array_7_1)
print(array_7_2)
print(array_7_1*array_7_1)
print(numpy.dot(array_7_1,array_7_2))

# zadanie 8

array_8 = numpy.random.normal(5.0,(10,10))
str = array_8.strides


# zadanie 9

array_9_1 = numpy.random.randint(0,100,15)
array_9_2 = numpy.random.randint(0,100,15)

a91=numpy.hstack((array_9_1,array_9_2))
a92=numpy.vstack((array_9_1,array_9_2))

print(array_9_1)
print(array_9_2)
print(a91)
print(a92)