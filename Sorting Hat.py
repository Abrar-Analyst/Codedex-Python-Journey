Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

Q1 = int(input("Do you like Dawn or Dusk? "))
print("1) Dawn")
print("2) Dusk")

answer = int(input("Answer (1 or 2): "))

if (answer == 1):
  Gryffindor += 1
  Ravenclaw += 1
elif (answer == 2):
  Hufflepuff += 1
  Slytherin += 1
else:
  print("Wrong input.")

Q2 = int(input("When I’m dead, I want people to remember me as: "))
print("1) The Good")
print("2) The Great")
print("3) The Wise")
print("4) The Bold")

answer1 = int(input("Answer (1-4): "))

if (answer1 == 1):
   Hufflepuff += 2
elif (answer1 == 2):
   Slytherin += 2
elif (answer1 == 3):
   Ravenclaw += 2
elif (answer1 == 4):
    Gryffindor += 2
else:
  print("Wrong input.")

Q3 = int(input("Which kind of instrument most pleases your ear? "))
print("1) The violin")
print("2) The trumpet")
print("3) The piano")
print("4) The drum")

answers = int(input("Answers (1-4): "))

if (answers == 1):
   Slytherin += 4
elif (answers == 2):
   Hufflepuff += 4
elif (answers == 3):
   Ravenclaw += 4
elif (answers == 4):
   Gryffindor += 4
else:
  print("Wrong input.")

print("\nFinal score:")
print(" Gryffindor: " ,Gryffindor)
print(" Ravenclaw: ", Ravenclaw)
print(f" Hufflepuff: ",Hufflepuff)
print(f" Slytherin: ",Slytherin)

highest_scores = max(Gryffindor, Ravenclaw, Hufflepuff, Slytherin)

print("Congrats you belong to: ")

if (highest_scores == Gryffindor):
  print("🦁 Gryffindor!")
elif (highest_scores == Ravenclaw):
  print("🦅 Ravenclaw!")
elif (highest_scores == Hufflepuff):
  print("🦡 Hufflepuff!")
else:
  print("🐍 Slytherin!")
