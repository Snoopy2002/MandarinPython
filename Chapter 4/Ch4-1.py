#Factor Finder Saha p. 115

import sympy as sp

F1=input("Enter a polynomial: ")
try:
      expr=sp.sympify(F1)
except:
      print("Invalid input must enter the polynomial again.")
else:
      result=sp.factor(expr)
      sp.pprint(result)
      
    
