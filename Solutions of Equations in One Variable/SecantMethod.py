import math

def newFunc(intVari):
    #newValue=intVari**3-2*intVari**2-5
    newValue=((intVari*math.exp(intVari))/(math.exp(intVari)-1))-1.5
    return newValue

def whileIter(p_0,p_1,Tol,N,i,q_0,q_1):
    while(i <= N):
        p= p_1-(q_1*(p_1-p_0))/(q_1-q_0)
        print('{0:2d}{1:20f}'.format(i,p))
        if abs(p-p_1) < Tol:
            print("Sucessful procedure: p",i,"= ",p)
            print("Finally, absolute value of p",i," - p: ",abs(p-p_1))
            return p
        #print("p",i,"= ",p)
        i=i+1
        p_0=p_1
        q_0=q_1
        p_1=p
        q_1=newFunc(p)
    print("Failed",N)
    return False

def main():
    p_0=float(input("Enter p_0: "))
    p_1=float(input("Enter p_1: "))
    Tol=float(input("Enter Tolerance: "))
    N=int(input("Enter max number: "))
    i=2
    q_0=newFunc(p_0)
    q_1=newFunc(p_1)
    print("-------------------------------------")
    print("           Secant Method         ")
    print("-------------------------------------")
    print('{0:1s}{1:15s}{2:12s}'.format(" ","n","p_n"))
    print('{0:2d}{1:20f}'.format(0,p_0))
    print('{0:2d}{1:20f}'.format(1,p_1))
    whileIter(p_0,p_1,Tol,N,i,q_0,q_1)



main()
