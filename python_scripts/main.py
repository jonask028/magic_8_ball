from curses import KEY_ENTER
from turtle import onkeypress
import random

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
        user_input = input("What would you like to know? (Push enter to exit) \n")
        if user_input:
            answer = random.choice(responses)
            print(f' \n{answer}\n')
        else:
            print("bye!") 
            i = i - 1
            break
magic_8_ball(1)