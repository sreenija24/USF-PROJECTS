
def RobotStack(b,n,k,nbarray):
    
    if n==0:
        return 0
    if b==0:
        nbarray[n][b]=1
    elif b<=k:
        if n==1:
            nbarray[n][b]=1
        else:
            nbarray[n][b]=RobotStack(b-1,n,k,nbarray)+RobotStack(b,n-1,k,nbarray)
    else:
        if n==1:
            return 0
        else:
            rowcolumnsum=0
            for i in range(b,b-k-1,-1):
                rowcolumnsum=rowcolumnsum+RobotStack(i,n-1,k,nbarray)

            nbarray[n][b]=rowcolumnsum
    
    return nbarray[n][b]

#input file reading        
bnklists = open('input.txt') # Open file on read mode
eachbnk = bnklists.read().splitlines() # List with stripped line-breaks
for each in eachbnk:
    b=int(each.split(' ')[0])
    n=int(each.split(' ')[1])
    k=int(each.split(' ')[2])
    nbarray=[[0 for i in range(0,b+1)]for j in range(0,n+1)]
    print("(",b,",",n,",",k,")","=",RobotStack(b,n,k,nbarray))



                
    

