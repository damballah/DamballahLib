#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import random

# --- traitement de chaines --- #

def droite_de (chaine,nbcar) :
	droite_de = chaine[-nbcar:]
	return droite_de

def gauche_de (chaine,nbcar) :
	gauche_de = chaine[:nbcar]
	return gauche_de

def milieu_de (chaine,debut,longueur):
	milieu_de = chaine[debut:debut+longueur]
	return milieu_de

# --- cryptographie --- #

def gensha256(chaine):
	if isinstance(chaine,str)==True:
		r=hashlib.sha256(chaine.encode())
		r=r.hexdigest()
	elif isinstance(chaine,int)==True:
			chaine=str(chaine)
			r=hashlib.sha256(chaine.encode())
			r=r.hexdigest()
	else:
		r="[ERREUR gensha256: type de variable attendu = 'str' ou 'int']"
	return r

# --- calcul d'instabilité --- #

def instab(nb_mesure):
	instabilite="False"
	n=0
	result_n=0
	result_p=0
	autoinc=0
	LaCC=""

	while autoinc != nb_mesure:
		rnd=random.uniform(-1,1)
		mesure=gauche_de(str(rnd),1)
		if mesure=="-":
			result_n=result_n+1
		if mesure=="0":
			result_p=result_p+1
		autoinc=autoinc+1
	
	if result_n < result_p:
		instabilite="True"
		LaCC="Blanc"
	if result_n > result_p:
		instabilite="False"
		LaCC="Noir"
	if result_n==result_p:
		instabilite="Egale"
		LaCC="Bleu"

	print(str(autoinc)+" --> "+str(result_n)+" -- "+str(result_p)+ " Couleur : " + LaCC)

	return instabilite








