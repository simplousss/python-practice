# Ask the user their name and store it
name = input("What is your name?")

# Greet the user and introduce the quiz
print("Hello welcome to my phython quiz ",name)

# Introduce what the quiz is about
print("This quiz is about the programming language python.")

# Ask the user a question
answer1 = input("1. What symbol is used to denote comments in Python a: // b: # c: /* */ d: -- ?")

# Check the user’s answer and give feedback
if answer1 == "#":
     print("correct!")
else:
    print("Incorrect, the correct answer is #.") 

# Ask the user a question
answer2 = input("What year was python founded")

# Check the user’s answer and give feedback
if int(answer2) < 1991:
     print("its an earleir date than that")
elif int(answer2) > 1991: 
     print("its a later date than that")
else:
          print("Correct!")

# End the quiz
print("This is the end of the quiz thank you for playing.")