question=('which of the following cannot be seen?')
print("")
print(" the question is:")
print(" which of the following (bacteria, humans, yeasts, keychains) canot be seen?")
print("bacteria = 1")
print("humans = 2")
print("yeasts = 3")
print("keychains = 4")
print("")
opt1 = ['bacteria']
opt2 = ['humans']
opt3 = ['robots']
opt4 = ['yeast']
opt5 = ['keychains']
answerList=['1', '4']
#print questions and answers
#ask user for input
ans=input("what is your answer?")


userAnswer = ans.split(",")
answerFlag = True
if len(userAnswer)!= len(answerList):
  answerFlag = False
for item in userAnswer:
  if item not in answerList:
   answerFlag = False
if answerFlag == True:
  print("your answer is Correct, good job!")
else:
  print("your answer is wrong, please try again!")


