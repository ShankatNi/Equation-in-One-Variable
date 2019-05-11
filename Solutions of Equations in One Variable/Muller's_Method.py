import math

def newFunc(x):
    #newValue=x**4+x**3+3*x**2+2*x+2
    #newValue=(x**4)-(3*(x**3))+(x**2)+x+1
    #newValue=3*(x**3)-(13*(x**2))+19*x-5
    newValue=x**3-2*(x**2)-5
    return newValue

def MuFunc(p_0,p_1,p_2):
    myList=list()
    h_1=p_1-p_0
    h_2=p_2-p_1
    delta_1=(newFunc(p_1)-newFunc(p_0))/h_1
    delta_2=(newFunc(p_2)-newFunc(p_1))/h_2
    d=(delta_2-delta_1)/(h_2+h_1)
    myList.append([h_1,h_2,delta_1,delta_2,d])
    return myList


def whileIter(p_0,p_1,p_2,Tol,N,i):
    bigList=list()
    newList=list()
    newList=MuFunc(p_0,p_1,p_2)
    while(i <= N):
        b=newList[0][3]+newList[0][1]*newList[0][4]
        D=(b**2-(4*newFunc(p_2)*newList[0][4]))**0.5
        if abs(b-D) < abs(b+D):
            E=b+D
        else:
            E=b-D
        h=((-2)*newFunc(p_2))/E
        p=p_2+h
        print('{0:2d}{1:20f}'.format(i,p))
        #print(newFunc(p))
        if abs(h) < Tol:
            print("Sucessful procedure: p",i,"= ",p)
            print("Finally, absolute value of p",i," - p: ",abs(p-p_0))
            return p
        p_0=p_1
        p_1=p_2
        p_2=p
        newList=MuFunc(p_0,p_1,p_2)
        i=i+1
    print("Failed",N)
    return False

def main():
    p_0=1    #float(input("Enter the p0:"))
    p_1=2   #float(input("Enter the p1:"))
    p_2=0+1j   #float(input("Enter the p2:"))
    Tol=float(input("Enter Tolerance: "))
    N=1000  #int(input("Enter no of iteration: "))
    print("-------------------------------------")
    print("          Muller's Method         ")
    print("-------------------------------------")
    print('{0:1s}{1:15s}{2:12s}'.format(" ","n","p_n"))
    i=3
    whileIter(p_0,p_1,p_2,Tol,N,i)


main()
