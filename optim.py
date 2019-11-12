
''' Title:  Layout for the TA1 Core
            All references to 20. changed to BSTEP
            BSTEP = Width of Step Increase (Input Value) '''
from goto import with_goto
@with_goto
def OPTIM(DCORN,F1,TCORST,RNK,PLIMB,HLIMB,FHD,ETA,
          BSTEP,BPLMAX):
    import common as CM
    ''' Each Packet shall have a multiple of RMLTPK sheets
        Each packet shall have at least RMINPK sheets '''

    RMLTPK=12.
    RMINPK=36.
    DENCST=7.65E-4
    RDNNP=[[0. for i in range(2)] for j in range(21)]
    
    DIST=[0. for i in range(3)]
    PRC=[0. for i in range(4)]
    F=[0. for i in range(100)]
    H=[[0. for i in range(100)]  for j in range(100)]
    BPLPKT=[0. for i in range(100)]
    TPHT=[0. for i in range(100)]
    ICLO=[0 for i in range(3)]
    IXINDX=[0 for i in range(100)]
    IWINDX=[[0 for i in range(100)]  for j in range(100)]
    
    RDNNP[0][0]=333.
    RDNNP[0][1]= 5.
    RDNNP[1][0]=384.
    RDNNP[1][1]= 6.
    RDNNP[2][0]=428.
    RDNNP[2][1]= 7.
    RDNNP[3][0]=474.
    RDNNP[3][1]= 8.
    RDNNP[4][0]=508.
    RDNNP[4][1]= 9.
    RDNNP[5][0]=541.
    RDNNP[5][1]=10.
    RDNNP[6][0]=572.
    RDNNP[6][1]=11.
    RDNNP[7][0]=600.
    RDNNP[7][1]=12.
    RDNNP[8][0]=621.
    RDNNP[8][1]=13.
    RDNNP[9][0]=646.
    RDNNP[9][1]=14.
    RDNNP[10][0]=672.
    RDNNP[10][1]=15.
    RDNNP[11][0]=698.
    RDNNP[11][1]=16.
    RDNNP[12][0]=723.
    RDNNP[12][1]=17.
    RDNNP[13][0]=749.
    RDNNP[13][1]=18.
    RDNNP[14][0]=775.
    RDNNP[14][1]=19.
    RDNNP[15][0]=800.
    RDNNP[15][1]=20.
    RDNNP[16][0]=825.
    RDNNP[16][1]=21.
    RDNNP[17][0]=850.
    RDNNP[17][1]=22.
    RDNNP[18][0]=875.
    RDNNP[18][1]=23.
    RDNNP[19][0]=940.
    RDNNP[19][1]=24.
    RDNNP[20][0]=2000.
    RDNNP[20][1]=25.

    PRC[0]=0.31
    PRC[1]=0.24
    PRC[2]=0.20
    PRC[3]=0.17

    ''' BBLARM is used to transmit a warning to the designer via the panel '''

    BBLARM=False
    ALARM='                                                  '

    ''' HNOTCH and BNOTCH define the dimensions of the
        step in the surface of the yoke against the winding '''

    HNOTCH=40.
    BNOTCH=65.

    for I in range(1,22):
        if(DCORN <= RDNNP[I-1][0]):
            CM.NPKTS=int(RDNNP[I-1][1])
            break

    RDN=2.*numpy.sqrt((DCORN/2.)**2-(0.1*DCORN)**2)
    B1MAX=int(RDN/BSTEP)*BSTEP
    if (B1MAX > BPLMAX):B1MAX=BPLMAX
    S1=numpy.sqrt(DCORN**2-F1**2)
    B1MIN=int(S1/BSTEP)*BSTEP
    N1=0

    for RI in range(B1MIN,B1MAX+1,BSTEP):
        N1=N1+1
        BPLPKT[N1-1]=RI

    if (N1 < CM.NPKTS):
        BBLARM= True
        ALARM='Check the Maximum Width of Core Plate Available.'
        return

    M=N1

    label ._140
    F[0]=F1/2.
    for I in range(2,M+1):
        F[I-1]=numpy.sqrt(DCORN**2-BPLPKT[I-1]**2)/2.

    for I in range(2,M-CM.NPKTS+3):
        H[CM.NPKTS-1][I-1]=0.
        for J in range(1,I):
            H1=BPLPKT[J-1]*(F[J-1]-F[I-1])
            if (H1 >H[CM.NPKTS-1][I-1]):
                H[CM.NPKTS-1][I-1]=H1
                IWINDX[CM.NPKTS-1][I-1]=J

    for KPKT in range((CM.NPKTS-1),1,-1):
        for I in range((2+CM.NPKTS-KPKT),(M-KPKT+2)+1):
            H[KPKT-1][I-1]=0.
            for J in range((CM.NPKTS-KPKT+1),I):
                H1=BPLPKT[J-1]*(F[J-1]-F[I-1])+H[KPKT][J-1]
                if (H1 > H[KPKT-1][I-1]):
                    H[KPKT-1][I-1]=H1
                    IWINDX[KPKT-1][I-1]=J
    
    A=0.
    for  J in range (CM.NPKTS,M+1):
        A1=2*(BPLPKT[J-1]*F[J-1]+H[1][J-1])
        if (A1 > A):
            A=A1
            IXINDX[0]=J

    for KPKT in (2,CM.NPKTS+1):
        IXINDX[KPKT-1]=IWINDX[KPKT-1][IXINDX[KPKT-2]-1]
  
    KPKT=1
    TPKT[KPKT-1]=F[IXINDX[KPKT-1]-1]+0.009
    RNS1[KPKT-1]=TPKT[KPKT-1]/TCORST
    for KPKT in (2,CM.NPKTS+1):
        TPKT[KPKT-1]=F[IXINDX[KPKT-1]-1]-F[IXINDX[KPKT-2]-1]
        RNS1[KPKT-1]=TPKT[KPKT-1]/TCORST

    ''' Locate the Cooling Ducts '''

    LOC=0
    DIST[0]=0.
    DIST[1]=0.
    DIST[2]=0.
    if (RNK > 1.):
        DIST[0]=F1*PRC(round(RNK)-1)
        if (RNK > 3.):DIST[1]=2.*DIST[0]
    AUX=0.
    I=1

    for KPKT in (CM.NPKTS,0,-1):
        AUX=AUX+TPKT[KPKT-1]
        if (DIST[I-1] <= AUX and DIST[I-1] !=0.):
            if (((AUX-DIST[I-1])/TPKT[KPKT-1]) > 0.2):
                TPKT[KPKT-1]=TPKT[KPKT-1]-4.
                LOC=LOC+1
                ICLO[LOC-1]=KPKT
            else:
                TPKT[KPKT]=TPKT[KPKT]-4.
                LOC=LOC+1
                ICLO[LOC-1]=KPKT+1

            I=I+1

    if (RNK == 1 or RNK == 3 or RNK ==5):
        TPKT[0]=TPKT[0]-2.
        LOC=LOC+1
        ICLO[LOC-1]=1

    ''' Make the packets a multiple of RMLTPK '''

    ARE1=0.
    ARE2=0.
    CM.REST=0.
    for KPKT in range(1,CM.NPKTS+1):
        ARE1=ARE1+2.*(TPKT[KPKT-1]*BPLPKT[IXINDX[KPKT-1]-1])*ETA
        RNS1[KPKT-1]=int((TPKT[KPKT-1]+CM.REST)/(TCORST*RMLTPK))*RMLTPK
        CM.REST=(TPKT[KPKT-1]+CM.REST)-(RNS1[KPKT-1]*TCORST)
        TPKT[KPKT-1]=RNS1[KPKT-1]*TCORST
        ARE2=ARE2+2.*(TPKT[KPKT-1]*BPLPKT[IXINDX[KPKT-1]-1])*ETA
  

    ''' Make the minimum packet with RMINPK sheets '''

    CM.REST=CM.REST*2.
    ARE3=0.
    for KPKT in range(CM.NPKTS,0,-1):
        if (RNS1[KPKT-1] < RMINPK):
            RNS1[KPKT-2]=RNS1[KPKT-2]-(RMINPK-RNS1[KPKT-1])
            RNS1[KPKT-1]=RMINPK
    
        TPKT[KPKT-1]=RNS1[KPKT-1]*TCORST
        ARE3=ARE3+2.*(TPKT[KPKT-1]*BPLPKT[IXINDX[KPKT-1]-1])*ETA
  

    ''' Adjust the width to fill all available space '''

    AUXST=0.
    AUXS=0.
    CM.ARE=0.
    TACC=0.
    for KPKT in range(1,CM.NPKTS+1):
        TACC=TACC+TPKT[KPKT-1]
        for NL in range(1,4):
            if (ICLO[NL-1] == KPKT):
                if (KPKT == 1):
                    TACC=TACC+2.
                else:
                    TACC=TACC+4.
    
        AUXST=numpy.sqrt((DCORN*0.5)**2-TACC**2)
        AUXS=round(BSTEP*int((2.*AUXST-BPLPKT[IXINDX[KPKT-1]-1])/BSTEP))
        BPLPKT[IXINDX[KPKT-1]-1]=BPLPKT[IXINDX[KPKT-1]-1]+AUXS

        for MPKT in range(1,KPKT):
            if (abs(BPLPKT[IXINDX[KPKT-1]-1]-BPLPKT[IXINDX[MPKT-1]-1])<(0.1)):
                TPKT[MPKT-1]=TPKT[MPKT-1]+TPKT[KPKT-1]
                CM.NPKTS=CM.NPKTS-1

        CM.ARE=CM.ARE+2.*(TPKT[KPKT-1]*BPLPKT[IXINDX[KPKT-1]-1])*ETA

    '''' Calculate the step for the yoke '''

    TACC=0.
    for KPKT in range(CM.NPKTS,0,-1):
        TACC=TACC+TPKT[KPKT-1]
        for NL in range(1,4):
            if (ICLO[NL-1] == (KPKT+1)):TACC=TACC+4.

        if (TACC >=BNOTCH):
            if ((BPLPKT[IXINDX[KPKT-2]-1]-BPLPKT[IXINDX[KPKT-1]-1]) < HNOTCH):
                for N1 in range(1,M+1):
                    if (BPLPKT[N1-1]==BPLPKT[IXINDX[KPKT-1]-1]):
                        for I in range(N1,M):
                            BPLPKT[I-1]=BPLPKT[I]
  
                        M=M-1
                        goto ._140
            else:
                goto ._150

    label ._150
    LSH=KPKT

    for I in range(1,CM.NPKTS+1):
        SW[I-1]=BPLPKT[IXINDX[I-1]-1]
        STP=0.
        if (I >=LSH):STP=HNOTCH
        TPHT[I-1]=SW[I-1]+STP

    V1=0.
    V2=0.
    for I in range(1,CM.NPKTS+1):

        if (I >= LSH):V1=V1+(SW[I-1]*TPKT[I-1]*HNOTCH)*ETA
        V2=V2+(TPKT[I-1]*SW[I-1]**2)*ETA

    RMLIMB=3.*(DENCST/100.)*(HLIMB*CM.ARE+4.*V1-(F1-CM.REST)*FHD**2*3.1416/4.)
    RMCORN=3.*(DENCST/100.)*4.*V2
    RMYOKE=4.*(DENCST/100.)*PLIMB*CM.ARE-(2./3.)*RMCORN
    RMCORE=RMLIMB+RMCORN+RMYOKE

    CM.TK=F1-CM.REST
    CM.RLK1=TACC

    CM.BSMAX=SW[0]
    CM.BSMIN=SW[CM.NPKTS-1]

    '''for I in range(1,CM.NPKTS+1):
        print('nsheet, width, thickness ', RNS1[I-1], SW[I-1], TPKT[I-1])'''

    return BBLARM,ALARM
