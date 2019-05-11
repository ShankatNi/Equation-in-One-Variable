import math

def newFunc(x):   
    funcValue=x**3+x-1
    funcDeri=3*(x**2)+1
    #funcValue=1-4*x*math.cos(x)+2*x**2+math.cos(2*x)
    #funcDeri=4*x-4*math.cos(x)+4*x*math.sin(x)-2*math.sin(2*x)
    newValue=x-(funcValue/funcDeri)
    return newValue

def whileIter(p_0,Tol,N,i):
    while(i <= N):
        p=newFunc(p_0)
        #print("No of steps: ",i,"Value p",i,"- p",p-p_0)
        print('{0:2d}{1:20f}'.format(i,p))
        if abs(p-p_0) < Tol:
            print("Sucessful procedure: p",i,"= ",p)
            #print("Finally, absolute value of p",i," - p: ",abs(p-p_0))
            return p
        i=i+1
        p_0=p
    print("Failed",N)
    return False

def main():
    p_0=float(input("Enter initial p0: "))
    Tol=float(input("Enter Tolerance: "))
    N=1000  #int(input("Enter no of iteration: "))
    print("-------------------------------------")
    print("           Newtons's Method          ")
    print("-------------------------------------")
    print('{0:1s}{1:15s}{2:12s}'.format(" ","n","p_n"))
    i=1
    whileIter(p_0,Tol,N,i)


main()
