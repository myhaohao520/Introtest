#!/usr/bin/env python3

#Title: Introvert or Extrovert Test v1


#Below is for Linux users to allow program to be executable: ./intr>#Copy and paste it before the title!

#!/usr/bin/env python3

#Make sure to add executable permssions: sudo chmod +x introtest.py


#Tell user to enter y for yes and n for no
print("For the questions below, enter y for YES and n for NO")


#Questions to determine if the user is Introvert or Extrovert

while True:
  question_1 = input("Question 1: Are you active in more than two d>  if question_1 == "y":
    answers["yes"] += 1
  elif question_1 == "n":
    answers["no"] += 1
                     
while True:
  question_2 = input("Question 2: When a coworker/friend asks you t>  if question_2 == "y":
    answers["yes"] += 1
  elif question_2 == "n":
    answers["no"] += 1

while True:
  question_3 =  input("Question 3: Are you a fan of last-minute pla>  if question_3 == "y":
    answer["yes"] += 1
  elif question_3 == "n":
    answers["no"] += 1

while True:
  question_4 =  input("Question 4: Are you a fan of being on camera>  if question_4 == "y":
    answer["yes"] += 1
  elif question_4 == "n":
    answers["no"] += 1

while True:
  question_5 =  input("Question 5: Do you thrive when you're in cha>  if question_5 == "y":
    answer["yes"] += 1
                  elif question_5 == "n":
    answers["no"] += 1

while True:
  question_6 =  input("Question 6: Do you send the first message?")
  if question_6 == "y":
    answer["yes"] += 1
  elif question_6 == "n":
    answers["no"] += 1

while True:
  question_7 =  input("Question 7: Do you act first without thinkin>  if question_7 == "y":
    answer["yes"] += 1
  elif question_7 == "n":
    answers["no"] += 1

while True:
  question_8 =  input("Question 8: Do you usually eat lunch in a la>  if question_8 == "y":
    answer["yes"] += 1
  elif question_8 == "n":
    answers["no"] += 1
                      
                      
#Create a dictionary to store the answers to the questions
answers = {"yes": 0, "no": 0}


#Function to determine whether the user is Introvert or Extrovert
def introvert_or_extrovert_test(answers):
  print("Results: ")
  if answers[yes] >= answers[no]:
    print("Unfortunately you are an Extrovert.")
  elif answers[yes] <= answers[no]:
    print("Congratulations, you are an Introvert!")
  else:
    print("Oh interesting, you are an ambivert.")   
