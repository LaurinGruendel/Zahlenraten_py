 import random

durchgang = 0

ZufallsZahl = random.randint(1, 20)

 

spielername = input('Wie heißt du denn?')
 
Anfang = input('Willkomen bei Zahlenraten. Ich denke mir eine Zahl zwischen 1 und 20 und du erratets sie! Welchen Modus willst du spielen? [classic/temp.]')

if Anfang == 'classic':
    ClassicBool = True

if Anfang == 'temp.':
    TempBool = True


while ClassicBool:
    
    
    durchgang = durchgang + 1

    Eingabe = int(input('Hier Zahl eingeben: '))
    

    if Eingabe == ZufallsZahl:
        print('richtig erraten, ' + spielername + '!')
        print('---------------------------------')
        print('---------------------------------')
        print('            Versuche:            ')
        print(             durchgang             )
        print('---------------------------------')
        print('---------------------------------')
        RestartClassic = input('Nochmal spielen? [j/n]')



    if Eingabe > ZufallsZahl: 
        print('zu hoch ' + spielername + '!')

    if Eingabe < ZufallsZahl:
        print('zu niedrig ' + spielername + '!')











    