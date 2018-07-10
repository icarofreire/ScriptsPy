#!/usr/bin/python
# -*- coding: latin1 -*-

"""
	Programa do NOTIFICADOR DE PÁGINAS WEB
"""

import os
import sys
import time
import random
import urllib
import Image
import ImageChops
from urllib2 import urlopen
from datetime import datetime
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

def comparar_duas_imagens(im1, im2):
	imageA = Image.open(im1)
	imageB = Image.open(im2)
	return ImageChops.difference(imageA, imageB).getbbox() is None

def log(texto):
	log_arq_nome = "Log_nw.txt"
	if os.path.isfile(log_arq_nome) == False:
		arquivo_log = open(log_arq_nome, 'w')
		arquivo_log.write(texto+"\n")
	else:
		arquivo_log = open(log_arq_nome, 'a')
		arquivo_log.write(texto+"\n")
		
def hora():
	return str(datetime.now().hour)+":"+str(datetime.now().minute)
	
def data():
	return str(datetime.now().day)+"/"+str(datetime.now().month)+"/"+str(datetime.now().year)
	
def esperar_uma_hora():
	time.sleep(3600)
		
def analise_por_hora():
	while True:
		analisar()
		esperar_uma_hora()
				
class Screenshot(QWebView):
    def __init__(self):
        self.app = QApplication(sys.argv)
        QWebView.__init__(self)
        self._loaded = False
        self.loadFinished.connect(self._loadFinished)

    def capture(self, url, output_file):
        self.load(QUrl(url))
        self.wait_load()
        # set to webpage size
        frame = self.page().mainFrame()
        self.page().setViewportSize(frame.contentsSize())
        # render image
        image = QImage(self.page().viewportSize(), QImage.Format_ARGB32)
        painter = QPainter(image)
        frame.render(painter)
        painter.end()
        #print 'Salvo em:', output_file
        image.save(output_file)

    def wait_load(self, delay=0):
        # process app events until page loaded
        while not self._loaded:
            self.app.processEvents()
            time.sleep(delay)
        self._loaded = False

    def _loadFinished(self, result):
        self._loaded = True

pasta = "Prints"
s = Screenshot()
		
def tirar_foto(url, nome):
	primeiro_arquivo = pasta+"/"+nome+"/"+nome+".jpg"
	segundo_arquivo = pasta+"/"+nome+"/_"+nome+"_"+".jpg"
	if os.path.isdir(pasta) == False:
		os.mkdir(pasta)
	if os.path.isdir(pasta+"/"+nome) == False:
		os.mkdir(pasta+"/"+nome)
		s.capture(url, primeiro_arquivo)
		print "Primeiro registro: " + url
		log("Primeiro registro: " + url)
	else:
		if os.path.isfile(primeiro_arquivo) == True and os.path.isfile(segundo_arquivo) == False:
			s.capture(url, segundo_arquivo)
		elif os.path.isfile(segundo_arquivo) == True:
			os.unlink(primeiro_arquivo)
			os.rename(segundo_arquivo, primeiro_arquivo)
			s.capture(url, segundo_arquivo)
			
def enviar_POST(email, url):
	names_valores = urllib.urlencode({'email': email, 'mensagem': "Foi detectada uma alteração no seguinte site: "+url})
	try:
		html = urllib.urlopen("http://notificacaoweb.ueuo.com/email.php", names_valores).read()
		if html.find("OK!") != -1:
			return True
		else:
			return False
	except urllib.request.URLError:
		print "Erro ao acessar site: notificacaoweb.ueuo.com/email.php"		
		
def analisar():
	print "Verificando..."
	log("Verificação realizada às "+hora()+" do dia: "+data())
	try:
		linha = urlopen("http://notificacaoweb.ueuo.com/167437802566496955.php").read()
		for a in linha.split("<BR>"):
			email = a[a.find("[")+1:a.find("]")]
			url = a[a.find("{")+1:a.find("}")]
			nome = a[a.find("(")+1:a.find(")")]
			primeiro_arquivo = pasta+"/"+nome+"/"+nome+".jpg"
			segundo_arquivo = pasta+"/"+nome+"/_"+nome+"_"+".jpg"
			if (len(email)>0) and (len(url)>0) and (len(nome)>0):
				tirar_foto(url, nome)
				if (os.path.isfile(primeiro_arquivo) == True) and (os.path.isfile(segundo_arquivo) == True):
					if comparar_duas_imagens(primeiro_arquivo, segundo_arquivo) == False:
						if enviar_POST(email, url):
							print "Alteração Detectada: " + url + "\nEmail enviado para: " + email
							log("Alteração Detectada: " + url + "\nEmail enviado para: " + email)
							time.sleep(2)
	except urllib.request.URLError:
		print "Erro ao acessar site: notificacaoweb.ueuo.com/167437802566496955.php"
	print "..."
	log("---------------------------------------------------------------")


#-----------------------------------------------------------------#
analise_por_hora()
#-----------------------------------------------------------------#
