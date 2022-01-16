from calendar import c
import random
import os

out0 = "It is certain"
out1 = "Outlook good"
out2 = "You may rely on it"
out3 = "Ask again later"
out4 = "Concentrate and ask again"
out5 = "Reply hazy, try again"
out6 = "My reply is no"
out7 = "My sources say no"

responses = [out0,out1,out2,out3,out4,out5,out6,out7]
i = 1
def magic_8_ball(i):
    while True:
        user_input = input("What would you like to know? (Type 'C' to clear the screen, type 'Q' to quit) \n").lower()
        if user_input and not user_input == 'q' and not user_input == 'c':
            answer = random.choice(responses)
            print(f' \n{answer}\n')
        elif user_input == 'q':
            quit()
        elif user_input == 'c':
            os.system('cls')
            i = i
        else:
            print('Please try again. \n')
magic_8_ball(i)
