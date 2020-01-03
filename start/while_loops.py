#i = 1
#while i <= 10:
#    print(i)
#    i += 1

#print("Done with loop")

secret_word = "giraffe"
guess = ""

while True:
    guess = str(input("Enter the word: "))
    if guess == secret_word:
        print("Congrats! The secret word is " + secret_word)
        break
    else:
        print("Noup! Try again...")
        continue


####THE OTHER WAY

guess_count = 0
guess_limit = 3
out_of_guesses = False
while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = str(input("Enter the word: "))
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, you LOSE!")
else:
    print("You win!")
