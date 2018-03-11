#!/usr/bin/env python
# -*- coding: utf-8 -*-

def droite_de (chaine,nbcar) :
	droite_de = chaine[-nbcar:]
	return droite_de

def gauche_de (chaine,nbcar) :
	gauche_de = chaine[:nbcar]
	return gauche_de

def milieu_de (chaine,debut,longueur):
	milieu_de = chaine[debut:debut+longueur]
	return milieu_de
