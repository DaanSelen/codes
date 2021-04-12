import random
import pyautogui
import string
import time

def calculate_time(startTime):
    endTime = time.time()
    elapsedTime = endTime - startTime
    print("Cracking your password took: " + elapsedTime + " seconds")

chars = string.printable

# chars = string.printable
chars_list = list(chars)


password = pyautogui.password("Enter a password: ")

startTime = time.time()

guess_password = ""


while(guess_password != password):
    guess_password = random.choices(chars_list, k=len(password))

    print("<="+ str(guess_password)+ "=>")

    if(guess_password == list(password)):
        print("Your password is: "+ "".join(guess_password))
        calculate_time(startTime)
        break