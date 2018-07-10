#!/usr/bin/python
# -*- coding: latin1 -*-
"""
Apaga todos os arquivos da pasta gerados pelo Make­file exceto os arquivos .py e .c;
Remove o modulo device driver.
"""

import os
import re

def nome_do_arquivo_c():
	dir_atual = os.getcwd()
	conteudos = os.listdir(dir_atual)
	for con in conteudos:
		if con[-2:] == ".c":
			arq = con
			break
	return arq[:-2]
	
def apagar_arquivos():
	ocu = ""
	dir_atual = os.getcwd()
	conteudos = os.listdir(dir_atual)
	for con in conteudos:
		ER1 = re.compile('^([a-z]+\.c)|([a-z]+\.py)$', re.I)
		ER1 = ER1.sub('.', con)
		ER2 = re.compile('^(\.[a-z-_]+)$', re.I)
		ER2 = ER2.sub('x', con)
		if ER1 != '.' and ER2 != 'x':
			os.unlink(dir_atual+"/"+con)
		if ER2 == 'x':
			ocu = con
	if len(ocu) > 0:
		nin = dir_atual+"/"+ocu
		for ap in os.listdir(nin):
			os.unlink(nin+"/"+ap)
		os.rmdir(dir_atual+"/.tmp_versions")

apagar_arquivos()
modulo = nome_do_arquivo_c()
os.system("sudo rmmod "+modulo)

