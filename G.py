#!/usr/bin/python
# -*- coding: latin1 -*-
"""
Gerar Arquivo Make­file;
Compilar Arquivo Make­file;
Carrega e visualiza o modulo no arquivo de log do sistema( /var/log/syslog )

**********
OBS: Só pode haver 1 arquivo .C dentro do diretório.
**********
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


def gerar_e_compilar_makefile():
	arq = nome_do_arquivo_c()
	mkfile = open("compilar","w")
	mkfile.write("KVER := $(shell uname -r)\n")
	mkfile.write("KDIR := /usr/src/linux-headers-$(KVER)\n")
	mkfile.write("PWD  := $(shell pwd)\n")
	mkfile.write("\n")
	mkfile.write("obj-m += "+arq+".o\n")
	mkfile.write("\n")
	mkfile.write("default:\n")
	mkfile.write("\t$(MAKE) -C $(KDIR) SUBDIRS=$(PWD) modules\n")
	mkfile.write("\n")
	mkfile.write("clean:\n")
	mkfile.write("\t@rm -Rf *.o *.ko *.mod.c modules.order Module.symvers Module.markers\n")
	mkfile.close()
	os.rename("compilar","Makefile")
	os.system("make") # compila o Makefile
	os.system("sudo insmod "+arq+".ko") # car­rega o módulo
	os.system("tail -f /var/log/syslog")



gerar_e_compilar_makefile()

