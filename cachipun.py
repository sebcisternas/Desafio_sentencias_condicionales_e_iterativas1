import sys
import random

computer_options = ['piedra','papel','tijera']

choice = str(input("Ingresa tu eleccion en el Cachipun, piedra , papel o tijera = "))
print("-------------------------------------------------------------------- \n")

if choice!="piedra" and choice!="papel" and choice!="tijera":
    print("Argumento inválido: Debe ser piedra, papel o tijera.")
    print("Programa Finalizado")
    sys.exit()
    
    

computer_choice = random.choice(computer_options)

print(f"Tu jugaste {choice}")
print(f"Computador jugo {computer_choice}")


if (choice == "piedra" and computer_choice == "piedra") or (choice == "papel" and computer_choice == "papel") or (choice == "tijera" and computer_choice == "tijera"):
    
    print("Empate")
    
elif (choice == "piedra" and computer_choice == "tijera") or (choice == "papel" and computer_choice == "piedra") or (choice == "tijera" and computer_choice == "papel"):
    
    print("Ganaste!!")
    
elif (choice == "piedra" and computer_choice == "papel") or (choice == "papel" and computer_choice == "tijera") or (choice == "tijera" and computer_choice == "piedra"):

    print("Perdiste :( ")