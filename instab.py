#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
import random
from damballah import *

Mafenetre = Tk()
Mafenetre.title("Calcul d'instabilité")

Largeur = 485
Hauteur = 485
Canevas = Canvas(Mafenetre, width = Largeur, height =Hauteur, bg ='white')
LaVal_instab=1000
LaCouleur="True"

def active():
	if instab(LaVal_instab)=="True":
		LaCouleur="White"
	elif instab(LaVal_instab)=="False":
		LaCouleur="Black"
	elif instab(LaVal_instab)=="Egale":
		LaCouleur="Blue"
	else:
		LaCouleur=""
	return LaCouleur

def L16():
# C120
	CC=active()
	Canevas.create_rectangle(5, 5, 30, 30, outline='black',fill=CC)
# C121
	CC=active()
	Canevas.create_rectangle(32, 5, 60, 30, outline='black',fill=CC)
# C122
	CC=active()
	Canevas.create_rectangle(62, 5, 90, 30, outline='black',fill=CC)
# C123
	CC=active()
	Canevas.create_rectangle(92, 5, 120, 30, outline='black',fill=CC)
# C124
	CC=active()
	Canevas.create_rectangle(122, 5, 150, 30, outline='black',fill=CC)
# C125
	CC=active()
	Canevas.create_rectangle(152, 5, 180, 30, outline='black',fill=CC)
# C126
	CC=active()
	Canevas.create_rectangle(182, 5, 210, 30, outline='black',fill=CC)
# C127
	CC=active()
	Canevas.create_rectangle(212, 5, 240, 30, outline='black',fill=CC)
# C128
	CC=active()
	Canevas.create_rectangle(242, 5, 270, 30, outline='black',fill=CC)
# C129
	CC=active()
	Canevas.create_rectangle(272, 5, 300, 30, outline='black',fill=CC)
# C130
	CC=active()
	Canevas.create_rectangle(302, 5, 330, 30, outline='black',fill=CC)
# C131
	CC=active()
	Canevas.create_rectangle(332, 5, 360, 30, outline='black',fill=CC)
# C132
	CC=active()
	Canevas.create_rectangle(362, 5, 390, 30, outline='black',fill=CC)
# C133
	CC=active()
	Canevas.create_rectangle(392, 5, 420, 30, outline='black',fill=CC)
# C134
	CC=active()
	Canevas.create_rectangle(422, 5, 450, 30, outline='black',fill=CC)
# C135
	CC=active()
	Canevas.create_rectangle(452, 5, 480, 30, outline='black',fill=CC)

def L15():
# 105
	CC=active()
	Canevas.create_rectangle(18, 56, 44, 32, outline='black',fill=CC)
# 106
	CC=active()
	Canevas.create_rectangle(46, 56, 74, 32, outline='black',fill=CC)	
# 107
	CC=active()
	Canevas.create_rectangle(76, 56, 104, 32, outline='black',fill=CC)
# 108
	CC=active()
	Canevas.create_rectangle(106, 56, 134, 32, outline='black',fill=CC)
# 109
	CC=active()
	Canevas.create_rectangle(136, 56, 164, 32, outline='black',fill=CC)
# 110
	CC=active()
	Canevas.create_rectangle(166, 56, 194, 32, outline='black',fill=CC)
# 111
	CC=active()
	Canevas.create_rectangle(196, 56, 224, 32, outline='black',fill=CC)
# 112
	CC=active()
	Canevas.create_rectangle(226, 56, 254, 32, outline='black',fill=CC)
# 113
	CC=active()
	Canevas.create_rectangle(256, 56, 284, 32, outline='black',fill=CC)
# 114
	CC=active()
	Canevas.create_rectangle(286, 56, 314, 32, outline='black',fill=CC)
# 115
	CC=active()
	Canevas.create_rectangle(316, 56, 344, 32, outline='black',fill=CC)
# 116
	CC=active()
	Canevas.create_rectangle(346, 56, 374, 32, outline='black',fill=CC)
# 117
	CC=active()
	Canevas.create_rectangle(376, 56, 404, 32, outline='black',fill=CC)
# 118
	CC=active()
	Canevas.create_rectangle(406, 56, 434, 32, outline='black',fill=CC)
# 119
	CC=active()
	Canevas.create_rectangle(436, 56, 464, 32, outline='black',fill=CC)

