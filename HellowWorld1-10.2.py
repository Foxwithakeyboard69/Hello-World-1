import random
n = random.randint(1,10)
print("I'M THINKING OF A NUMBER BETWEEN 1 AND 10...")
running = True
while running:
    guess_str = input("Take a guess")
    guess = int(guess_str)
    if guess == n:
        print("Nice job cutie~")
        running = False
    elif guess < n:
        print("Try a bigger number")
    else:
        print("Try a smaller number")