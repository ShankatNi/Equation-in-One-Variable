import math

def newFunc(intVari):
    newValue=(5/(intVari**2))+2
    #newValue=2**(-intVari)
    return newValue



def whileIter(p_0,Tol,N,i):
    while(i <= N):
        p= newFunc(p_0)
        if abs(p-p_0) < Tol:
            print("Sucessful procedure: p",i,"= ",p)
            print("Finally, absolute value of p",i," - p: ",abs(p-p_0))
            return p
        print("p",i,"= ",p)
        #print("absolute value of p",i," - p: ",abs(p-p_0))
        i=i+1
        p_0=p
    print("Failed",N)
    return False

def main():
    p_0=float(input("Enter initial p0: "))
    Tol=float(input("Enter Tolerance: "))
    N=int(input("Enter no of iteration: "))
    
    i=1
    whileIter(p_0,Tol,N,i)


main()
