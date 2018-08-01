#this program will take any most inequalities in x and solve it, printing the equation and the solution

import sympy as sp
import math

def iSolve(exprn1):
    OK=0
    if(exprn1.is_polynomial() == True): #solve polynomial inequality
        x=sp.Symbol('x')
        ineq_obj=exprn1
        lhs=ineq_obj.lhs
        p=sp.Poly(lhs,x)
        rel=ineq_obj.rel_op
        n=sp.solve_poly_inequality(p,rel)
        print("Expression: ", exprn1, "has solution: ", n)
        OK=1
    elif(exprn1.is_rational_function() == True): #solve rational inequality
        x=sp.Symbol('x')
        ineq_obj=exprn1
        lhs=ineq_obj.lhs
        num, denom = lhs.as_numer_denom()
        p1=sp.Poly(num)
        p2=sp.Poly(denom)
        rel=ineq_obj.rel_op
        k=sp.solve_rational_inequalities([[((p1,p2),rel)] ])
        print("Expression: ", exprn1, "has solution: ", k)
        OK=1
    else:
        x=sp.Symbol('x')
        ineq_obj =exprn1
        t=sp.solve_univariate_inequality(ineq_obj, x, relational=False)
        print("Expression: ", exprn1, "has solution: ", t)
        OK=1
    return(OK)
 ###########################################################    
print("Program to solve an inequality.")
print("Enter polynomial powers of x as x**n where n is the power of x" )
expr1=input('Enter a polynomial :  ')
try:
   ck=0 
   F1=sp.sympify(expr1) #convert first function to python symbolic
   ck=iSolve(F1)
   if(ck == 1):
       print(" ")
   else:
        print("Error in the solution.")
except:
    print("Can't convert input to a Python function, invalid input try again" )