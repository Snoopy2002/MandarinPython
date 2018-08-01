##Compound interest using Sympy
import sympy as sp
from sympy import S


def AccountValue(P,r,n,t):
    A=P*(1+r/n)**(n*t)
    return(A)
    
P=input("Enter initial principal amount: ")
P=float(P)
r=input("Enter the rate of interest as a decimal: ")
r=float(r)
t=input("Enter the number of years the interest will be accrued: ")
t=int(t)
n=input("Enter the compounding periods: ")
n=int(n)
if(n > 100):
    P2=sp.Symbol('P2', positive=True)
    r2=sp.Symbol('r2', positive=True)
    t2=sp.Symbol('t2', positive=True)
    print(sp.Limit(P2*(1+r2/n)**(n*t2),n,S.Infinity).doit())
else:
    finalval=AccountValue(P,r,n,t)
    print("Final Account Value is: $", finalval)
