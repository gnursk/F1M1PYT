print ("Hello you!, Nick")
print ("Wie ben jij?")
name = input ("Hello + name")
print ("Hello" + name)

import datetime
import os

x = datetime.datetime.now()
print ("de tijd en datum zijn:")
print (x)


input()
print ("Hallo, ik ben Nick. ik ben een nieuwkomer op het mediacollege.")
print ("Ik heb een paar multiple choice vragen voor jou om mij beter te leren kennen\n\n")
d1 = input ("Waar woon ik? \nA Amsterdam\nB Lelystad \nC Enkhuizen \nHier typen: " )
if d1 == "A" or d1 == "a":
    print ("Ik woon niet in Amsterdam, ik moet ongeveer een uur met de trein naar Amsterdam.")
    d1 = input("Woon ik in \nB Lelystad \nC Enkhuizen?\nHier typen: ")
    if d1 == "B" or d1 == "b":
        print ("Nee, ik woon ik Enkhuizen, ik woon hier al mijn hele leven.\n\n")
    if d1 == "C" or d1 == "c":
        print ("Ik woon inderdaad in Enkhuizen, ik woon hier al mijn hele leven.\n\n")
elif d1 == "B" or d1 == "b":
    print ("Ik woon niet in Lelystad, Lelystad ligt ongeveer een half uur weg bij mij")
    d1 = input ("woon ik in \nA Amsterdam \nC Enkhuizen?\n\nHier typen:")
    if d1 == "A" or d1 == "a":
        print ("Nee, ik woon ik Enkhuizen, ik woon hier al mijn hele leven.\n\n")
    elif d1 == "C" or d1 == "c":
        print ("Nee, ik woon in Enkhuizen, ik woon hier al mijn hele leven.\n\n")
elif d1 == "C" or d1 == "c":
    print ("Ik woon inderdaad in Enkhuizen, ik woon hier al mijn hele leven.\n\n")



print ("De volgende vraag is: ")
d2 = input ("hoe oud ben ik? \nA 15\nB 16\nC 17\nHier typen: \n" )
if d2 == "A" or d2 == "a":
    print ("Nee ik ben geen 15")
    d2 = input("Ben ik \nB 16  \nC 17\nHier typen: ")
    if d2 == "B" or d2 == "b":
        print ("Ik ben inderdaad 16, ik ben geboren op 22 juli 2005.")
    elif d2 == "C" or d2 == "c":
        print ("nee, ik ben 16.")
elif d2 == "B" or d2 == "b":
    print ("Ik ben inderdaad 16, ik ben geboren op 22 juli 2005.")
elif d2 == "C" or d2 == "c":
    print ("Nee, ik ben geen 17.")
    d2 = input("Ben ik \nA 15  \nB 16\n")
    if d2 == "A" or d2 == "a":
        print ("Nee, ik ben 16, ik ben geboren op 22 juli 2005")
    if d2 == "B" or d2 == "b":
        print ("Ik ben inderdaad 16")
    
print ("De laatste vraag:\n\n")
d3 = input ("Wat wil ik bereiken met deze opleiding? \nA Niks\nB software developer \nC Game developer \nHier typen: " )
if d3 == "A" or d3 == "a":
    print ("Wow, verwacht je echt zo weinig van mij? Bestwel jammer.\n")
    d3 = input("Wat wil ik worden na deze opleiding \nB software developer \nC game developer\nHier typen: ")
    if d3 == "B" or d3 == "b":
        print ("Nee, ik wil graag een game developer worden\n\n")
    if d3 == "C" or d3 == "c":
        print ("Ik wil inderdaad game developer worden\n\n")
elif d3 == "B" or d3 == "b":
    print ("Ik wil geen software developer worden.")
    d3 = input ("Wat wil ik doen met deze opleiding \nA Niks \nC Gamedeveloper\n\nHier typen:")
    if d3 == "A" or d3 == "a":
        print ("Nee, ik wil graag game developer worden.\n\n")
    elif d3 == "C" or d3 == "c":
        print ("Nee, ik wil graag game developer worden.\n\n")
elif d3 == "C" or d3 == "c":
    print ("Ik wil inderdaad game developer worden.\n\n")

print ("Bedankt voor het deelnemen aan deze quiz, succes met het leven.")
