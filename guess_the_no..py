import random
computer_num=random.randrange(1,101)
score=10
while True:
    user_num = int(input("Guess the number between 1,100\n"))
    if user_num==computer_num:
        print('You Win with score',score)
        break
    elif user_num < computer_num:
        print("too small")
    else:
        print("Too Big")
    score-=1