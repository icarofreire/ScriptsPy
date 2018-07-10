#!/usr/bin/python
# -*- coding: latin1 -*-
def ler(n_ou_s):
	import sys; 
	if n_ou_s == "n": return int(sys.stdin.readline())
	if n_ou_s == "s": return sys.stdin.readline()[0:-1]

def abrir_browser(url):
	import webbrowser
	webbrowser.open(url,2)

# converter conjuntos de instruções de um programa assembly NASM para GNU Assembly (GAS);

import sys
import os
import signal

if len(sys.argv)==2:
	os.chdir("/home/icaro/Desktop/ASM")
	os.system("intel2gas -i " + sys.argv[1] + " > temp.asm")
	if os.path.isfile("temp.asm") == True:
		flag = False
		f = open("temp.asm")
		for linha in f:
			l = linha.rstrip()
			if (l.find("_start:")!=-1):
				flag = True
				print "__asm__ ("
				
			if flag and (l.find("_start:")==-1) and (len(l.strip())>0):
				print "\"" + l.strip() + ";\""
		f.close()
		print ");"
		os.unlink("temp.asm")
else:
	print "Escreva o nome do arquivo assembly como argumento do programa.\nEx: "+sys.argv[0]+" arquivo.asm"
