
# Guess the Number

import random
guess=random.randint(1,10)
print(guess)
print("Guess the Number between 1 tO 10!")
# guess=0
score=0


for i in range(0,3):
    num=int(input('num'))
    if(guess==num):
        score=score+5
    else:
        score=score-2
print(score)