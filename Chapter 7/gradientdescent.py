#Gradient descent method Saha P.206
import sympy as sp

global d 
delta=.00000001 #difference between old and new
global stepsize
stepsize=0.001

def gradient_des(x0, Fx, x): #computes the minimum value of the function
    xold=x0
    xnew=xold-stepsize*Fx.subs({x:xold}).evalf()
    while abs(xold-xnew) > delta:
        xold=xnew
        xnew=xold-stepsize*Fx.subs({x:xold}).evalf()
    return xnew
    
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
        initguess=input("Enter the initial guess for the function minimum: ")
        initguess=float(initguess)
        minval=gradient_des(initguess, expr1der, expr2)
        yminval=expr1.subs({expr2:minval}).evalf()
        print("Minimum value of the function is x= ", minval, "y= ", yminval)
        plt = sp.plot(expr1, legend=True, show=False)  #plot the function
        plt.line_color='green'
        plt.show()
  