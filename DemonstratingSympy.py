#polynomial product using sympy and graphing
import sympy as sp

def productfn(exp1, exp2):
    prod=sp.expand(exp1*exp2)
    return(prod)
    
expr1=input('Enter the first polynomial:  ')
expr2=input('Enter the 2nd polynomial: ')
try:
    expr1=sp.sympify(expr1)
    expr2=sp.sympify(expr2)
except:
    print("invalid function input try again" )
else:
    x=sp.Symbol('x')
    pfunc=productfn(expr1, expr2)
    print(pfunc)
    plt= sp.plot(expr1,expr2,pfunc, (x,-5,5), legend=True, show=False)
    plt[0].line_color='green'
    plt[1].line_color='red'
    plt[2].line_color='blue'
    plt.show()
    
    
