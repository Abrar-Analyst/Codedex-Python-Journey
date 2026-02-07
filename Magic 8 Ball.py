import random

question = input("Please enter yes or no question here: ")

answers = [
  "Yes - definitely.",
  "It is decidedly so.",
  "Without a doubt.",
  "Reply hazy, try again.",
  "Ask again later.",
  "Better not tell you now.",
  "My sources say no.",
  "Outlook not so good.",
  "Very doubtful."
] 

answer = random.choice(answers)

print("Magic 8 ball answer is: ", answer)
