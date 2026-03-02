from Automovil import Automovil
import random

auto=[]

for _ in range(10):
   auto.append(Automovil.crear_auto_random())

for a in auto:
   print(a)

print(auto[4]>auto[5])