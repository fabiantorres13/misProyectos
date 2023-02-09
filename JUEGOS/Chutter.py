# Con este juego podré jugar piedra, papel o tijera con el computador o con otra persona

import random
import sys
from time import sleep
import emoji
import getpass


def juegoCpu():
        
        print("")
        print('\U0001F6A9'+' Comienza el juego!')
        print("")
        armas = "\U0000270A Piedra,\n\U0000270B Papel,\n\U0000270C  Tijera\n\U000023F1  1,2,3...!"
        for c in armas:
                print(c, end='')
                sys.stdout.flush()
                sleep(0.1)
        print("")
        print("")
        print('\U0001F4E3'+' ¡Ahora!')
        

        while True:

                cpu = random.choice(['Piedra','Papel','Tijera'])
                print("")
                usuario = input("\U0001F466 Tú: ")
                print(f'\U0001F4BB CPU: {str(cpu)}')

                if usuario.lower() == cpu.lower():
                        print("Ambos han lanzado igual. Vuelvan a lanzar!")
                        continue
                elif usuario.lower() == "piedra" and cpu.lower() == "tijera":
                        print("--------------------------")
                        return "\U0001F3C6 Has Ganado!"
                elif usuario.lower() == "tijera" and cpu.lower() == "papel":
                        print("--------------------------")
                        return "\U0001F3C6 Has Ganado!"
                elif usuario.lower() == "papel" and cpu.lower() == "piedra":
                        print("--------------------------")
                        return "\U0001F3C6 Has Ganado!"
                elif usuario.lower() == "tijera" and cpu.lower() == "piedra":
                        print("--------------------------")
                        return "\U0001F62D Has Perdido..."
                elif usuario.lower() == "papel" and cpu.lower() == "tijera":
                        print("--------------------------")
                        return "\U0001F62D Has Perdido..."
                elif usuario.lower() == "piedra" and cpu.lower() == "papel":
                        print("--------------------------")
                        return "\U0001F62D Has Perdido..."
                elif (usuario.lower() != "piedra" or usuario.lower() != "papel" or usuario.lower() != "tijera"):
                        print("\U0001F6A8 : Haz escrito erroneamente. Vuelve a lanzar!")
                        print("--------------------------")
                        continue




def juego2p():
        print("")
        print('\U0001F6A9'+' Comienza el juego!')
        print("")
        armas = "\U0000270A Piedra,\n\U0000270B Papel,\n\U0000270C  Tijera\n\U000023F1  1,2,3...!"
        for c in armas:
                print(c, end='')
                sys.stdout.flush()
                sleep(0.1)
        print("")
        print("")
        print('\U0001F4E3'+' ¡Ahora!')
        

        while True:
                
                print("")
                usuario1 = getpass.getpass("- 1P: ")
                usuario2 = getpass.getpass("- 2P: ")
 
                if usuario1.lower() == usuario2.lower():
                        print("Ambos han lanzado igual. Vuelvan a lanzar!")
                        continue
                elif usuario1.lower() == "piedra" and usuario2.lower() == "tijera":
                        print("--------------------------")
                        return "\U0001F3C6 1P Ha Ganado!"
                elif usuario1.lower() == "tijera" and usuario2.lower() == "papel":
                        print("--------------------------")
                        return "\U0001F3C6 1P Ha Ganado!"
                elif usuario1.lower() == "papel" and usuario2.lower() == "piedra":
                        print("--------------------------")
                        return "\U0001F3C6 1P Ha Ganado!"
                elif usuario1.lower() == "tijera" and usuario2.lower() == "piedra":
                        print("--------------------------")
                        return "\U0001F3C6 2P Ha Ganado!"
                elif usuario1.lower() == "papel" and usuario2.lower() == "tijera":
                        print("---------------------------")
                        return "\U0001F3C6 2P Ha Ganado!"
                elif usuario1.lower() == "piedra" and usuario2.lower() == "papel":
                        print("--------------------------")
                        return "\U0001F3C6 2P Ha Ganado!"
                elif (usuario1.lower() != "piedra" or usuario1.lower() != "papel" or usuario1.lower() != "tijera") or (usuario2.lower() != "piedra" or usuario2.lower() != "papel" or usuario2.lower() != "tijera"):
                        print("\U0001F6A8 : Alguno de los jugadores ha escrito erroneamente. Vuelvan a lanzar!")
                        print("----------------------------------------------------------------------------")
                        continue

def juego():

        print("")
        print("")
        print('\U0001F917'+" Bienvenido a Chutter")
        

        while True:
                
                oponente = input("\U00002753 Modo de Juego (CPU/2P): ")


                if oponente.lower() == "cpu":
                        print(juegoCpu())

                elif oponente.lower() == "2p":
                        print(juego2p())
  
                else:
                        print("\U00002757 Opción no válida.")
                        continue

                while True:
                        salir = input("\U00002753 Escribe R para reiniciar la partida, M para ir al menú o S para salir del programa: ")

                        if salir.lower() == "r" and oponente.lower() == "cpu":
                                print(juegoCpu())
                                continue
                        elif salir.lower() == "r" and oponente.lower() == "2p":
                                print(juego2p())
                                continue
                        elif salir.lower() == "m":
                                print(juego())
                                break
                        elif salir.lower() == "s":
                                print("")
                                adios = "\U0001F44B Cerrando el programa..."
                                for c in adios:
                                        print(c, end='')
                                        sys.stdout.flush()
                                        sleep(0.05)
                                print("")
                                print("")
                                creditos = "-- De Fabián con \U00002764  para tu"
                                for i in creditos:
                                        print(i, end='')
                                        sys.stdout.flush()
                                        sleep(0.05)
                                print("")
                                print("")
                                sys.exit()
                        else:
                                print("\U00002757 Opción no válida.")
                                continue

               
                        
    
juego()



    


