#                           Cajero automatico 
#============================Instrucciones======================================
#1. Simular un cajero automatico
#2. Gnerar un saldo al azar
#3. Nip establecido como 2025
#4. Maximo de 3 intentos antes de boquear la cuenta
#5. Ofrecer un menu de opciones
#      A. Cambiar el nip-->Pedir el nip-->cambiar-->confirmar el cambio
#      B. Retirar dinero
#      C. Depositar
#      D. Movimientos-->los ultimos 3 movimientos
#      E. Consultar el saldo
#      F. Salir
#6. Restricciones:
#      a. Nip incorrecto
#      b. Retiro: >100 & menor saldo & multiplos de 50
#      c. Depositos: Maximo de $25,000.00, exceso, retira el 10% de comision
#      d. 3 Movimientos (los ultimos) B & C.
#_______________________________________________________________________________
#importar librerias
import random
import math
#Generar el saldo al azar de la cuenta entre [3,800 & 4,600] & El NIP
saldo=int(random.randint(3800,4600))
nip=int(2025)
#
print("Bienvenido a CCVA del Bienestar ingrese su numero de cuenta")
ccid=input()
print("Hola cuenta: Guest", ccid,sep='_' )
print("ingresa tu NIP de 4 digitos a continuacion")
nipEn=int(input())
i=0
valid=1
movN=""
while nipEn!=nip:
    print("nip incorrecto porfavor ingrese de nuevo su NIP")
    if nipEn==nip:
        break  
    elif i==3:
        valid=0
        print("Demasiados intentos Saliendo de la sesion")
        break
    nipEn=int(input())
    i+=1  
#_______________________________________________________________________
if valid==1:
    print("Nip Correcto accediendo al menu...")
    while valid==1:
        print("Bienvenido al menu de CCVA del Bienestar.")
        print("Porfavor elija la accion que desee ejecutar y pulse [ENTER].")
        print("[1]Cambiar el Nip")
        print("[2]Retirar Dinero")
        print("[3]Depositar Dinero")
        print("[4]Consultar Saldo")
        print("[5]Consultar Movimientos")
        print("[9]Salir")
        select=int(input()) 
        # Empezar el Match para continuar con las opciones del cajero automatico
        match select:
            #Cambio de NIP
            case 1:
                nipEn=int(input("Porfavor, ingrese su NIP actual para continuar: ")) 
                i=0
                while i<3:
                    if nipEn==nip:
                        nipEn=int(input("Ingrese su nuevo NIP: "))
                        i+=1
                        if nipEn!=nip:
                            nip=int(input("Ingrese su nuevo NIP para confirmar los cambios: ")) 
                            if nip==nipEn:
                                print("Cambios confirmados volviendo al menu...")
                                print("")
                                break
                            nipEn=nip
                        elif nipEn==nip:
                            print("El nuevo NIP no puede ser igual que el anterior.")
                            print("")
                    else :
                        print("EL nip es incorrecto")
                        print("")
                        break
                i+=1  
## Retirar dinero          
            case 2:
                i=1
                while i==1:
                    print("Bienvenido al sistema de retiros")
                    retiro=int(input("Cuanto desea retirar?"))
                    if retiro<=saldo :
                        print("Ahora su saldo es: ",(saldo-retiro),".",sep="")
                        saldo=saldo-retiro
                        movN=movN+"Retiro de "+str(retiro)+". "
                        print(movN)
                        print("")
                        break
                    elif retiro>saldo:
                        print("Su retiro excede el maximo de creditos de la cuenta")
                        print("ingrese otra cantidad")
                    else:
                        print("Saliendo del servicio de Retiros")
                        print("")
                        break
## Depositar dinero
            case 3:
                i=1
                while i==1 :
                    print("Bienvenido al sistema de depositos")
                    transFer=input("Ingrese cuando dinero desea depositar?: ")
                    print("El deposito de: ",transFer," fue realizado con exito",sep='')
                    movN=movN+"Deposito a la cuenta de: "+transFer
                    print("Si desea volver al menu oprima [0] si desea hacer otra transferencia oprima [1]")
                    i=int(input())
                    print("")

## Consultar saldo
            case 4:
                print("Consulta de saldo")
                print("Su saldo total es de: ",saldo,sep="")
                print("")
## Conslutar movimientos
            case 5:
                if movN=="":
                    print("La cuenta no tiene movimientos registrados en esta sesion")
               else:
                    print("Movimientos de la cuenta ",monN,sep="")
                    print("")
## Salir del cajero
            case 9:
                break
else:
    print("Cerrando sesion en el cajero, siga invirtiendo en CCVA del Bienestar")
## Fin del programa
## Hecho por Kristopher
## LCC UNISON