# Title:  Dimensioning short-circuit cases
def DIMSCC(BBVR,NG,SLINE):
    print("start of DIMSCC")
   #INITIALIZATIONS
    BBSCI=[0 for i in range(4)]
    BBSCJ=[0 for i in range(4)]
    BBSCK=[0 for i in range(4)]
    BBSCL=[0 for i in range(4)]

     #Set BBSCI,BBSCJ,BBSCK,BBSCL 

   #Start of the Setting block.
   
    BBSCI[0]=True
    BBSCI[1]=BBVR[0]
    BBSCI[2]=BBVR[0]
    BBSCI[3]=BBVR[0]

    BBSCJ[0]=True
    BBSCJ[1]=BBVR[1]
    BBSCJ[2]=BBVR[1]
    BBSCJ[3]=BBVR[1]

    BBSCK[0]=True
    BBSCK[1]=BBVR[2]
    BBSCK[2]=BBVR[2]
    BBSCK[3]=BBVR[2]

    BBSCL[0]=True
    BBSCL[1]=True
    BBSCL[2]=True
    BBSCL[3]=False

    #End of the Setting block.

    # Set BBSCL(MAX)
    if(NG<=2):
        BBSCL[2]=False
        MAX=1
        BB1=False
        if(SLINE[1-1]>=0): BB1=True
        BB2=False
        if(SLINE[2-1]>=0): BB2=True
        if(BB1 and not(BB2)):MAX=2
        if(BB1 and BB2 and SLINE[0]<SLINE[1]): MAX=2
        BBSCL[MAX-1]=False
    print("end of DIMSCC")    
    return (BBSCI,BBSCJ,BBSCK,BBSCL)    


