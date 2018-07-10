#!/usr/bin/python
# -*- coding: latin1 -*-
"""
Substitui todos os hexadecimais por números decimais equivalentes de um programa assembly.
"""
import re
import sys

if len(sys.argv)==2:
	if sys.argv[1][-3:] == "asm":
		f = open(sys.argv[1])
		c = open(sys.argv[1][:-4]+"_DEC.asm", 'w')
		for linha in f:
			ll = linha.rstrip()
			for n in re.findall("0x[A-Fa-f0-9]+",ll):
				ll = ll.replace(n, str(int(n , 16)))
			c.write(ll+"\n")
		f.close()
		c.close()
		print "Arquivo '"+sys.argv[1][:-4]+"_DEC.asm'"+" criado."
	else:
		print "O arquivo inserido não é um arquivo .asm"
else:
	print "Escreva o nome do arquivo assembly como argumento do programa.\nEx: "+sys.argv[0]+" arquivo.asm"
