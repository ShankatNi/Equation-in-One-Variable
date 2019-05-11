import math

def newFunc(x):
    #newValue=math.cos(x)
    newValue=x-2**(-x)
    return newValue


def whileIter(p_0,Tol,N,i):
    while(i <= N):
        p_1=newFunc(p_0)
        p_2=newFunc(p_1)
        p=(p_0-(p_1-p_0)**2)/(p_2-2*p_1+p_0)
        print('{0:2d}{1:20f}'.format(i,p))
        if abs(p-p_0) < Tol:
            print("Sucessful procedure: p",i,"= ",p)
            print("Finally, absolute value of p",i," - p: ",abs(p-p_0))
            return p
        i=i+1
        p_0=p
    print("Failed",N)
    return False

def main():
    p_0=float(input("Enter initial p0: "))
    Tol=float(input("Enter Tolerance: "))
    N=1000    #int(input("Enter no of iteration: "))
    print("-------------------------------------")
    print("           Aitken's Method          ")
    print("-------------------------------------")
    print('{0:1s}{1:15s}{2:12s}'.format(" ","n","p_n"))
    i=1
    whileIter(p_0,Tol,N,i)


main()
