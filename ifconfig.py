import os

while True:

    print('\nTyp het ipadres een gedeelte per keer\ntyp het eerste gedeelte: ', end='')
    ip_adres1 = int(input())
    print('typ het tweede gedeelte: ', end='')
    ip_adres2 = int(input())
    print('typ het derde gedeelte: ', end='')
    ip_adres3 = int(input())
    print('typ het vierde gedeelte: ', end='')
    ip_adres4 = int(input())

    ip_adres = (str(ip_adres1) + '.' + str(ip_adres2) + '.' + str(ip_adres3) + '.' + str(ip_adres4))
    print(ip_adres)
    os.system('ping {}'.format(ip_adres))
    
    print('\nWil je doorgaan? ', end='')
    antwoord = str(input())
    if antwoord == 'nee':
        break