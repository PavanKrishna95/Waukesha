def BRUM(IBB,IHLIMB):
    C1=[0]*8
    C2=[0]*8
    C3=[0]*8

    D1=[0]*8
    D2=[0]*8
    D3=[0]*8

    K=[0]*8
    IBB=0
    IHLIMB=0

    C1[0]=0.11563E-8
    C1[1]=0.84859E-9
    C1[2]=0.67364E-9
    C1[3]=0.58590E-9
    C1[4]=0.48458E-9
    C1[5]=0.42789E-9
    C1[6]=0.35437E-9
    C1[7]=0.29899E-9

    C2[0]=0.50872E-6
    C2[1]=0.55917E-6
    C2[2]=0.57081E-6
    C2[3]=0.55485E-6
    C2[4]=0.55586E-6
    C2[5]=0.56066E-6
    C2[6]=0.55634E-6
    C2[7]=0.57354E-6

    C3[1-1]=0.80216E-3
    C3[2-1]=0.10401E-2
    C3[3-1]=0.12866E-2
    C3[4-1]=0.15068E-2
    C3[5-1]=0.18173E-2
    C3[6-1]=0.20540E-2
    C3[7-1]=0.24819E-2
    C3[8-1]=0.28856E-2

    D1[1-1]=0.10604E-8
    D1[2-1]=0.77528E-9
    D1[3-1]=0.61468E-9
    D1[4-1]=0.53676E-9
    D1[5-1]=0.43857E-9
    D1[6-1]=0.38856E-9
    D1[7-1]=0.32236E-9
    D1[8-1]=0.27364E-9

    D2[1-1]=0.43755E-6
    D2[2-1]=0.49761E-6
    D2[3-1]=0.51253E-6
    D2[4-1]=0.49183E-6
    D2[5-1]=0.51700E-6
    D2[6-1]=0.51893E-6
    D2[7-1]=0.51114E-6
    D2[8-1]=0.52168E-6

    D3[1-1]=0.68678E-3
    D3[2-1]=0.89365E-3
    D3[3-1]=0.11109E-2
    D3[4-1]=0.13120E-2
    D3[5-1]=0.15678E-2
    D3[6-1]=0.17778E-2
    D3[7-1]=0.21579E-2
    D3[8-1]=0.25133E-2

    K[1-1]=260
    K[2-1]=350
    K[3-1]=440
    K[4-1]=510
    K[5-1]=620
    K[6-1]=700
    K[7-1]=850
    K[8-1]=1100

    RF=1.0
    M=1
    if(IBB>K[6]): M=7
    
    for I in range(1,8):
        if(IBB>=K[I-1] and IBB <= K[I]): M=I

    SUCK=IBB-K[M-1]
    DUCK=K[M]-K[M-1]
    CF=SUCK/DUCK
    BLAND1=C1[M-1]*IHLIMB**2+C2[M-1]*IHLIMB+C3[M-1]
    PLAND1=D1[M-1]*IHLIMB**2+D2[M-1]*IHLIMB+D3[M-1]
    BLAND2=C1[M]*IHLIMB**2+C2[M]*IHLIMB+C3[M]
    PLAND2=D1[M]*IHLIMB**2+D2[M]*IHLIMB+D3[M]
    BLAND=BLAND1+(BLAND2-BLAND1)*CF
    PLAND=PLAND1+(PLAND2-PLAND1)*CF
    FRNAT1=RF/BLAND
    FRNAT2=RF/PLAND    

    return (FRNAT1,FRNAT2)
