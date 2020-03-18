#!/usr/bin/python3
import os

print("")
print("   ▐ ▄ • ▌ ▄ ·.  ▄▄▄·  ▄▄▄·         ▄▄▄· ▄• ▄▌▄▄▄▄▄      • ▌ ▄ ·.  ▄▄▄· ▄▄▄▄▄▄▄▄ .·▄▄▄▄    ")
print("  •█▌▐█·██ ▐███▪▐█ ▀█ ▐█ ▄█        ▐█ ▀█ █▪██▌•██  ▪     ·██ ▐███▪▐█ ▀█ •██  ▀▄.▀·██▪ ██   ")
print("  ▐█▐▐▌▐█ ▌▐▌▐█·▄█▀▀█  ██▀·        ▄█▀▀█ █▌▐█▌ ▐█.▪ ▄█▀▄ ▐█ ▌▐▌▐█·▄█▀▀█  ▐█.▪▐▀▀▪▄▐█· ▐█▌  ")
print("  ██▐█▌██ ██▌▐█▌▐█ ▪▐▌▐█▪·•        ▐█ ▪▐▌▐█▄█▌ ▐█▌·▐█▌.▐▌██ ██▌▐█▌▐█ ▪▐▌ ▐█▌·▐█▄▄▌██. ██   ")
print("  ▀▀ █▪▀▀  █▪▀▀▀ ▀  ▀ .▀            ▀  ▀  ▀▀▀  ▀▀▀  ▀█▄▀▪▀▀  █▪▀▀▀ ▀  ▀  ▀▀▀  ▀▀▀ ▀▀▀▀▀•   ")  
print("")

# NMAP AUTOMATED
print("Selecciona la IP destino:")
ipDestino = input()

# Funciones nmap:
def GetNMAP1 (ipDestino):
    command = "nmap -sV -p80,443 " + ipDestino
    startProcess = os.popen(command)
    results = str(startProcess.read())

    return results

def GetNMAP2 (ipDestino):
    command = "nmap -sV -sC -A " + ipDestino
    startProcess = os.popen(command)
    results = str(startProcess.read())

    return results

def GetNMAP3 (ipDestino):
    command = "nmap --top-ports 20 --open " + ipDestino
    startProcess = os.popen(command)
    results = str(startProcess.read())

    return results

def GetNMAP4 (ipDestino):
    command = "nmap -sS -A -sV -O -p- " + ipDestino
    startProcess = os.popen(command)
    results = str(startProcess.read())

    return results

def GetNMAP5 (ipDestino):
    command = "nmap -sU " + ipDestino
    startProcess = os.popen(command)
    results = str(startProcess.read())

    return results
# Final funciones nmap:

def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Elige una opcion: "))
            correcto=True
        except ValueError:
            print("Error, elige una opcion")
    
    
    return num
 
salir = False
opcion = 0


while not salir:
    
    print("------------------------------")
    print("------------------------------")
    print ("1. NMAP apps web")   # --> nmap -sV -p80,443 → puertos 80/443
    print ("2. NMAP versiones + scripts por defecto + agresivo")    # --> nmap -sV (version) -sC (scripts por defecto) -A (agresivo)
    print ("3. NMAP puertos comunes no cerrados/filtrados")     # --> nmap --top-ports 20 --open
    print ("4. NMAP versiones y sistema operativo TODOS LOS PUERTOS")     # --> nmap -sS -A -sV -O -p-
    print ("5. NMAP UDP")   # --> nmap -sU
    print ("6. Salir")
    print("------------------------------")
    print("------------------------------")

    print ("") 
    
 
    opcion = pedirNumeroEntero()
 
    if opcion == 1:
        print ("Ha seleccionado NMAP apps web")
        print(GetNMAP1(ipDestino))
    elif opcion == 2:
        print ("Ha seleccionado NMAP versiones + scripts por defecto + agresivo")
        print(GetNMAP2(ipDestino))
    elif opcion == 3:
        print("Ha seleccionado NMAP puertos comunes no cerrados/filtrados")
        print(GetNMAP3(ipDestino))
    elif opcion == 4:
        print("Ha seleccionado NMAP versiones y sistema operativo TODOS LOS PUERTOS")
        print(GetNMAP4(ipDestino))
    elif opcion == 5:
        print("Ha seleccionado NMAP UDP")
        print(GetNMAP5(ipDestino))
    elif opcion == 6:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 5")
 
print ("Saliendo...")