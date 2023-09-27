from random_word import*
from figures import*

life=0


print("                                     Welcome to "+welcome)




word= list(rand_word(input("Enter a difficulty level (easy, medium, hard):  ")))
hidden= list(hide_word(word))
print(spaced(stringfy(hidden)))
while True:
    letter=input("Guess a letter: ").lower()
    if letter in word:
        for i in range (0,len(word)):

            if letter == word[i]:

                hidden[i] = letter
        print("********************\n       correct!\n********************".upper())
        print(spaced(stringfy(hidden)))
        
    else:
        life+=1
        print("********************\n       wrong!!\n********************".upper())
    print(hangman[life])


    if life==6 or (hidden)==word:
        break

print("the word was: "+stringfy(word))
      
if life ==6:
    print(loss)
else:
    print(win)