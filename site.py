#!/usr/bin/python
# -*- coding: latin1 -*-
"""
Baixar todas as imagens de um site(JPG).
"""
import os
import shutil

def deletar_arquivo(arq):
	os.remove(arq)

def copiar(alvo, destino):
	os.system("cp -r "+alvo+" "+destino)

def mover(alvo, destino):
	shutil.move(alvo, destino)
		
def deletar_diretorio(caminho):
	os.system("rm -r "+caminho)

pastas_livres = {
"Música":True,
"Pública":True,
"Documentos":True,
"NetBeansProjects":True,
"Notebooks":True,
"Modelos":True,
"Download":True,
"Ubuntu One":True,
"examples.desktop":True,
"eclipse":True,
"Público":True,
"MyDownloads":True,
"android-sdks":True,
"Vídeos":True,
"Imagens":True,
"Desktop":True,
"Downloads":True,
"Músicas":True,
"robocode":True,
"eclipse_c":True,
"public_html":True,
"scripts_py":True,
"icaro":True,
"jdownloader":True,
"amsn_received":True,
"netbeans-7.0.1":True,
"Fts":True
}


url = raw_input("URL: ")
if (len(url) > 0):
	os.system("wget -r -erobots=off -np \".jpg\" "+url)
	pasta = {}
	dir_atual = os.getcwd()
	conteudos = os.listdir(dir_atual)
	for con in conteudos:
		if con[0] != '.':
			pasta = con
			if os.path.isdir(pasta):
				if pastas_livres.get(pasta) == None:
					copiar(pasta,"Fts")
					deletar_diretorio(pasta)
else:
	print "Digite a URL"

"""				
url = raw_input("URL: ")
if (len(url) > 0):
	os.system("wget -r -erobots=off -np \".jpg\" "+url)
else:
	print "Digite a URL"
"""
