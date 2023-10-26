def game(Q,A):
    guesses = []
    score = 0
    questions_no = 1
    for i,j in Q.items():
        print("--------------------------------------------------------")
        print(i)
        for k in A[questions_no-1]:
            print(k)
        questions_no += 1
        user_guess = input("Enter the Answer like 'A','B','C','D':").upper()
        if user_guess == j:
            print("correct")
            guesses.append(user_guess)
        else:
            print("Wrong")
    score = len(guesses)
    print("You score is {}/3".format(score))
def play_again():
    while True:
        user = input("Do you wanna play again ?").lower()
        if user == "yes" or user == "y":
            game(questions,answers)
        else:
            print("Thank you ! bye : ) ")
            break


questions = {
    "What is the maximum length of a Python identifier?" : "D",
    "What will be the output of the following code snippet?print(2**3 + (5 + 6)**(1 + 1))" : "A",
    "How is a code block indicated in Python?" : "B"
    }
answers = [["32,16,128,No fixed length is specified."],["129,8,121,None of the above."],["Brackets,Indentation,Key,,None of the above."]]


game(questions,answers)
play_again()