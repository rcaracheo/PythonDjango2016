#!/usr/bin/env python
#-*-coding:utf-8-*-
from time import sleep
import random

sus="-" * 35
depo=["piedra","papel","tijera"]
while True:
	x=raw_input("¿Qué elijes? piedra, papel o tijera: ")
	if x not in depo:
		print("No hagas trampa!!")
		continue

	pc=random.choice(depo)
	sleep(0.5)
	print(("Computadora elijio {}.").format(pc))
	if x == pc:
		print ("\n Empate.")
	elif x == "piedra" and pc == "tijera":
		print ("\n Ganaste")
	elif x == "papel" and pc == "piedra":
		print ("\n Ganaste")
	elif x == "tijera" and pc == "papel":
		print ("\n Ganaste")
	else:
		print ("perdiste {} gana {} \n".format(pc, x))
	print (sus)