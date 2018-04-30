import hashlib
import random
import os

# --- traitement de chaines --- #

def Cls():
	if os.sys.platform=="win32":
		os.system("cls")
	elif os.sys.platform=="linux":
		os.system("clear")
	
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

# Jeu du pendu ##############################
# ------------------------------------------#
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

def AffichageDuTitreDuJeu():
	L1="##################################################"
	L2="#                                                #"
	L3="#            Bienvenue au jeu du pendu           #"
	L4="#                  'Mode normal'                 #"
	L5="#                                   By Damballah #"
	L6="##################################################"
	print(L1)
	print(L2)
	print(L3)
	print(L4)
	print(L5)
	print(L6)

def CentrerMot(Mot,NbCarDansLigne):
	NbCarDansMot=len(Mot)
	NbEspace=int(NbCarDansLigne / 2 - (NbCarDansMot/2))
	Space=" " * NbEspace
	NouveauMotCentre=Space + Mot + Space
	return NouveauMotCentre

def AfficheGagnePerdu(resultat):
	if resultat==True:
		# L1="##################################################"
		L2="#                                                #"
		L3="#    ▓▓▓▓▓▓  ▓▓▓▓▓▓  ▓▓▓▓▓▓  ▓▓▓    ▓▓  ▓▓▓▓▓    #"
		L4="#    ▓       ▓    ▓  ▓       ▓▓ ▓   ▓▓  ▓        #"
		L5="#    ▓  ▓▓▓  ▓▓▓▓▓▓  ▓  ▓▓▓  ▓▓  ▓  ▓▓  ▓▓▓▓     #"
		L6="#    ▓    ▓  ▓    ▓  ▓    ▓  ▓▓   ▓ ▓▓  ▓        #"
		L7="#    ▓▓▓▓▓▓  ▓    ▓  ▓▓▓▓▓▓  ▓▓    ▓▓▓  ▓▓▓▓▓    #"
		L8="#                                                #"
		L9="##################################################"
		# print(L1)
		print(L2)
		print(L3)
		print(L4)
		print(L5)
		print(L6)
		print(L7)
		print(L8)
		print(L9)

	elif resultat==False:
		# L1="##################################################"
		L2="#                                                #"
		L3="#    ▓▓▓▓▓▓  ▓▓▓▓▓▓  ▓▓▓▓▓▓  ▓▓▓▓▓▓   ▓     ▓    #"
		L4="#    ▓    ▓  ▓       ▓    ▓   ▓   ▓▓  ▓     ▓    #"
		L5="#    ▓▓▓▓▓▓  ▓▓▓▓▓   ▓ ▓▓▓▓   ▓    ▓  ▓     ▓    #"
		L6="#    ▓       ▓       ▓   ▓    ▓   ▓▓  ▓▓   ▓▓    #"
		L7="#    ▓       ▓▓▓▓▓▓  ▓    ▓  ▓▓▓▓▓▓    ▓▓▓▓▓     #"
		L8="#                                                #"
		L9="##################################################"
		# print(L1)
		print(L2)
		print(L3)
		print(L4)
		print(L5)
		print(L6)
		print(L7)
		print(L8)
		print(L9)

		
		
