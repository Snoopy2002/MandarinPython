#polynomial product using sympy and graphing
import sympy as sp

def product(exp1, exp2):
    prod=sp.expand(exp1*exp2)
    return(prod)
    
def subtract(exp1,exp2):
    result=sp.expand(exp1-exp2)
    return(result)

def add(exp1,exp2):
    result=sp.expand(exp1+exp2)
    return(result)

def divide(exp1,exp2):
    result=sp.cancel(exp1/exp2)
    return(result)
    
    
expr1=input('Enter the first polynomial:  ')
expr2=input('Enter the 2nd polynomial: ')
try:
    expr1=sp.sympify(expr1)
    expr2=sp.sympify(expr2)
except:
    print("invalid function input try again" )
else:
    x=sp.Symbol('x')
    pfunc=product(expr1, expr2)
    '''
    pfunc2=subtract(expr1,expr2)
    pfunc3=add(expr1,expr2)
    pfunc4=divide(expr1,expr2)
    sp.pprint(pfunc)
    
    sp.pprint(pfunc2)
    sp.pprint(pfunc3)
    sp.pprint(pfunc4)
    '''
    plt= sp.plot(expr1,expr2,pfunc, (x,-5,5), legend=True, show=False)
    plt[0].line_color='green'
    plt[1].line_color='red'
    plt[2].line_color='blue'
    plt.show()
    
    
