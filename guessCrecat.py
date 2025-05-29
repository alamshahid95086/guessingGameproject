import random

n=random.randint(1,100)
a=-1
guesses=0

while (a != n):
    guesses+=1
    a =int(input("Guess the number 🤔 :-"))

    if ( a > n):
        print("Lower Number please⬇️")

    else:
        print ("higher Number please ⬆️")

print (f" you have guessed  the number {n}  corretetly in {guesses} attempts ")