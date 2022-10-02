
import random #Biblioteca de funções aleatórias

palavras = ["computador", "viagem", "bola", "jogos", "brasil"]

palavra = random.choice(palavras)  #Escolher uma palavra aleatória 


tentativas = 0

chances = 5

letras_escolhidas = []

estado_atual = ["_"] * len(palavra)

print("Seja bem-vindo ao jogo da forca!!!")

print("Seu objetivo é tentar acertar a palavra secreta!") 

while tentativas < chances and ''.join(estado_atual) != palavra: 

    letra = input("\n\nQual letra você quer tentar? ")

    while letra in letras_escolhidas: 
        print("Você escolheu uma letra que já tinha tentado, escolha outra.")
        letra = input("\nQual letra você quer tentar? ")
    letras_escolhidas.append(letra) 

    if letra in palavra:
        print("Parabéns, você acertou a letra!")
        for i in range(len(palavra)):
            if letra == palavra[i]: 
                estado_atual[i] = letra 

    else:
        print("Que pena, você errou a letra!")
        tentativas += 1

#Quantas tentativas ainda tem?
    print(f"Você já fez {tentativas} tentativas e ainda tem {chances - tentativas} chances!")

#Qual o estato atual da palavra?
    print(f"Esse é o estado atual {estado_atual}.")

#Quais letras já tentou
    print(f"As letras que você já tentou são: ")
    for item in letras_escolhidas:
        print(item, end=" ")

if tentativas == chances:
    print("\n\nAcabaram suas tentativas! Você perdeu!!!")

else:
    print("\n\nVocê ganhou!!!")

print(f"A palavra era {palavra}.")  









