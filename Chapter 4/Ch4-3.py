#arithmetic series solver using Sympy Saha p.115
import sympy as sp

an=sp.Symbol('an')
a=sp.Symbol('a')
n=sp.Symbol('n')
d=sp.Symbol('d')
x1=input("Enter the nth term of the series as an: ")
x1=int(x1)
x2=input("Enter the number of terms, n: ")
x2=int(x2)
x3=input("Enter the first term: ")
x3=int(x3)
exp=a+(n-1)*d-an
exp=exp.subs(an, x1)
exp=exp.subs(n, x2)
exp=exp.subs(a, x3)
res=sp.solve(exp)
print("Common difference is: ", res)
print(exp)
S=0.5*(a+an)*d
S=S.subs(a,x3)
S=S.subs(an, x1)
S=S.subs(d, res[0])
print(S)

