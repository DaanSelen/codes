#Start
import string
import random
import sys
import os

#Complexiteit samenstellen
print('#' * 80 + '\n')
nummer = int(input('Hoeveel wachtwoorden? - '))
lengte = int(input('Wachtwoord lengte? - '))

complexiteit = ''
choice = input('\nWil je de interne library met karakters gebruiken?\n(Alternatief is zelf karakters intypen) ja/nee - ')

if choice == 'ja':
    print('\nLoading Libraries...')
    antwoord = input('\nWil je kleine letters gebruiken? ja/nee - ')
    if antwoord == 'ja':
        complexiteit += string.ascii_lowercase
    antwoord = input('Wil je hoofdletters gebruiken? ja/nee - ')
    if antwoord == 'ja':
        complexiteit += string.ascii_uppercase
    antwoord = input('Wil je nummers gebruiken? ja/nee - ')
    if antwoord == 'ja':
        complexiteit += string.digits
    antwoord = input('Wil je speciale karakters gebruiken? ja/nee - ')
    if antwoord == 'ja':
        complexiteit += string.punctuation
else:
    antwoord = input('\nVul hier je eigen karakters in: ')
    complexiteit = antwoord

#Passwords worden hier gegenereerd
for p in range(nummer):
    password = ''
    for c in range(lengte):
        password += random.choice(complexiteit)
    print('\n' + password)
print('\n' + '#' * 80)
#End