def L14():
# 091
	CC=active()
	Canevas.create_rectangle(31, 82, 59, 58, outline='black',fill=CC)
# 092
	CC=active()
	Canevas.create_rectangle(61, 82, 89, 58, outline='black',fill=CC)
# 093
	CC=active()
	Canevas.create_rectangle(91, 82, 119, 58, outline='black',fill=CC)
# 094
	CC=active()
	Canevas.create_rectangle(121, 82, 149, 58, outline='black',fill=CC)
# 095
	CC=active()
	Canevas.create_rectangle(151, 82, 179, 58, outline='black',fill=CC)
# 096
	CC=active()
	Canevas.create_rectangle(181, 82, 209, 58, outline='black',fill=CC)
# 097
	CC=active()
	Canevas.create_rectangle(211,82 , 239, 58, outline='black',fill=CC)
# 098
	CC=active()
	Canevas.create_rectangle(241, 82, 269, 58, outline='black',fill=CC)
# 099
	CC=active()
	Canevas.create_rectangle(271, 82, 299, 58, outline='black',fill=CC)
# 100
	CC=active()
	Canevas.create_rectangle(301, 82, 329, 58, outline='black',fill=CC)
# 101
	CC=active()
	Canevas.create_rectangle(331, 82, 359, 58, outline='black',fill=CC)
# 102
	CC=active()
	Canevas.create_rectangle(361, 82, 389, 58, outline='black',fill=CC)
# 103
	CC=active()
	Canevas.create_rectangle(391, 82, 419, 58, outline='black',fill=CC)
# 104
	CC=active()
	Canevas.create_rectangle(421, 82, 449, 58, outline='black',fill=CC)

def L13():
# 078	
	CC=active()
	Canevas.create_rectangle(44, 108, 74, 84, outline='black',fill=CC)
# 079
	CC=active()
	Canevas.create_rectangle(76, 108, 104, 84, outline='black',fill=CC)
# 080
	CC=active()
	Canevas.create_rectangle(106, 108, 134, 84, outline='black',fill=CC)
# 081
	CC=active()
	Canevas.create_rectangle(136, 108, 164, 84, outline='black',fill=CC)
# 082
	CC=active()
	Canevas.create_rectangle(166, 108, 194, 84, outline='black',fill=CC)
# 083
	CC=active()
	Canevas.create_rectangle(196, 108, 224, 84, outline='black',fill=CC)
# 084
	CC=active()
	Canevas.create_rectangle(226, 108, 254, 84, outline='black',fill=CC)
# 085
	CC=active()
	Canevas.create_rectangle(256, 108, 284, 84, outline='black',fill=CC)
# 086
	CC=active()
	Canevas.create_rectangle(286, 108, 314, 84, outline='black',fill=CC)
# 087
	CC=active()
	Canevas.create_rectangle(316, 108, 344, 84, outline='black',fill=CC)
# 088
	CC=active()
	Canevas.create_rectangle(346, 108, 374, 84, outline='black',fill=CC)
# 089
	CC=active()
	Canevas.create_rectangle(376, 108, 404, 84, outline='black',fill=CC)
# 090
	CC=active()
	Canevas.create_rectangle(406, 108, 434, 84, outline='black',fill=CC)

def L12():
# 066
	CC=active()
	Canevas.create_rectangle(60, 134, 89, 110, outline='black',fill=CC)
# 067
	CC=active()
	Canevas.create_rectangle(91, 134, 120, 110, outline='black',fill=CC)
# 068
	CC=active()
	Canevas.create_rectangle(122, 134, 150, 110, outline='black',fill=CC)
# 069
	CC=active()
	Canevas.create_rectangle(152, 134, 180, 110, outline='black',fill=CC)
# 070
	CC=active()
	Canevas.create_rectangle(182, 134, 210, 110, outline='black',fill=CC)
# 071
	CC=active()
	Canevas.create_rectangle(212, 134, 240, 110, outline='black',fill=CC)
# 072
	CC=active()
	Canevas.create_rectangle(242, 134, 270, 110, outline='black',fill=CC)
# 073
	CC=active()
	Canevas.create_rectangle(272, 134, 300, 110, outline='black',fill=CC)
# 074
	CC=active()
	Canevas.create_rectangle(302, 134, 330, 110, outline='black',fill=CC)
# 075
	CC=active()
	Canevas.create_rectangle(332, 134, 360, 110, outline='black',fill=CC)
