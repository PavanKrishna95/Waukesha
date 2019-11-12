
''' Title:  Calculates the Yoke Dimensions '''

import numpy
def OKDIM(COM,X1,Y1,Y2,XG,OK):

    DCOR  = round(COM[2])
    BAND  = COM[9]
    LFPL  = COM[21]
    BSTEP = round(COM[32])
    TFLPL = COM[37]
    N     = COM[52]
    print(N)
    LC    = COM[98]

    ''' Calculate the total thickness '''
    TS=[0 for i in range(100)]
    TS[0]=Y1[1]

    for I in range(2,N+1):
        TS[I-1]=TS[I-2]+Y1[I]

    if (LC != 0):

        ''' Core with yoke bolts '''

        for I in range(1,N+1):
            XG[I-1]=0

        HYLLA=60.
        if(BAND > 0.1) :
            EXTRA=50.
        else:
            EXTRA=0.

        for I in range(1,N+1):
            OK[I-1]=X1[I]+20
        
        ''' Corrugations of the yoke against the winding
            in regards to winding support thickness '''

        I=1
        while(OK[I-1]+LFPL <= OK[N-1] and I <= N):
            XG[I-1]=LFPL
            I=I+1
 
        ''' Check for irregularities on the upper side '''

        I=2

        while (I <= N):
            while (OK[I-1]+XG[I-1] < OK[I-2]+XG[I-2]):
                OK[I-1]=OK[I-1]+round(BSTEP)

            I=I+1

        I=1
        while (I <= N and Y2[0]-Y2[I-1] < HYLLA):
            IS=I
            I=I+1

        for I in range(1,IS+1):
            XG[I-1]=OK[IS-1]+LFPL+EXTRA-OK[I-1]

        ''' Adjust openings for yoke bolts '''

        if (DCOR > 700) :
            H=80.
        else:
            H=70.

        for I in range(1,N+1):
            if (XG[I-1] > (H+LFPL)) :
                OK[I-1]=XG[I-1]+OK[I-1]-H-LFPL
                XG[I-1]=H+LFPL

        ''' In the case 1st & 2nd yoke plates of equal width '''

        OK[0]=OK[1]
        XG[0]=XG[1]

        ''' Check space for yoke banding '''

        J=1
        while(J <= N):
            if (XG[J-1] > 0.) :
                J=J+1
            else:
                I=J
                J=N+1
  
        A=(35.+LFPL)/SIN20/COS20-100.
        while(A >= TS[I-2]+TFLPL+3.):
            XG[I-1]=LFPL
            I=I+1

        ''' Check irregularities on upper side '''

        for I in range(2,N+1):
            while(OK[I-1]+XG[I-1] < OK[I-2]+XG[I-2]):
                OK[I-1]=OK[I-1]+round(BSTEP)
 
        return COM,XG,OK

        ''' Core with NO yoke bolt '''


    for I in range(1,N+1):
        XG[I-1]=0

    IANL=0
    IX=0
    IX1=0
    IY=0

    ''' Constant overlap '''

    for I in range(1,N+1):
        OK[I-1]=X1[I]+20

    I=1
    while(I <= N  and OK[I-1]+LFPL <= OK[N-1]):
        IANL=I
        XG[I-1]=LFPL
        I=I+1

    ''' Height of winding plate re-inforcement '''

    EL=0.

    if (LFPL >65.) :
        if (DCOR >1200) :
            S=93.
        elif (DCOR >=1000) :
            S=93./200.*(DCOR-1000)
        else:
            S=0.
    
    elif (LFPL > 50) :
        if (DCOR >=1050) :
            S=93.
        elif (DCOR >750) :
            S=93./300.*(DCOR-750)
        else:
            S=0.

    else:
        if (DCOR >900) :
            S=93.
        else:
            S=93./400.*(DCOR-500)
 
    if(S > 15.):
        I=1
        while(I <=N):
            EL=EL+Y1[I]

            if(EL < S):
                I=I+1
            else:
                IX=I
                I=N+1

        for I in range(1,IX+1):
            XG[I-1]=80+LFPL
 
    else:
        S=0.
    
    ''' Check space for yoke banding '''

    A=(35.+LFPL)/(numpy.sin(numpy.deg2rad(20))/numpy.cos(numpy.deg2rad(20)))-100.
    I=0

    while(A > TS[IANL-1]+TFLPL+3. and I !=1):
        if(IANL == N-1):
            ''' WRITE(6,3111) '''
            I=1
        else:
            IANL=IANL+1
            XG[IANL-1]=LFPL

    ''' Check contact area of winding support '''

    ANL=2.*LFPL
    I=0

    while(TS[IANL-1] < ANL and I !=1):
        if(IANL == N-1):
            ''' WRITE(6,3333) '''
            I=1
        else:
            IANL=IANL+1
            XG[IANL-1]=LFPL

    ''' In the case of 1st & 2nd yoke plates of equal width '''

    OK[0]=OK[1]
    XG[0]=XG[1]

    for I in range(2,N+1):
        while(OK[I-1]+XG[I-1] < OK[I-2]+XG[I-2]):
            OK[I-1]=OK[I-1]+round(BSTEP)

    COM[95]=EL

    return COM,XG,OK

    ''' 3111  FORMAT('0','Inner Yoke Banding will make contact with ',
     &   'yoke. Support is too thick for this Core Diameter.')
 3333  FORMAT('0','Winding Support Contact Area too small. ',
     &         'Support is too thick for this Core Diameter.')
       END '''
