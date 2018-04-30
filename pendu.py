from damballah import *

Cls()

print("")

AffichageDuTitreDuJeu()
Potence(0)

MotATrouver=ChoixduMotAleat("pendu.mot").upper()
# print(MotATrouver)

AfficheMot=AffichageDuMotTroue(MotATrouver).upper()
#print (AfficheMot)

Longueur=len("###################################################")

LeMotCentre=CentrerMot(AfficheMot,Longueur+1)
MotATrouver=CentrerMot(MotATrouver,Longueur)

#gagne=True
#AfficheGagnePerdu(gagne)

print("")
print(CentrerMot("Mot à trouver",Longueur))
print(CentrerMot("-------------",Longueur))
print("")
print(LeMotCentre)
print("")
print("")

while True:
    char = Keypressed()
     #if (char == "p"):
    print(char)
    exit(0)
