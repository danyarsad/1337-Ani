import requests
import os
os.system('pip install heatshrink && pkg install figlet&&pip install figlet ')
os.system('xdg-open https://www.instagram.com/danyar.sad')
os.system('clear')
os.system('figlet danyar.sad')
print("=============================================")


t = raw_input(" List File : ")

print("=============================================")

file = open(t, 'r').readlines()
for x in file:
  u = x.strip()
  url = "https://instagram.com/"+u
  ss = requests.get(url)
  chk = ss.status_code
  if chk==200:
    print("==== USER ====")
    print("User : "+u)
    print("La instagram  : Haya")
    print("=============")
    print(" ")
  elif chk==404:
    print("==== USER ====")
    print("User : "+u)
    print("La instagram nya : Nya")
    print("=============")
    print(" ")
    
os.system('figlet DONE')
