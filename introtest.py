#!/usr/bin/env python3

#Title: Introvert or Extrovert Test v1


#Below is for Linux users to allow program to be executable: ./introtest.py
#Copy and paste it before the title!

#!/usr/bin/env python3

#Make sure to add executable permssions: sudo chmod +x introtest.py


#Tell user to enter y for yes and n for no
print("For the questions below, enter y for YES and n for NO\n")


#Create a dictionary to store the answers to the questions
answers = {"yes": 0, "no": 0}


#Questions to determine if the user is Introvert or Extrovert

while True:
  question_1 = input("Question 1: Are you active in more than two different group chat? Answer: ")
  if question_1 == "y":
    answers["yes"] += 1
  elif question_1 == "n":
    answers["no"] += 1
  break

while True:
  question_2 = input("Question 2: When a coworker/friend asks you to go have a drink after work, do you want to go? Answer: ")
  if question_2 == "y":
    answers["yes"] += 1
  elif question_2 == "n":
    answers["no"] += 1
  break

while True:
  question_3 =  input("Question 3: Are you a fan of last-minute plans? Answer: ") 
  if question_3 == "y":
    answers["yes"] += 1
  elif question_3 == "n":
    answers["no"] += 1
  break

while True:
  question_4 =  input("Question 4: Are you a fan of being on camera? Answer: ")
  if question_4 == "y":
    answers["yes"] += 1
  elif question_4 == "n":
    answers["no"] += 1
  break

while True:
  question_5 =  input("Question 5: Do you thrive when you're in charge of a project? Answer: ")
  if question_5 == "y":
    answers["yes"] += 1
  elif question_5 == "n":
    answers["no"] += 1
  break

while True:
  question_6 =  input("Question 6: Do you send the first message? Answer: ")
  if question_6 == "y":
    answers["yes"] += 1
  elif question_6 == "n":
    answers["no"] += 1
  break

while True:
  question_7 =  input("Question 7: Do you act first without thinking? Answer: ")  
  if question_7 == "y":
    answers["yes"] += 1
  elif question_7 == "n":
    answers["no"] += 1
  break

while True:
  question_8 =  input("Question 8: Do you usually eat lunch in a large group? Answer: ")
  if question_8 == "y":
    answers["yes"] += 1
  elif question_8 == "n":
    answers["no"] += 1
  break


#Display answers dictionary
print("\nAnswers: " + str(answers))


#Function to determine whether the user is Introvert or Extrovert
def introvert_or_extrovert_test(answers):
  print("\nResults: ")
  if answers["yes"] > answers["no"]:
    print("Unfortunately you are an Extrovert.")
  elif answers["yes"] < answers["no"]:
    print("Congratulations, you are an Introvert!")
  else:
    print("Oh interesting, you are an ambivert.")   

introvert_or_extrovert_test(answers)
