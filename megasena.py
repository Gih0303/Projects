#Cada jogo da mega sena contém 6 números entre 1 e 60, sem repetições. 
from random import randint
guess = list()
play = list()
print("-" * 50)  
print(" Mega Sena ".center(50, "#")) 
print("-" * 50)   
amount = int(input("Quantos palpites deseja fazer? ")) 
total = 1 
while total <= amount:
    cont = 0 
    while True: 
        number = randint(1,60)  
        if number not in guess:
            guess.append(number) 
            cont += 1
        if cont >= 6: 
            break  
#Para ordenar os números da lista
    guess.sort() 
    play.append(guess[:]) 
    guess.clear()
    total += 1
print("-="*4, f" Sorteando {amount} jogos! ", "-="*4)    
for i, l in enumerate(play):
    print(f"Jogo {i+1}: {l}")