def Potence(Level):
	if Level==0:
		#L1="##################################################"
		L2="#                                                #"
		L3="#                     POTENCE                    #"
		L4="#                     *******                    #"
		L5="#                                                #"
		L6="#                                                #"
		L7="#                                                #"
		L8="#                                                #"
		L9="#                                                #"
		L10="#                                                #"
		L11="#                                                #"
		L12="#                                                #"
		L13="#                                                #"
		L14="#                                                #"
		L15="#                                                #"
		L16="#                                                #"
		L17="#                                                #"
		L18="#                                                #"
		L19="#                                           0/11 #"
		L20="##################################################"
		#print(L1)
		print(L2)
		print(L3)
		print(L4)
		print(L5)
		print(L6)
		print(L7)
		print(L8)
		print(L9)
		print(L10)
		print(L11)
		print(L12)
		print(L13)
		print(L14)
		print(L15)
		print(L16)
		print(L17)
		print(L18)
		print(L19)
		print(L20)
	elif Level==1:
		#L1="##################################################"
		L2="#                                                #"
		L3="#                     POTENCE                    #"
		L4="#                     *******                    #"
		L5="#                                                #"
		L6="#                                                #"
		L7="#                                                #"
		L8="#                                                #"
		L9="#                                                #"
		L10="#                                                #"
		L11="#                                                #"
		L12="#                                                #"
		L13="#                                                #"
		L14="#                                                #"
		L15="#                                                #"
		L16="#                                                #"
		L17="#                                                #"
		L18="#               ///////////////////              #"
		L19="#                                           1/11 #"
		L20="##################################################"
		#print(L1)
		print(L2)
		print(L3)
		print(L4)
		print(L5)
		print(L6)
		print(L7)
		print(L8)
		print(L9)
		print(L10)
		print(L11)
		print(L12)
		print(L13)
		print(L14)
		print(L15)
		print(L16)
		print(L17)
		print(L18)
		print(L19)
		print(L20)
	elif Level==2:
		#L1="##################################################"
		L2="#                                                #"
		L3="#                     POTENCE                    #"
		L4="#                     *******                    #"
		L5="#                                                #"
		L6="#               //                               #"
		L7="#               //                               #"
		L8="#               //                               #"
		L9="#               //                               #"
		L10="#               //                               #"
		L11="#               //                               #"
		L12="#               //                               #"
		L13="#               //                               #"
		L14="#               //                               #"
		L15="#               //                               #"
		L16="#               //                               #"
		L17="#               //                               #"
		L18="#               ///////////////////              #"
		L19="#                                           2/11 #"
		L20="##################################################"
		#print(L1)
		print(L2)
		print(L3)
		print(L4)
		print(L5)
		print(L6)
		print(L7)
		print(L8)
		print(L9)
		print(L10)
		print(L11)
		print(L12)
		print(L13)
		print(L14)
		print(L15)
		print(L16)
		print(L17)
		print(L18)
		print(L19)
		print(L20)
	elif Level==3:
		#L1="##################################################"
		L2="#                                                #"
		L3="#                     POTENCE                    #"
		L4="#                     *******                    #"
		L5="#                                                #"
		L6="#               ///////////////////              #"
		L7="#               //                               #"
		L8="#               //                               #"
		L9="#               //                               #"
		L10="#               //                               #"
		L11="#               //                               #"
		L12="#               //                               #"
		L13="#               //                               #"
		L14="#               //                               #"
		L15="#               //                               #"
		L16="#               //                               #"
		L17="#               //                               #"
		L18="#               ///////////////////              #"
		L19="#                                           3/11 #"
		L20="##################################################"
		#print(L1)
		print(L2)
		print(L3)
		print(L4)
		print(L5)
		print(L6)
		print(L7)
		print(L8)
		print(L9)
		print(L10)
		print(L11)
		print(L12)
		print(L13)
		print(L14)
		print(L15)
		print(L16)
		print(L17)
		print(L18)
		print(L19)
		print(L20)
	elif Level==4:
		#L1="##################################################"
		L2="#                                                #"
		L3="#                     POTENCE                    #"
		L4="#                     *******                    #"
		L5="#                                                #"
		L6="#               ///////////////////              #"
		L7="#               //     //                        #"
		L8="#               //    //                         #"
		L9="#               //   //                          #"
		L10="#               //  //                           #"
		L11="#               // //                            #"
		L12="#               ////                             #"
		L13="#               //                               #"
		L14="#               //                               #"
		L15="#               //                               #"
		L16="#               //                               #"
		L17="#               //                               #"
		L18="#               ///////////////////              #"
		L19="#                                           4/11 #"
		L20="##################################################"
		#print(L1)
		print(L2)
		print(L3)
		print(L4)
		print(L5)
		print(L6)
		print(L7)
		print(L8)
		print(L9)
		print(L10)
		print(L11)
		print(L12)
		print(L13)
		print(L14)
		print(L15)
		print(L16)
		print(L17)
		print(L18)
		print(L19)
		print(L20)
	elif Level==5:
		#L1="##################################################"
		L2="#                                                #"
		L3="#                     POTENCE                    #"
		L4="#                     *******                    #"
		L5="#                                                #"
		L6="#               ///////////////////              #"
		L7="#               //     //   ||                   #"
		L8="#               //    //    ||                   #"
		L9="#               //   //     ||                   #"
		L10="#               //  //                           #"
		L11="#               // //                            #"
		L12="#               ////                             #"
		L13="#               //                               #"
		L14="#               //                               #"
		L15="#               //                               #"
		L16="#               //                               #"
		L17="#               //                               #"
		L18="#               ///////////////////              #"
		L19="#                                           5/11 #"
		L20="##################################################"
		#print(L1)
		print(L2)
		print(L3)
		print(L4)
		print(L5)
		print(L6)
		print(L7)
		print(L8)
		print(L9)
		print(L10)
		print(L11)
		print(L12)
		print(L13)
		print(L14)
		print(L15)
		print(L16)
		print(L17)
		print(L18)
		print(L19)
		print(L20)
	elif Level==6:
		#L1="##################################################"
		L2="#                                                #"
		L3="#                     POTENCE                    #"
		L4="#                     *******                    #"
		L5="#                                                #"
		L6="#               ///////////////////              #"
		L7="#               //     //   ||                   #"
		L8="#               //    //    ||                   #"
		L9="#               //   //    ××××                  #"
		L10="#               //  //    ( ^^ )                 #"
		L11="#               // //      (__)                  #"
		L12="#               ////                             #"
		L13="#               //                               #"
		L14="#               //                               #"
		L15="#               //                               #"
		L16="#               //                               #"
		L17="#               //                               #"
		L18="#               ///////////////////              #"
		L19="#                                           6/11 #"
		L20="##################################################"
		#print(L1)
		print(L2)
		print(L3)
		print(L4)
		print(L5)
		print(L6)
		print(L7)
		print(L8)
		print(L9)
		print(L10)
		print(L11)
		print(L12)
		print(L13)
		print(L14)
		print(L15)
		print(L16)
		print(L17)
		print(L18)
		print(L19)
		print(L20)
	elif Level==7:
		#L1="##################################################"
		L2="#                                                #"
		L3="#                     POTENCE                    #"
		L4="#                     *******                    #"
		L5="#                                                #"
		L6="#               ///////////////////              #"
		L7="#               //     //   ||                   #"
		L8="#               //    //    ||                   #"
		L9="#               //   //    ××××                  #"
		L10="#               //  //    ( ^^ )                 #"
		L11="#               // //      (__)                  #"
		L12="#               ////        &&                   #"
		L13="#               //          &&                   #"
		L14="#               //          &&                   #"
		L15="#               //          &&                   #"
		L16="#               //                               #"
		L17="#               //                               #"
		L18="#               ///////////////////              #"
		L19="#                                           7/11 #"
		L20="##################################################"
		#print(L1)
		print(L2)
		print(L3)
		print(L4)
		print(L5)
		print(L6)
		print(L7)
		print(L8)
		print(L9)
		print(L10)
		print(L11)
		print(L12)
		print(L13)
		print(L14)
		print(L15)
		print(L16)
		print(L17)
		print(L18)
		print(L19)
		print(L20)
	elif Level==8:
		#L1="##################################################"
		L2="#                                                #"
		L3="#                     POTENCE                    #"
		L4="#                     *******                    #"
		L5="#                                                #"
		L6="#               ///////////////////              #"
		L7="#               //     //   ||                   #"
		L8="#               //    //    ||                   #"
		L9="#               //   //    ××××                  #"
		L10="#               //  //    ( ^^ )                 #"
		L11="#               // //      (__)                  #"
		L12="#               ////        &&                   #"
		L13="#               //          &&                   #"
		L14="#               //          &&                   #"
		L15="#               //          &&                   #"
		L16="#               //             &                 #"
		L17="#               //             &&                #"
		L18="#               ///////////////////              #"
		L19="#                                           8/11 #"
		L20="##################################################"
		#print(L1)
		print(L2)
		print(L3)
		print(L4)
		print(L5)
		print(L6)
		print(L7)
		print(L8)
		print(L9)
		print(L10)
		print(L11)
		print(L12)
		print(L13)
		print(L14)
		print(L15)
		print(L16)
		print(L17)
		print(L18)
		print(L19)
		print(L20)
	elif Level==9:
		#L1="##################################################"
		L2="#                                                #"
		L3="#                     POTENCE                    #"
		L4="#                     *******                    #"
		L5="#                                                #"
		L6="#               ///////////////////              #"
		L7="#               //     //   ||                   #"
		L8="#               //    //    ||                   #"
		L9="#               //   //    ××××                  #"
		L10="#               //  //    ( ^^ )                 #"
		L11="#               // //      (__)                  #"
		L12="#               ////        &&                   #"
		L13="#               //          &&                   #"
		L14="#               //          &&                   #"
		L15="#               //          &&                   #"
		L16="#               //        &    &                 #"
		L17="#               //       &&    &&                #"
		L18="#               ///////////////////              #"
		L19="#                                           9/11 #"
		L20="##################################################"
		#print(L1)
		print(L2)
		print(L3)
		print(L4)
		print(L5)
		print(L6)
		print(L7)
		print(L8)
		print(L9)
		print(L10)
		print(L11)
		print(L12)
		print(L13)
		print(L14)
		print(L15)
		print(L16)
		print(L17)
		print(L18)
		print(L19)
		print(L20)
	elif Level==10:
		#L1="##################################################"
		L2="#                                                #"
		L3="#                     POTENCE                    #"
		L4="#                     *******                    #"
		L5="#                                                #"
		L6="#               ///////////////////              #"
		L7="#               //     //   ||                   #"
		L8="#               //    //    ||                   #"
		L9="#               //   //    ××××                  #"
		L10="#               //  //    ( ^^ )                 #"
		L11="#               // //      (__)                  #"
		L12="#               ////        &&_                  #"
		L13="#               //          && \                 #"
		L14="#               //          &&  \_               #"
		L15="#               //          &&                   #"
		L16="#               //        &    &                 #"
		L17="#               //       &&    &&                #"
		L18="#               ///////////////////              #"
		L19="#                                          10/11 #"
		L20="##################################################"
		#print(L1)
		print(L2)
		print(L3)
		print(L4)
		print(L5)
		print(L6)
		print(L7)
		print(L8)
		print(L9)
		print(L10)
		print(L11)
		print(L12)
		print(L13)
		print(L14)
		print(L15)
		print(L16)
		print(L17)
		print(L18)
		print(L19)
		print(L20)
	elif Level==11:
		#L1="##################################################"
		L2="#                                                #"
		L3="#                     POTENCE                    #"
		L4="#                     *******                    #"
		L5="#                                                #"
		L6="#               ///////////////////              #"
		L7="#               //     //   ||                   #"
		L8="#               //    //    ||                   #"
		L9="#               //   //    ××××                  #"
		L10="#               //  //    ( ^^ )                 #"
		L11="#               // //      (__)                  #"
		L12="#               ////       _&&_                  #"
		L13="#               //        / && \                 #"
		L14="#               //      _/  &&  \_               #"
		L15="#               //          &&                   #"
		L16="#               //        &    &                 #"
		L17="#               //       &&    &&                #"
		L18="#               ///////////////////              #"
		L19="#                                          11/11 #"
		L20="##################################################"
		#print(L1)
		print(L2)
		print(L3)
		print(L4)
		print(L5)
		print(L6)
		print(L7)
		print(L8)
		print(L9)
		print(L10)
		print(L11)
		print(L12)
		print(L13)
		print(L14)
		print(L15)
		print(L16)
		print(L17)
		print(L18)
		print(L19)
		print(L20)
