#Continuity of a Function Saha #1 p.205
import sympy as sp
import math

delta=.00000001
expr1=input('Enter a function:  ')
expr2=input('Enter the variable name: ')
try:
    expr1=sp.sympify(expr1)
    expr2=sp.Symbol(expr2)
except:
    print("invalid function input try again" )
else:
    point=input("Enter a point to check the continuity at:")
    point=int(point)
    L1=sp.Limit(expr1,expr2,point,dir='-').doit()
    L2=sp.Limit(expr1, expr2, point,dir='+').doit()
    print(L1, L2)
    if(L1==L2):
        print(expr2, " is continuous at ", point)
        plt = sp.plot(expr1, legend=True, show=False)  #plot the function
        plt.line_color='green'
        plt.show()
    else:
        print(expr2, " is not continous at ", point)
        plt = sp.plot(expr1, legend=True, show=False)  #plot the function
        plt.line_color='green'
        plt.show()