
''' Title:  Calculates the Yoke-Section for the TCA Core '''

def TCAOK(TYP,N,OLAPP,BSTEP,DCOR,TWSUPC,AF,B1,TP,FINDR):
    import common as CM
    ''' Preliminary layout '''
    RK1=[0. for i in range(N)]
    B3=[0. for i in range(N)]
    TS=[0. for i in range(100)]
    for I in range(1,N+1):
        B3[I-1]=B1[I]+OLAPP
 
    BBPRT1=False
    BBPRT2=False
    TS[0]=TP[1]

    for I in rnage(2,N+1):
        TS[I-1]=TS[I-2]+TP[I]

    for I in range(I,N+1):
        RK1[I-1]=0.

    if (DCOR <= 780.):
        RLNU=35.
    
    elif(780<DCOR <= 900.):
        RLNU=45.
        
    elif(900<DCOR <= 1200.):
        RLNU=55.

    else:RLNU=65.
 
    I=1

    while(I <= N):
        I1=I
        RK1[I-1]=TWSUPC+58.+8.
        if (TS[I-1] <RLNU):I=I+1
        else:I=N+1
 
    ANL=FINDR*TWSUPC
    I=I1+1

    while(I <= N-1):
        I2=I
        RK1[I-1]=TWSUPC+8.
        if (TS[I-1]-TS[I1-1] >= ANL):I=N
        else:I=I+1

    A=(29.+TWSUPC+8.)/numpy.tan(numpy.deg2rad(20))-100.
    J=0

    while(A >= TS[I2-1]+18. and J != 1):
        if (I2 == N-1):
            BBPRT2=True
            J=1
        else:
            I2=I2+1
            RK1[I2-1]=TWSUPC+8.

    N1=N-1
    I=1

    while(I <= N1):
        if (RK1[I]+B3[I] >= RK1[I-1]+B3[I-1]):I=I+1
        else:B3[I]+=BSTEP
        
    if (TYP <= 3. and DCOR >=680.):
        OKM=B3[N-1]-(int(0.08*DCOR/BSTEP)*BSTEP)
        I=1
        while(I <= N):
            if(RK1[I-1]+B3[I-1]<=OKM):I=I+1
            else:
                IX=I
                I=N+1
 
        for I in range(IX,N+1):
            B3[I-1]= int((OKM-RK1[I-1])/BSTEP)*BSTEP
 
    if (DCOR > 800.):
        if (DCOR > 900.):NL=5
        else:NL=4
    else:NL=3

    if (TYP > 3.):
        if (DCOR > 800.):
            if (DCOR > 1200.):NL=7
            else:
                NL= int((DCOR-0.001)*0.01)-5
        else:NL=2

    for I in range(1,NL):
          B3[I-1]= int((B3[NL-1]+RK1[NL-1]-RK1[I-1])/BSTEP)*BSTEP
 
    ''' B) '''

    Y1=35.
    M=1
    while(M <= 2):
        AVST=35./numpy.cos(numpy.deg2rad(20))
        I=2
        while (I <= N and TS[I-1] <= 50.):
            RL=RK1[0]+B3[0]+Y1/numpy.cos(numpy.deg2rad(20))
            Y=numpy.tan(numpy.deg2rad(20))*TS[I-2]+RL
            if (RK1[I-1]+B3[I-1] <= Y-AVST):
                N1=I
                I=I+1
            else:
                Y1=Y1+1
    
        AVST=20./numpy.cos(numpy.deg2rad(20))
        I=1
        while(I <= N):
            if (RK1[I-1]+B3[I-1] < B3[N-1]):I=I+1
            else:
                N2=I
                I=N+1
 
        I=N1

        while(I <= N2):
            RL=RK1[0]+B3[0]+Y1/numpy.cos(numpy.deg2rad(20))
            Y=numpy.tan(numpy.deg2rad(20))*TS[I-1]+RL
            if (RK1[I-1]+B3[I-1]<=Y-AVST):I=I+1
            else:Y1=Y1+1
 
        CM.HB=B3[N-1]+15.-RL
        CM.CB=CM.HB/numpy.tan(numpy.deg2rad(20))

        if (M != 1):M=M+1
        else:

            ''' C) '''
        
            I=2
            while(I <= N2):
                if (TS[I-2] <= CM.CB+20.):I=I+1
                else:
                    B3[I-1]= int((B3[N-1]+RK1[N-1]-RK1[I-1])/BSTEP)*BSTEP
                    I=I+1

            ''' D) '''

            J=1
            while(J <= N2):
                I=N2-J+1
                if (I >NL+1):
                    while (B3[I-1]+RK1[I-1]-B3[I-2]-RK1[I-2] >16.):B3[I-2]+=BSTEP
                    J=J+1
                else:J=N2+1                
 
            M=M+1

    if (AF !=0.):
        for I in range(1,N+1):
            B3[I-1]=B3[I-1]+AF

    return B3,RK1,BBPRT1,BBPRT2
