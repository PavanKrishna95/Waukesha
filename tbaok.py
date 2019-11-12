
''' Title:  Calculates the yoke section
               for the TBA Core '''

from avtral import AVTRAL
def TBAOK(N,BSTEP,B1,OLAPP,DCOR,TT,TP,
          TWSUPC,TH,TB,OHRED):
    import common as CM
    ''' Preliminary width of yoke plates '''
    RK1=[0. for i in range(N)]
    B3=[0. for i in range(N)]

    for I in range(1,N+1):
        B3[I-1]=B1[I]+OLAPP

    M=N

    if(TWSUPC <= 5.):

        if(OHRED > 0.):
            DCORA=660.
        else:
            DCORA=580.

        if(DCOR >=DCORA):
            IX1=1
            RK1=AVTRAL(M,IX1,RK1,TP,150.,50.-TT)
            IX1=1
            RK1=AVTRAL(M,IX1,RK1,TP,80.,120.-TT)
            IX1=1
            RK1=AVTRAL(M,IX1,RK1,TP,40.,186.-TT)
        else:
            IX1=1
            RK1=AVTRAL(M,IX1,RK1,TP,40.,92.-TT)
        
    else:
        AVTR=TH+50.+TWSUPC
        BMIN=TB+10.-TT
        IX1=1
        RK1=AVTRAL(M,IX1,RK1,TP,AVTR,BMIN)

        AVTR=TWSUPC
        TS=0.

        if(CM.FINDR == 0.):
            FIND=2.
        else:
            FIND=CM.FINDR
    
        for I in range(1,IX1+1):
            TS=TS+TP[I]

        BMIN=TS+(FIND*TWSUPC)+30.
        IX1=IX1+1
        RK1=AVTRAL(M,IX1,RK1,TP,AVTR,BMIN)
       
    N1=N-1
    for I in range(1,N1+1):
        I1=N+1-I
        TSTEG=0.
        while(RK1[I1-1]+B3[I1-1] < RK1[I1-2]+B3[I1-2]):
            TSTEG=TSTEG+BSTEP
            if(TSTEG > 2.*BSTEP):break
            B3[I1-2]-=BSTEP

    if(CM.EOKF !=0.) :
        AREA1=0.
        AREA2=0.
        for I in range(1,N+1):
            AREA1=AREA1+B1[I]*TP[I]
            AREA2=AREA2+B3[I-1]*TP[I]
            
        AOKERF=CM.EOKF*AREA1

        if(AREA2 < AOKERF):
            OH=B3[N-1]
            I=1
            while(I <=N):
                I1=N+1-I
                if(B3[I1-1]+RK1[I1-1] <OH):break
                B3[I1-1]=B3[I1-1]+BSTEP
                AREA2=AREA2+TP[I1]*BSTEP
                N1=N
                I=I+1
        

            if(AREA2 < AOKERF):
                I=1
                while(I <=N1):
                    I1=N1+1-I
                    B3[I1-1]=B3[I1-1]+BSTEP
                    AREA2=AREA2+BSTEP*TP[I1]
                    if(AREA2 >= AOKERF):break
                    I=I+1

    N1=N-1
    I=1
    while(I <= N1):
        while(RK1[I]+B3[I] < RK1[I-1]+B3[I-1]):
            B3[I]=B3[I]+BSTEP
            
        I=I+1

    if(OHRED >= 2.):
        OKM=B3[N-1]-OHRED
        I=1
        while(I <= N):
            if(RK1[I-1]+B3[I-1] <= OKM):
                I=I+1
            else:
                IX=I
                I=N+1

        for I in range(IX,N+1):
            B3[I-1]=OKM-RK1[I-1]

        AREA1=0.
        AREA2=0.
        for I in range(1,N+1):
            AREA1=AREA1+B1[I]*TP[I]
            AREA2=AREA2+B3[I-1]*TP[I]

        I=1
        while(I <=N1):
            I1=IX+1-I
            if(AREA2 >= AREA1):
                I=N1+1
            else:
                if(RK1[I1-1]+B3[I1-1] >= OKM):
                    I=I+1
                else:
                    B3[I1-1]+=BSTEP
                    AREA2+=BSTEP*TP[I1]

    B3[0]=B3[1]
    if(DCOR >= 700.):
        for I in range(1,4):
            B3[I-1]=RK1[3]+B3[3]-RK1[I-1]
 
    return B3,RK1
