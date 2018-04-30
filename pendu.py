from damballah import *
import time

Cls()

print("")

AffichageDuTitreDuJeu()

i=0
k=""
while i<=11:
	Cls()
	AffichageDuTitreDuJeu()
	Potence(i)
	i=i+1
	time.sleep(.200)

MotATrouver=ChoixduMotAleat("pendu.mot").upper()
# print(MotATrouver)

AfficheMot=AffichageDuMotTroue(MotATrouver).upper()
#print (AfficheMot)

Longueur=len("###################################################")

LeMotCentre=CentrerMot(AfficheMot,Longueur+1)
MotATrouver=CentrerMot(MotATrouver,Longueur)

gagne=True
AfficheGagnePerdu(gagne)

print("")
print(CentrerMot("Mot à trouver",Longueur))
print(CentrerMot("-------------",Longueur))
print("")
print(LeMotCentre)
print("")
print("")


	
	
