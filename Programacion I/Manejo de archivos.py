#
#
#
#
#
import random

while True:
   with open('NewText.txt','a') as f:
      bin=input("Ingresa el nombre del paciente: ")
            #
      f.write(bin,". ")
      if bin=="":
         break
            #
      nib=input("Ahora ingresa la edad del paciente: ")
      f.write(nib)
      if not nib:
         nib=random.randint(0,100)
         f.write(str(nib),". ")
            #
with open('NewText.txt') as f:
      print(f.read())


