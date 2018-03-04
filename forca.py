# -*- coding: utf-8 -*-
from random import randint
import os

def PALAVRAOCULTA(palavraOculta):
	retornoPalavra =""
	for x in xrange(0,len(palavraOculta)):
		retornoPalavra +=palavraOculta[x]
	return retornoPalavra

def DICA(dica):
	retornoDica=""
	for x in xrange(0,len(dica)):
		retornoDica+=dica[x]

	return retornoDica


listaDePalavras=["Acidente","carro","naruto","Respeito","haltere","perry o onitorrinco","yu gi oh","todo mundo odeia o cris","alquimista","Helio","xablau","macaco voador","chevrolet ford da silva"]
listaDeDicas=["aquilo que ocorre inesperadamente","meio de trasnporte","anime","Conssentimento que leva alguém a considerar outro ser","Instrumento de ginastica","personagem de chapeu","jogo de cartas","seriado","quimica","Deus sol","bicho vermelho","musica que o leo canta","nome estranho"]

indice =randint(0,len(listaDePalavras)-1)

palavra = listaDePalavras[indice]
dica = listaDeDicas[indice]
palavraOculta=[]

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
##Oucutando a palavra
for x in xrange(0,len(palavra)):
	if palavra[x] in alfabeto:
		palavraOculta.append("*")
	else:
		palavraOculta.append(palavra[x])

contPerdeu=0
validacao=0
chutes=""

while validacao <= len(palavra)+2 and contPerdeu <=6:
#mostrando a interface
	if contPerdeu == 0:
		os.system("clear")
		print"||----------|-|      Palavra:",

		print PALAVRAOCULTA(palavraOculta)

		print"||----------|||      Chutes:",

		print chutes
		print"||           |       Dica:",

		print DICA(dica)


		print"||           |"
		print"||           |"
		print"||"
		print"||"
		print"||"
		print"||"
		print"||"
		print"||"
		print"||"
		print"||"
		print"||"
		print"||__________________"

	if contPerdeu == 1:
		os.system("clear")
		print"||----------|-|      Palavra:",

		print PALAVRAOCULTA(palavraOculta)
		print"||----------|||      Chutes:",

		print chutes
		print"||           |       Dica:",

		print DICA(dica)

		print"||           |   -----------"
		print"||           |  - SOCORRO -"
		print"||         (-_-)- ---------"
		print"||          "
		print"||         "
		print"||          "
		print"||         "
		print"||        "
		print"|| "
		print"|| "
		print"||                 "
		print"||__________________"

	if contPerdeu ==2:
		os.system("clear")
		print"||----------|-|      Palavra:",

		print PALAVRAOCULTA(palavraOculta)
		print"||----------|||      Chutes:",

		print chutes
		print"||           |       Dica:",

		print DICA(dica)

		print"||           |   -----------"
		print"||           |  - SOCORRO -"
		print"||         (-_-)- ---------"
		print"||           |"
		print"||           | "
		print"||           |"
		print"||         "
		print"||        "
		print"|| "
		print"|| "
		print"||                 "
		print"||__________________"

	if contPerdeu == 3:
		os.system("clear")
		print"||----------|-|      Palavra:",

		print PALAVRAOCULTA(palavraOculta)

		print"||----------|||      Chutes:",

		print chutes
		print"||           |       Dica:",

		print DICA(dica)

		print"||           |   -----------"
		print"||           |  - SOCORRO -"
		print"||         (-_-)- ---------"
		print"||          /|"
		print"||         / |"
		print"||           |"
		print"||         "
		print"||        "
		print"|| "
		print"|| "
		print"||                 "
		print"||__________________"

	if contPerdeu == 4:
		os.system("clear")

		print"||----------|-|      Palavra:",

		print PALAVRAOCULTA(palavraOculta)

		print"||----------|||      Chutes:",

		print chutes
		print"||           |       Dica:",

		print DICA(dica)

		print"||           |   -----------"
		print"||           |  - SOCORRO -"
		print"||         (-_-)- ---------"
		print"||          /|\\"
		print"||         / | \\"
		print"||           |"
		print"||         "
		print"||        "
		print"|| "
		print"|| "
		print"||                 "
		print"||__________________"

	if contPerdeu == 5:
		os.system("clear")
		print"||----------|-|      Palavra:",

		print PALAVRAOCULTA(palavraOculta)

		print"||----------|||      Chutes:",

		print chutes
		print"||           |       Dica:",

		print DICA(dica)

		print"||           |   -----------"
		print"||           |  - SOCORRO -"
		print"||         (-_-)- ---------"
		print"||          /|\\"
		print"||         / | \\"
		print"||           |"
		print"||          / "
		print"||         /  "
		print"|| "
		print"|| "
		print"||                 "
		print"||__________________"


	if contPerdeu == 6:
		os.system("clear")

		print"||----------|-|      Palavra:",

		print PALAVRAOCULTA(palavraOculta)
		print"||----------|||      Chutes:",

		print chutes
		print"||           |       Dica:",

		print DICA(dica)

		print"||           |       palavra certa:",
		print palavra
		print"||           |  "
		print"||         (x_x)    \\    /   ----   |    |   |----   -----      /\\      |---- "
		print"||          /|\\      \\  /   |    |  |    |   |    |  |         /  \\     |    |"
		print"||         / | \\      |     |    |  |    |   |    |  |---     / _ _\\    |    |"
		print"||           |        |     |    |  |    |   |    |  |       /      \\   |    |"
		print"||          / \\       |      ----    ----    |____|  -----  /        \\  |____|"
		print"||         /   \\      "
		print"|| "
		print"|| "
		print"||                 "
		print"||__________________ by: Leo Jaimesson _|_--0_0--_|_"
		break


	print "1 para dizer uma letra"
	print"2 para dizer a palavra"
	resposta = input()
#conferindo o que o usuario digitou

	
	if resposta == 1:
		print"letra"
		entrada = raw_input()
#conferindo se letra existe
		if entrada.lower() in palavra or entrada.upper() in palavra:
			chutes+=entrada
			for x in xrange(0,len(palavra)):

				if entrada.lower() == palavra[x] or entrada.upper() == palavra[x]:
					palavraOculta[x] = palavra[x]
					validacao+=1

		else:
			contPerdeu+=1
			chutes += entrada
	
	else:
		print"palavra"
		entrada2 = raw_input()
#conferindo se palavra esta certo
		if entrada2.upper() == palavra.upper():
			os.system("clear")
			print"                                                                               "
			print"                                                                      "
			print"                                                                    "
			print"   \\  /   ----  |    |    \\       /\\        /  |  |\\        /  "
			print"    \\/   |    | |    |     \\     /  \\      /   |  | \\      /   "
			print"     |   |    | |    |      \\   /    \\    /    |  |  \\    /     "
			print"     |   |    | |    |       \\ /      \\  /     |  |   \\  /      "
			print"     |    ----   ----         /        \\/      |  |    \\/        "
			print"                                                                   "
			print"     by: Leo Jaimesson \('-')/"
			break
		else:
			contPerdeu+=1
