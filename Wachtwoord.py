#Start
import string
import random
import sys
import os

#Functies
def wachtwoord_lengte():
    lengte = int(input('Wachtwoord lengte? - '))
    return lengte

def invalid_reactie():
    print('U heeft een fout antwoord ingevult')

def lengte_bepaling():
    lengte = wachtwoord_lengte()
    if lengte < 8:
        antwoord = input('\nU heeft minder dan 8 karakters ingetypt, klopt dit? Dit is niet veilig. ja/nee - ')
        if antwoord == 'ja':
            return lengte
        elif antwoord == 'nee':
            wachtwoord_lengte()
        else:
            invalid_reactie()
            lengte_bepaling()
    return lengte

#Complexiteit samenstellen
while True:
    print('#' * 80 + '\n')
    nummer = int(input('Hoeveel wachtwoorden? - '))
    lengte = lengte_bepaling()

    complexiteit = ''
    choice = input('\nWil je de interne library met karakters gebruiken?\n(Alternatief is zelf karakters intypen) ja/nee - ')

    if choice == 'ja':
        print('\nLoading Libraries...')
        antwoord = input('\nWil je kleine letters gebruiken? ja/nee - ')
        if antwoord == 'ja':
            complexiteit += string.ascii_lowercase
        else:
            print('')
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
    print('\n' + '#' * 80 + '\n')
#End