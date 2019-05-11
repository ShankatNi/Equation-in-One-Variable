import math

def FuncP(intValue):
    funcValue=intValue**6+7*(intValue**5)-15*(intValue**4)-70*(intValue**3)+75*(intValue**2)+175*intValue-125
    funcDeri=6*(intValue**5)+35*(intValue**4)-60*(intValue**3)-210*(intValue**2)+150*intValue+175
    func2Deri=30*(intValue**4)+140*(intValue**3)-120*(intValue**2)-420**intValue+150
    newValue=intValue-((funcValue*funcDeri)/((funcDeri)**2-(funcValue*func2Deri)))
    return newValue

def FuncCap(n,myList):
    x=list()
    delta=(myList[0][n+1]-myList[0][n])**2
    delta2=myList[0][n+2]-2*myList[0][n+1]+myList[0][n]
    x=myList[0][n]-(delta/delta2)
    return x

def main():
    p_0=float(input("Enter initial p0: "))
    N=1000    #int(input("Enter no of iteration: "))
    i=0
    myList=list()
    newList=list()
    newList2=list()
    

    for cl in range(0,9):
        x=FuncP(p_0)
        newList.append(x)
        p_0=x
    myList.append(newList)
    n=0

    p_02=0
    for cl in range(0,6):
        newList2.append(FuncCap(cl,myList))
        
    myList.append(newList2)


    print("-------------------------------------")
    print("           Aitken Method         ")
    print("-------------------------------------")
    print('{0:2s}{1:20s}{2:2s}{3:20s}'.format("|","               p","|","             Cap p"))
    for cl in range(len(myList[1])):
        print('{0:2s}{1:20f}{2:2s}{3:20f}'.format("|",myList[0][cl],"|",myList[1][cl]))
    


main()
