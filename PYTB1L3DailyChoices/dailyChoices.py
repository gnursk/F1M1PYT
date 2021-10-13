print ("You get woken up by your alarm, do you GETUP or do you SNOOZE")
choice1 = input()
if choice1 == 'GETUP':
    print ("You had a good night of sleep, you feel refreshed")
elif choice1 == "SNOOZE":
    print ("you stay in bed for a little longer, but when you wake up you need to rush, was this the right decision?")
else:
    print (choice1, "is not a valid awnser")

print ("You get out of bed, you brush your teeth and dress up. Do you eat BREAD or CORNFLAKES?")
choice2 = input()
if choice2 == "BREAD":
    print ("You ate some bread with cheese, the cheese was out of date though, you feel sick now.")
elif choice2 == "CORNFLAKES":
    print ("You had some cornflakes with milk, it was a good and healthy breakfast.")
else:
    print (choice2, "can't be defined")

print ("You need to get to the train for school, do you take a RIGHT, right is the shortest way but there might be alot of wind, or do you take LEFT, this is the safe route but your a bit late so you might need to take the right to make it in time.")
choice3 = input()
if choice3 == "RIGHT":
    print ("You took the right, there was too much wind and you didn't make it in time for the train")
elif choice3 == "LEFT":
    print ("You took the safe choice, it worked out, you got to the train just in time")
else:
    print(choice3, "I couldn't understand that")

print ("You get home from a long day of school, you need to make dinner, do you make PIZZA or CARROTS")
choice4 = input()
if choice4 == "PIZZA":
    print ("The pizza was good, it was a nice cheap and easy dinner")
elif choice4 == "CARROTS":
    print("The carrots were good, a nice and healthy dinner")
else:
    print (choice4, "I was unable to identify that")

print ("It's getting pretty late, do you STAYUP to feed your crippeling phone addiction, or do you SLEEP and feel nice and refreshed tomorrow?")
choice5 = input()
if choice5 == "STAYUP":
    print("You stayed up untill 2 am, you are very tired now")
elif choice5 == "SLEEP":
    print ("You went to bed early, you're still tired though.")
else:
    print(choice5,"is not a valid awnser" )

