secret_number = 7  # The secret number picked by the magician

while True:
    user_number = int(input("Enter an integer number: "))
    
    if user_number == secret_number:
        print("Well done, muggle! You are free now.")
        break
    else:
        print("Ha ha! You're stuck in my loop!")
