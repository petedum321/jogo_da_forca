# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 19:12:29 2024

@author: 21.00422-6
"""
from random import choice
import os

def imprime(ponto, certas, erradas, palavra):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("*************** Forca ***************")
    print("\n\nPalavra secreta: " + palavra + "\n\n")
    if ponto == 0:
        print("=======[_] \n|| | \n|| \n|| \n|| \n||\nHHHHHHHHHHHH")
    elif ponto == 1:
        print("=======[_] \n|| | \n|| o \n|| \n|| \n||\nHHHHHHHHHHHH")
    elif ponto == 2:
        print("=======[_] \n|| | \n|| o \n|| | \n|| \n||\nHHHHHHHHHHHH")
    elif ponto == 3:
        print("=======[_] \n|| | \n|| o \n|| /| \n|| \n||\nHHHHHHHHHHHH")
    elif ponto == 4:
        print("=======[_] \n|| | \n|| o \n|| /|\ \n|| \n||\nHHHHHHHHHHHH")
    elif ponto == 5:
        print("=======[_] \n|| | \n|| o \n|| /|\ \n|| / \n||\nHHHHHHHHHHHH")
    elif ponto == 6:
        print("=======[_] \n|| | \n|| o \n|| /|\ \n|| / \ \n||\nHHHHHHHHHHHH")
    print("\nLetras erradas:", erradas)
    print("Letras corretas:", certas)

def iniciaPalavra(tamanho):
    return '_' * tamanho

def sorteia():
    return choice(['cachorro', 'gato', 'galinha', 'cavalo', 'camelo', 'girafa',
                   'elefante', 'pirata', 'rato', 'arara', 'arame', 'familia',
                   'camisa', 'fazenda', 'cama', 'mesa', 'garfo', 'sapato',
                   'formiga', 'martelo', 'lagarto', 'lanche', 'copo', 'corpo',
                   'humano', 'laranja', 'pera', 'melancia', 'manteiga', 'sofa'])

def jogo_da_forca():
    palavra_secreta = sorteia()
    palavra_exibida = iniciaPalavra(len(palavra_secreta))
    letras_certas = ''
    letras_erradas = ''
    tentativas = 0
    max_tentativas = 6

    while True:
        imprime(tentativas, letras_certas, letras_erradas, palavra_exibida)

        if palavra_exibida == palavra_secreta:
            print("\nParabéns! Você venceu!")
            break
        elif tentativas == max_tentativas:
            print("\nVocê perdeu! A palavra era:", palavra_secreta)
            break

        letra = input("\nDigite uma letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, digite apenas uma letra válida.")
            continue

        if letra in letras_certas or letra in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        if letra in palavra_secreta:
            letras_certas += letra
            indices = [i for i, char in enumerate(palavra_secreta) if char == letra]
            for index in indices:
                palavra_exibida = palavra_exibida[:index] + letra + palavra_exibida[index+1:]
        else:
            letras_erradas += letra
            tentativas += 1

if __name__ == "__main__":
    jogo_da_forca()

