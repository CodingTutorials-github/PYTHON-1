num = 100
while num > 0:
  if num%5 == 0 or num%7 == 0:
    num -= 1
    continue
  print(num)
  num -= 1


#this program prints our numbers from 100 to 1 but skips multiples of 5 and 7.
#all multiples of 5 gives a remainder of sero [0]. So this condition will be true, if num is a multiple of 5.
#basically num should either be multiples of 5 or multiples of 7 in order for the if code to excecute.
