#Derivatives using Sympy
import sympy as sp

def der(F, vbl):
    D=sp.Derivative(F, vbl).doit()
    return(D)
    
expr1=input('Enter the function:  ')
v=input("Enter the variable of differentiation: ")

try:
    expr1=sp.sympify(expr1)
except:
    print("invalid function or input variable try again" )
else:
    v=sp.Symbol(v)
    d=der(expr1,v)
    sp.pprint(d)
    dim=expr1.atoms(sp.Symbol)
    print(dim)
if(len(dim) == 1):
    try:
       critpts=sp.solve(d)
       print("Critical Points")
       sp.pprint(critpts)
    except:
       print("Can't compute the critical points for the function.")
    r=input("Enter the plot range: ")
    r=float(r)
    plt= sp.plot(expr1,d, (v,-r,r), legend=True, show=False)
    plt[0].line_color='green'
    plt[1].line_color='red'
    plt.show()

    
