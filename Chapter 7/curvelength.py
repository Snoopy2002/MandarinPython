#Length of a Curve Saha P.208
import sympy as sp

def curvelength(b, a, x, fx): #computes the minimum value of the function
        F = sp.sqrt(1+(fx*fx))
        print(F)
        res=sp.Integral(fx,(x,a,b)).doit()
        return res
    
######mainpart of program    
expr1=input('Enter a function:  ')
expr2=input('Enter the variable name: ')
try:
    expr1=sp.sympify(expr1)
    expr2=sp.Symbol(expr2)
except:
    print("invalid function input try again" )
else:
        expr1der=sp.Derivative(expr1, expr2).doit() #compute derivative for gradient descent
        upper=input("Enter the upper integral limit: ")
        lower=input("Enter the lower integral limit: ")
        upper=float(upper)
        lower=float(lower)
        res=curvelength(upper, lower, expr2, expr1der)
        print("The line integral is: ", res, " units"+)
        plt = sp.plot(expr1, legend=True, show=False)  #plot the function
        plt.line_color='green'
        plt.show()
  