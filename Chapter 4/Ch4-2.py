#equation solver using Sympy Saha p.115
import sympy as sp
import math

def Solve(ex1, ex2): #solve for the intersection points of the two equations
    num=sp.degree(ex1, gen=x) #determine degree to order  the new polynomial for solving
    num2=sp.degree(ex2, gen=x)
    if(num > num2): #if first poly higher degree than second
        ex3=ex1-ex2
        print("Intersection equation is: ", ex3)
        k=sp.solve(ex3)
    else:  #if second polynomial higher degree than the first
        ex3=ex2-ex1
        print("Intersection Equation is: ", ex3)
        k=sp.solve(ex3 )
    return(k)

print("Program to find the intersection of any two polynomials.")
print("Enter polynomial powers of x as x**n where n is the power of x" )
expr1=input('Enter a polynomial in terms of x and y:  ')
expr2=input("Enter another polynomial in terms of x and y: ")
x=sp.Symbol('x')
y=sp.Symbol('y')
try:
   F1=sp.sympify(expr1) #convert first function to python symbolic
   F2=sp.sympify(expr2) #convert second function to python expression
except:
    print("Can't convert input to a Python function, invalid input try again" )
else:
    S=Solve(F1, F2) #call Solver function
    i=0
    for i in range(len(S)):
         value=sp.N(S[i],6)
         if(isinstance(value, complex)==False):
              print("Solution is: ", value)    
    sol1=sp.solve(F1,'y') #solve in terms of y both funtions for plotting
    sol2=sp.solve(F2,'y')
    p1=sol1[0]
    p2=sol2[0]
    plt= sp. plot(p1,p2,(x,-5,5), legend=True, show=False)  #plot the two functions
    plt[0].line_color='green'
    plt[1].line_color='red'
    plt.show()
    
    
