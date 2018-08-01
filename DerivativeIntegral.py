#Derivatives and Integrals using Sympy
import sympy as sp

def der(F, vbl):
    D=sp.Derivative(F, vbl).doit()
    return(D)
def Int(F, vbl):
    I=sp.Integral(F, vbl).doit()
    return(I)
    
expr1=input('Enter the function:  ')
v=input("Enter the variable :")
try:
    expr1=sp.sympify(expr1)
except:
    print("invalid function or input variable try again" )
else:
    v=sp.Symbol(v)
    d=der(expr1,v)
    ITGR=Int(expr1,v)
    print("Derivative ")
    sp.pprint(d)
    print("Integral")
    sp.pprint(ITGR)
    r=input("Enter the plot range as an integer (max to min): ")
    r=float(r)
    plt= sp.plot(expr1,d, ITGR, (v,-r,r), legend=True, show=False)
    plt[0].line_color='green'
    plt[1].line_color='red'
    plt.show()

    
