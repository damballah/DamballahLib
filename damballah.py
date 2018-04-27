import hashlib
import random
import os
# --- traitement de chaines --- #

def ClearScreen():
	os.system("cls")
	
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
	instabilite=0
	result_n=0
	result_p=0
	autoinc=0
	LaCC=""
	n=0
	
	while autoinc != nb_mesure:
		rnd=random.uniform(-1,1)
		mesure=gauche_de(str(rnd),1)
		if mesure=="-":
			result_n=result_n+1
		if mesure=="0":
			result_p=result_p+1
		autoinc=autoinc+1
	
	if result_n < result_p:
		instabilite=1
		LaCC="Blanc"
		n=n+1
	if result_n > result_p:
		instabilite=2
		LaCC="Noir"
		n=n+1
	if result_n==result_p:
		instabilite=3
		LaCC="Bleu"
		n=n+1
	
	print(" NB_MESURE : "+str(autoinc)+" --> "+str(result_n)+" -- "+str(result_p)+ " Couleur : " + LaCC)

	return instabilite

# Jeu du pendu
# ------------
def ChoixduMotAleat(fichier):
	nbligne=0
	i=0
	LeMot=""
	
	f = open(fichier,'r')
	for line in f:
		nbligne=nbligne+1
	f.close	
	
	x=random.randint(0,nbligne-1)
	
	f = open(fichier,'r')
	while i <= x:
		LeMot=f.readline()
		i=i+1
	f.close()
	
	return LeMot

def AffichageDuMotTroue(LeMot):
	NouvelAffichage=gauche_de(LeMot,1)
	longueur=len(LeMot)
	longueur=longueur-3
	
	nb_tiret=" _ " * longueur

	NouvelAffichage=NouvelAffichage+nb_tiret+droite_de(LeMot,2)
	
	return NouvelAffichage

	





