import re
password = input("Vul hier je wachtwoord in: ")
flag = 0
while True:  
    if (len(password)<8):
        flag = 1
        break
    elif not re.search("[a-z]", password):
        flag = 2
        break
    elif not re.search("[A-Z]", password):
        flag = 4
        break
    elif not re.search("[0-9]", password):
        flag = 8
        break
    elif not re.search("[!#$%&'()*+, -./:;<=>?@[]^_`{|}~]", password):
        flag = 16
        break
    else:
        flag = 31
        print("Valid Password")
        break
  
if flag != 31:
    print(flag)