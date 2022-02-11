name = input ("what is your name?: ")
birthYear = int(input("what year is it? :"))
currentYear = int(input("what year is it?:"))
rating = input ("what is the censorship rating of the movie? :")
age = currentYear - birthYear

if age >= 0 and age <=12 and rating == "G" :
  print("Dear",  name, "you are allowed to watch this movie")
elif age >= 13 and age <=20 and rating != "R21":
  print("Dear",  name, "you are allowed to watch this movie")
elif age >=21 :
  print("Dear",  name, "you are allowed to watch this movie")
else:
  print("De
