
import random, string
import os
import time
os.system('pkg install figlet && pkg install python')
os.system('clear')

os.system('figlet Danyar.sad')
time.sleep(4)


print("======================")
text = string.ascii_letters + string.digits

ani = int(input('Chand Pet Be : '))
print("========================")
hama = int(input('Chand User Drust kat : '))

with open('ani.txt', 'a') as file:

    for x in range(hama):

        word = ''.join(random.choice(text) for x in

range(ani))

        if x == range(hama)[-1]:
            file.write(word)
        else:
            file.write(word + '\n')

    print("===========================")
    os.system('clear')
    input('=====Tawaw Bu! Enter Ka Bo Darchun!========\n')
    print("===================DoNe====================")
    os.system("clear")