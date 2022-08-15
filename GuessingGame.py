answer=6 #Number to be guessed
print("Welcome to the guessing game!!\nPlease guess a number between 1 to 10: ")
guess=int(input())
if guess==answer:
    print("Yayy!! You've guessed the right answer in first attempt:")
    exit(0) #using the best case to save time and exitting the program
def check():
    guess = int(input())
    if guess == answer:
        print("You've guessed it right!")
    else:
        print("Better luck next time :(")
                                    #code reusability
if guess<answer:
    print("please guess higher!")
    check()
elif guess>answer:
    print("please guess lower!")
    check()