# 076
	CC=active()
	Canevas.create_rectangle(362, 134, 390, 110, outline='black',fill=CC)
# 077
	CC=active()
	Canevas.create_rectangle(392, 134, 420, 110, outline='black',fill=CC)

def L11():
# 055
	CC=active()
	Canevas.create_rectangle(76, 160, 104, 136, outline='black',fill=CC)
# 056
	CC=active()
	Canevas.create_rectangle(106, 160, 134, 136, outline='black',fill=CC)
# 057
	CC=active()
	Canevas.create_rectangle(136, 160, 164, 136, outline='black',fill=CC)
# 058
	CC=active()
	Canevas.create_rectangle(166, 160, 194, 136, outline='black',fill=CC)
# 059
	CC=active()
	Canevas.create_rectangle(196, 160, 224, 136, outline='black',fill=CC)
# 060
	CC=active()
	Canevas.create_rectangle(226, 160, 254, 136, outline='black',fill=CC)
# 061
	CC=active()
	Canevas.create_rectangle(256, 160, 284, 136, outline='black',fill=CC)
# 062
	CC=active()
	Canevas.create_rectangle(286, 160, 314, 136, outline='black',fill=CC)
# 063
	CC=active()
	Canevas.create_rectangle(316, 160, 344, 136, outline='black',fill=CC)
# 064
	CC=active()
	Canevas.create_rectangle(346, 160, 374, 136, outline='black',fill=CC)
# 065
	CC=active()
	Canevas.create_rectangle(376, 160, 404, 136, outline='black',fill=CC)
	
def L10():
# 045
	CC=active()
	Canevas.create_rectangle(92, 186, 119, 162, outline='black',fill=CC)
# 046
	CC=active()
	Canevas.create_rectangle(122, 186, 149, 162, outline='black',fill=CC)
# 047
	CC=active()
	Canevas.create_rectangle(152, 186, 179, 162, outline='black',fill=CC)
# 048
	CC=active()
	Canevas.create_rectangle(182, 186, 209, 162, outline='black',fill=CC)
# 049
	CC=active()
	Canevas.create_rectangle(212, 186, 239, 162, outline='black',fill=CC)
# 050
	CC=active()
	Canevas.create_rectangle(242, 186, 269, 162, outline='black',fill=CC)
# 051
	CC=active()
	Canevas.create_rectangle(272, 186, 299, 162, outline='black',fill=CC)
# 052
	CC=active()
	Canevas.create_rectangle(302, 186, 329, 162, outline='black',fill=CC)
# 053
	CC=active()
	Canevas.create_rectangle(332, 186, 359, 162, outline='black',fill=CC)
# 054
	CC=active()
	Canevas.create_rectangle(362, 186, 389, 162, outline='black',fill=CC)

def L09():
# 036
	CC=active()
	Canevas.create_rectangle(108, 212, 134, 188, outline='black',fill=CC)
# 037
	CC=active()
	Canevas.create_rectangle(137, 212, 164, 188, outline='black',fill=CC)
# 038
	CC=active()
	Canevas.create_rectangle(167, 212, 194, 188, outline='black',fill=CC)
# 039
	CC=active()
	Canevas.create_rectangle(197, 212, 224, 188, outline='black',fill=CC)
# 040
	CC=active()
	Canevas.create_rectangle(227, 212, 254, 188, outline='black',fill=CC)
# 041
	CC=active()
	Canevas.create_rectangle(257, 212, 284, 188, outline='black',fill=CC)
# 042
	CC=active()
	Canevas.create_rectangle(287, 212, 314, 188, outline='black',fill=CC)
# 043
	CC=active()
	Canevas.create_rectangle(317, 212, 344, 188, outline='black',fill=CC)
# 044
	CC=active()
	Canevas.create_rectangle(347, 212, 374, 188, outline='black',fill=CC)


def L08():
# 028
	CC=active()
	Canevas.create_rectangle(123, 238, 149, 214, outline='black',fill=CC)
# 029
	CC=active()
	Canevas.create_rectangle(152, 238, 179, 214, outline='black',fill=CC)
# 030
	CC=active()
	Canevas.create_rectangle(182, 238, 209, 214, outline='black',fill=CC)
# 031
	CC=active()
	Canevas.create_rectangle(212, 238, 239, 214, outline='black',fill=CC)
