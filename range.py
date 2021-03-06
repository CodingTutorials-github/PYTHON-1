#The range() Function
#If you do need to iterate over a sequence of numbers, the built-in function range() comes in handy. It
#generates arithmetic progressions:
  
  
  
  
  
  #example1
  
  #CODE INPUT (done in python IDLE)
>>> for i in range(5):
... print(i)
...

#OUTPUT:
0
1
2
3
4



# The given end point is never part of the generated sequence; range(10) generates 10 values, the legal indices
# for items of a sequence of length 10. It is possible to let the range start at another number, or to specify a
# different increment (even negative; sometimes this is called the ‘step’):
range(5, 10)
5, 6, 7, 8, 9
range(0, 10, 3)
0, 3, 6, 9
range(-10, -100, -30)
-10, -40, -70]]]


# To iterate over the indices of a sequence, you can combine range() and len() as follows:
  
  
  #CODE EXAMPLE (done in python IDLE)
>>> a = ['Mary', 'had', 'a', 'little', 'lamb']
>>> for i in range(len(a)):
... print(i, a[i])
...

#output:
0 Mary
1 had
2 a
3 little
4 lamb
