import random

def number_guessing_game():
   """Simple number guessing game using Python."""
  print("🎯 WELCOME TO NUMBER GUESSING GAME ")
  print("YOU SELECT NUMBER BETWEEN 1 TO 100 .\n ")
  
  secret_number = random.randint(1,100)
  attempt = int(input("Enter number of attempts : "))
  
  while attempt > 0:
    try:
      guess = int(input("Enter your guessing number : " ))
    except ValueError:
      print("please enter a valid number .\n ")
      continue
    
    if guess<secret_number:
      attempt -= 1
      print("📉 Too Low!")
    elif guess>secret_number:
      attempt -= 1
      print("📈 Too high!")
    else :
      print(f"🎉 Congratulations! You guessed it right: {secret_number}")
      return
    
    print(f"Attempts left: {attempt}\n")  
  
  print(f"😢 Game Over! The number was {secret_number}")

number_guessing_game()  
