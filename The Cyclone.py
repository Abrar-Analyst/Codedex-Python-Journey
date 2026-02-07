height = int(input("What is your height: "))
credits = int(input("What is your credits: "))

if (height >= 173 and credits >= 10):
  print("Enjoy the ride!")
elif (height < 173 and credits >= 10):
  print("You are not tall enough to ride.")
elif (height >= 173 and credits < 10):
  print("You don't have enough credits")
else:
  print("You didn't meet the requirement.")
