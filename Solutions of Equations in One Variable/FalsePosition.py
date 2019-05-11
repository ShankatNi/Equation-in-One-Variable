import math

def newFunc(intVari):
    newValue=((intVari*math.exp(intVari))/(math.exp(intVari)-1))-1.5
    #newValue=math.exp(intVari)+2**(-intVari)+2*math.cos(intVari)-6
    return newValue

def whileIter(p_0,p_1,Tol,N,i,q_0,q_1):
    while(i <= N):
        p= p_1-(q_1*(p_1-p_0))/(q_1-q_0)
        print('{0:2d}{1:20f}'.format(i,p))
        if abs(p-p_1) < Tol:
            print("Sucessful procedure: p",i,"= ",p)
            print("Finally, absolute value of p",i," - p: ",abs(p-p_1))
            return p
        #print("Value of p",i," - p: ",p-p_1)
        i=i+1
        q=newFunc(p)
        if q*q_1<0:
            p_0=p_1
            q_0=q_1
        p_1=p;
        q_1=q
    print("Failed",N)
    return False

def main():
    p_0=float(input("Enter initial p0: "))
    p_1=float(input("Enter second p1: "))
    Tol=float(input("Enter Tolerance: "))
    N=int(input("Enter no of iteration: "))
    print("-------------------------------------")
    print("           False Position         ")
    print("-------------------------------------")
    print('{0:1s}{1:15s}{2:12s}'.format(" ","n","p_n"))
    i=2
    q_0=newFunc(p_0)
    q_1=newFunc(p_1)
    print('{0:2d}{1:20f}'.format(0,p_0))
    print('{0:2d}{1:20f}'.format(1,p_1))
##    print("p",0,"= ",p_0, " Steps: 0")
##    print("p",1,"= ",p_1, " Steps: 1")
##    print("Value of p",i," - p: ",p_0-p_1)
    whileIter(p_0,p_1,Tol,N,i,q_0,q_1)
    #print(p)


main()
