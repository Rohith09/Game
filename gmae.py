# The word jumble game
import random
WORDS = ("python","jumble","game","word","rachit","shashank","anmol")
word = random.choice(WORDS)
correct = word
jumble =""
while word:
    position = random.randrange(len(word))
    jumble +=word[position]
    word = word[:position]+word[(position+1):]

#Start the game
print(
    """
         WELCOME TO WORD JUMBLE
         ----------------------
         Unscramble the letters to make a word\n
         """
    )
print("the jumble is:",jumble)
guess=input("\nyour guess:")
while guess !=correct and guess !="":
    print("sorry thats not it,")
    guess=input("your guess:")
if guess==correct:
    print("thats it! you guessed it!\n")
print("thanks for playing")
input("\n\n press the enter key to exit")
