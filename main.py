play = "yes"
# Ask the user their name and store it
name = input("What is your name?")
if name == "":
      print("Not sure?")

# Greet the user and introduce the quiz
print("Hello welcome to my phython quiz",name)

while True:
      try:
            tries = input("How many attempts do you want for each question? 1-4")
            tries = int(tries)
            break
      except:
            print("Thats not a number.")

# Introduce what the quiz is about
print("This quiz is about the programming language python.")

while play == "yes":

      score = 0

      question_attempts = tries
      while question_attempts > 0:

            # Ask the user a question
            question = "What symbol is used to denote comments in Python"
            a = "//"
            b = "#"
            c = "/**/"
            d = "--"
            answer = input("{}\nA.{} B.{} C.{} D.{}".format(question, a, b, c, d,)).lower()


            # Check the user’s answer and give feedback
            if answer == b or answer == "b".lower():
                  score += 1
                  print("correct!")
                  break
            elif answer != a and answer != "a" and answer != b and answer != "b" and answer != c and answer != "c" and answer != d and answer != "d":
                  print("That wasnt a option???")
            elif answer == "":
                  print("Not sure?")
            else: 
                  print("Incorrect.") 
                  
            
            question_attempts -= 1
            
      question_attempts = tries
      while question_attempts > 0:

            # Ask the user a question
            answer = input("What year was python founded?").lower()

            # Check the user’s answer and give feedback
            if int(answer) < 1991:
                  print("its an earleir date than that.")
                  question_attempts -= 1
            elif int(answer) > 1991: 
                  print("its a later date than that.")
                  question_attempts -= 1
            elif answer == "":
                  print("Not sure?")
            else:
                  print("Correct!")
                  score = score + 1
                  break         
      # End the quiz
      print("Well done {} you finished the quiz. Your final score is {}.". format(name, score))
      if int(score) == 2:
            print("You did great!") 
      else:
            print("Better luck next time.")
      play = input ("Do you want to play again?").lower()      
