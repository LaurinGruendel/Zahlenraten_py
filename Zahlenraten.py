import random


def main():


    durchgang = 0


    ZufallsZahl = random.randint(1, 20)

    spielername = input('Wie heißt du denn?')

    Anfang = input(f'Willkomen bei Zahlenraten {spielername}. Ich denke mir eine Zahl zwischen 1 und 20 und du errätst sie! Welchen Modus willst du spielen? [classic/temp.(schwierig)]')

    if Anfang == 'Easter Egg':
        print('Ich sehe was, was Du nicht siehst – nämlich gut aus.')

    if Anfang == 'classic':
        
        while True:
                

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
                neustart = input('Nochmal spielen? [j/n]')

                
                
                if neustart == 'j':
                    durchgang = 0
                    ZufallsZahl = random.randint(1, 20)

                else:
                    print('Danke fürs spielen ' + spielername + ' !')
                    break


            elif Eingabe > ZufallsZahl: 
                print('zu hoch ' + spielername + '!')


            else:
                print('zu niedrig ' + spielername + '!')

    if Anfang == 'temp':
        durchgang = 0

        ZufallsZahl = random.randint(1, 20)
        

        while True:


            
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
                neustart = input('Das hat doch Spaß gemacht! Nochmal spielen? [j/n]')

                if neustart == 'j':
                    print('Okay ' + spielername + ' und noch eine Runde!')
                    durchgang = 0
                    ZufallsZahl = random.randint(1, 20)

                else:
                    print('Danke fürs spielen, ' + spielername + ' !')
                    break



            elif Eingabe == ZufallsZahl + 1:
                print('Sehr Heiß, ' + spielername + ' !')

            elif Eingabe == ZufallsZahl - 1:
                print('Sehr Heiß, ' + spielername + ' !')

            elif Eingabe == ZufallsZahl + 2:
                print('heiß,' + spielername + ' !')

            elif Eingabe == ZufallsZahl - 2:
                print(f"'heiß, {spielername} !")

            elif Eingabe == ZufallsZahl + 3:
                print('warm,' + spielername + ' !')

            elif Eingabe == ZufallsZahl - 3:
                print('warm,' + spielername + ' !')

            else:
                print('kalt,' + spielername + ' !')
main()