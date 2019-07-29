#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from os import system
from time import sleep

texto = "Python é uma linguagem de programação de alto nível,[4] interpretada, de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991.[1] Atualmente possui um modelo de desenvolvimento comunitário, aberto e gerenciado pela organização sem fins lucrativos Python Software Foundation. Apesar de várias partes da linguagem possuírem padrões e especificações formais, a linguagem como um todo não é formalmente especificada. O padrão de facto é a implementação CPython. A linguagem foi projetada com a filosofia de enfatizar a importância do esforço do programador sobre o esforço computacional. Prioriza a legibilidade do código sobre a velocidade ou expressividade. Combina uma sintaxe concisa e clara com os recursos poderosos de sua biblioteca padrão e por módulos e frameworks desenvolvidos por terceiros. "
#texto.encode('utf-8')
comeco = 0
fim = 30
while fim < len(texto):
	comeco += 1
	fim += 1
	system('clear')
	sleep(0.2)
	print("|{}|".format(texto[comeco:fim]))
