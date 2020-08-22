import operator

def hasArrived(currentTime,arrivalTime) :
    if(arrivalTime < currentTime) :
        return True
    else :
        return False
    
#start here    
#input
n = int(input("Enter no. of processes : "))
P = [] #list of tuples
for i in range(0,n) :
    AT = int(input("Enter arrival time of P"+str(i+1)+" : "))
    BT = int(input("Enter burst time of P"+str(i+1)+" : "))
    P.append((("P"+str(i+1)),AT,BT))
    
print(P)

ZAT = []
NZAT = []
for process in P :
    if(process[1] == 0) :
        ZAT.append(process)
    else :
        NZAT.append(process)
ZAT.sort(key = operator.itemgetter(2)) #sorting zero AT processes by their BT
NZAT.sort(key = operator.itemgetter(2,1))

print(ZAT)
print(NZAT)

GC = []
startTime = 0
for ele in ZAT :
    GC.append((ele[0],startTime,startTime+ele[2]))
    startTime = startTime + ele[2] #updating start time of new process to end time of old process
    
for ele in NZAT :
    if(hasArrived(startTime,ele[1])) :
        GC.append((ele[0],startTime,startTime+ele[2]))
        startTime = startTime + ele[2]
    else :
        

zip_lists = zip(P,GC)
WT = []
TT = []
for (i,j) in zip_lists :
    WT.append((i[0],j[1]-i[1]))
    TT.append((i[0],j[1]-i[1]+i[2]))
        
print(GC)
print("waiting times :",WT)
print("turnaround times :",TT)