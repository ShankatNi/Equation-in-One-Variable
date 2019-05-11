import math

def newFunc(intValue):
    newValue=((intValue*math.exp(intValue))/(math.exp(intValue)-1))-1.5
    return newValue

def whileIter(a,b,Tol,N,FA,i,myList):
    list1=list()
    while(i <= N):
        list1.append(i)
        list1.append(a)
        list1.append(b)
        p=a+((b-a)/2)
        FP=newFunc(p)
        list1.append(p)
        list1.append(FP)
        myList.append(list1)
        if FP==0 or (b-a)<Tol:
            print("After ",i,"iterations, p",i,"=",b-a)
            print("Sucessful procedure: p",i,"= ",p)
            return myList
        i=i+1
        if FA*FP>0:
            a=p
            FA=FP
        else:
            b=p
        list1=list()
    print("Failed",N)
    return False

def main():
    myList=[["n","a","b","p","f(p)"]]
    a=float(input("Enter End point 1st: "))
    b=float(input("Enter End point 2nd: "))
    Tol=float(input("Enter the Tolerance: "))
    N=int(input("Enter no of iteration: "))
    
    i=1
    FA=newFunc(a)
    whileIter(a,b,Tol,N,FA,i,myList)
    print('{0:1s}{1:6s}{2:12s}{3:12s}{4:12s}{5:10s}'.format(" ","n","a_n","b_n","p_n","f(p_n)"))

    for cl in myList:
        if cl[0]=="n":
            print("----------------------------------------------------")
        else:
            print('{0:2d}{1:20f}{2:20f}{3:20f}{4:15f}'.format(cl[0],cl[1],cl[2],cl[3],cl[4]))
        

main()
