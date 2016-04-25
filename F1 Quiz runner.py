import random
import sys
from random import shuffle
score = 0
wrong = 0
print ("Welcome to F1 Quiz")

qBank = [
    ("How many championships have Ferrari Won?\nA)3 \nB)1 \nC)7 \nD)16", "d"),
    ("How many qualifying sessions are there in a race weekend? \nA)1 \nB)3 \nC)4 \nD)6", "b"),
    ("When did lewis Hamilton win his first championship \nA)2008 \nB)2014 \nC)2012 \nD)2007", "a"),
    ("Who is the oldest Formula 1 race winner still alive today? \nA)Stirling Moss \nB)Tony Brooks \nC)Dan Gurney \nD)Eddie Jordan", "a"),
    ("Michael Schumacher's 91st and last Formula 1 win came at which 2006 race? \nA)Italy \nB)China \nC)Japan \nD)Monaco", "b"),
    ("Which current F1 driver has competed in the most F1 races? \nA)Lewis Hamilton \nB)Fernando Alonso \nC)Jenson Button \nD)Alexander Rossi", "c"),
    ("How many races did Mark Webber win with Red Bull Racing? \nA)5 \nB)32 \nC)9 \nD)1", "c")
]

shuffle(qBank)
 
numQuestions = int(input("How many questions do you want to be asked?"))
for question, rightAnswer in qBank[:numQuestions]:
    answer = input(question + " ")
    if answer.lower() == rightAnswer:
        print ("Right!")
        score += 1
    else:
        print ("Wrong")
        wrong += 1


percent = ( (score / (score + wrong)) * 100)

if score != 1:
    print ("You got " + str(score) + " questions right! And " + str(wrong) + " wrong.")
else:
    print ("You got " + str(score) + " question right. And " + str(wrong) + " wrong.")

print ("You got " + str(percent) + "% of the questions correct.")
