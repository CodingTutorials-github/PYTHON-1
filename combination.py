# combining conditions


'''
IMAGINE:

your father comes to you and tell u, if ur math and sci score is above 90, you get a gift
if your math score and sci score is below 50, then attend tution classes, and no gift.

PROGRAM:

'''

math = int(input("your math score is?"))
science = int(input("your science score is?"))
if math > 90:
  if science > 90:
    print("congrats!you get a gift! YAY")
elif math < 50:
  print("you need tution bro")
elif science < 50:
  print("you need tution also bro")
else:
  print("thats fine with me")
