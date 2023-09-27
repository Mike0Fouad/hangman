#importing modules
from random_word import*
from figures import*



# initializing variables, taking input and getting the word and hiding it
print("                                     Welcome to "+welcome)
word= list(rand_word(input("\nEnter a difficulty level (easy, medium, hard):  ")))
life=0
hidden= list(hide_word(word))
# printing the hidden word
print(spaced(stringfy(hidden)))
# while loop to keep the game going until the player wins or loses
while True:
    # taking input and checking if the letter is in the word
    letter=input("\nGuess a letter: ").lower()
    if letter in word:
        # if the letter is in the word, the hidden word is updated
        for i in range (0,len(word)):
            if letter == word[i]:

                hidden[i] = letter
        print("********************\n       correct!\n********************".upper())
        print(spaced(stringfy(hidden)))
        
    else:
        # if the letter is not in the word, the life is decreased and the hangman figure is printed
        life+=1
        print("********************\n       wrong!!\n********************".upper())
    # printing the hangman figure
    print(hangman[life])
    
    # checking if the player has won or lost
    if life==6 or (hidden)==word:
        break
# printing the result
print("the word was: "+stringfy(word))
  
if life ==6:
    print(loss)
else:
    print(win)