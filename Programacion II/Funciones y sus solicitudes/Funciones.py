#
#
#
#
#
def factorial(n):
      # Valorar si n vale algo
      
   if n == 1:
      return 1
      # Nalcular en factorial del numero
   elif n > 1:
      while n > 1:            
         return n*factorial(n-1)
   else:
      return False

