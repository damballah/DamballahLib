from damballah import *

Cls()

print("")

AffichageDuTitreDuJeu()
Potence(11)

MotATrouver=ChoixduMotAleat("pendu.mot").upper()
# print(MotATrouver)

AfficheMot=AffichageDuMotTroue(MotATrouver).upper()
#print (AfficheMot)

Longueur=len("###################################################")

LeMotCentre=CentrerMot(AfficheMot,Longueur+1)
MotATrouver=CentrerMot(MotATrouver,Longueur)

print("")
print(CentrerMot("Mot à trouver",Longueur))
print(CentrerMot("-------------",Longueur))
print("")
print(LeMotCentre)
print("")
print("")