# 032
	CC=active()
	Canevas.create_rectangle(242, 238, 269, 214, outline='black',fill=CC)
# 033
	CC=active()
	Canevas.create_rectangle(272, 238, 299, 214, outline='black',fill=CC)
# 034
	CC=active()
	Canevas.create_rectangle(302, 238, 329, 214, outline='black',fill=CC)
# 035
	CC=active()
	Canevas.create_rectangle(332, 238, 359, 214, outline='black',fill=CC)

def L07():
# 021	
	CC=active()
	Canevas.create_rectangle(138, 264, 164, 240, outline='black',fill=CC)
# 022
	CC=active()
	Canevas.create_rectangle(167, 264, 194, 240, outline='black',fill=CC)
# 023
	CC=active()
	Canevas.create_rectangle(197, 264, 224, 240, outline='black',fill=CC)
# 024
	CC=active()
	Canevas.create_rectangle(227, 264, 254, 240, outline='black',fill=CC)
# 025
	CC=active()
	Canevas.create_rectangle(257, 264, 284, 240, outline='black',fill=CC)
# 026
	CC=active()
	Canevas.create_rectangle(287, 264, 314, 240, outline='black',fill=CC)
# 027
	CC=active()
	Canevas.create_rectangle(317, 264, 344, 240, outline='black',fill=CC)

def L06():
# 016	
	CC=active()
	Canevas.create_rectangle(153, 290, 179, 266, outline='black',fill=CC)
# 017
	CC=active()
	Canevas.create_rectangle(182, 290, 209, 266, outline='black',fill=CC)
# 018
	CC=active()
	Canevas.create_rectangle(212, 290, 239, 266, outline='black',fill=CC)
# 019
	CC=active()
	Canevas.create_rectangle(242, 290, 269, 266, outline='black',fill=CC)
# 020
	CC=active()
	Canevas.create_rectangle(272, 290, 299, 266, outline='black',fill=CC)
# 021
	CC=active()
	Canevas.create_rectangle(302, 290, 329, 266, outline='black',fill=CC)

def L05():
# 011	
	CC=active()
	Canevas.create_rectangle(167, 316, 194, 292, outline='black',fill=CC)
# 012
	CC=active()
	Canevas.create_rectangle(196, 316, 224, 292, outline='black',fill=CC)
# 013
	CC=active()
	Canevas.create_rectangle(226, 316, 254, 292, outline='black',fill=CC)
# 014
	CC=active()
	Canevas.create_rectangle(256, 316, 284, 292, outline='black',fill=CC)
# 015
	CC=active()
	Canevas.create_rectangle(286, 316, 314, 292, outline='black',fill=CC)

def L04():
# 007
	CC=active()
	Canevas.create_rectangle(180, 342, 209, 318, outline='black',fill=CC)
# 008
	CC=active()
	Canevas.create_rectangle(211, 342, 239, 318, outline='black',fill=CC)
# 009
	CC=active()
	Canevas.create_rectangle(241, 342, 269, 318, outline='black',fill=CC)
# 010
	CC=active()
	Canevas.create_rectangle(271, 342, 299, 318, outline='black',fill=CC)

def L03():
# 004
	CC=active()
	Canevas.create_rectangle(195, 368, 224, 344, outline='black',fill=CC)
# 005
	CC=active()
	Canevas.create_rectangle(226, 368, 254, 344, outline='black',fill=CC)
# 006
	CC=active()
	Canevas.create_rectangle(256, 368, 284, 344, outline='black',fill=CC)

def L02():

# 002
	CC=active()
	Canevas.create_rectangle(210, 394, 239, 370, outline='black',fill=CC)
# 003
	CC=active()
	Canevas.create_rectangle(241, 394, 269, 370, outline='black',fill=CC)

def L01():
# 001	
	CC=active()
	Canevas.create_rectangle(225, 421, 254, 396, outline='black',fill=CC)

# Premier affichage des cubes

L01()
L02()
L03()
L04()
L05()
L06()
L07()
L08()
L09()
L10()
L11()
L12()
L13()
L14()
L15()
L16()

# Canevas.pack(padx =5, pady =5)
Canevas.pack(padx =5, pady =5)

#BoutonLancer = Button(Mafenetre, text ='Vérifier', command = Cactif())
# Positionnement du widget avec la méthode pack()
# BoutonLancer.pack(side = LEFT, padx = 5, pady = 5)

Mafenetre.mainloop()









