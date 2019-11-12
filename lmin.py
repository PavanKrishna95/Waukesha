from goto import with_goto
from funk import FUNK
def LMIN (N,NB,X,F,XREL,GREL,EPSI,FEPSI,DELTA,
          MFIRST,NFMX,NCYK,NF,ITR,HV,PARAM):

    ''' VID ANROPET #R :
        NB     = M
        EPSI   = EPS
        FEPSI  = FEPS
        DELTA  = DRV
        MFIRST = AF
        OCH I PARAM-VEKTORN #R
        PARAM( 4)= NLIM = SIGLIM
        PARAM( 5)= NDR  = PCONT
        PARAM( 6)= DEPS = DEPSI
        PARAM( 7)= AMAX = AMMAX
        PARAM( 8)= REPS = ERRM
        PARAM[9]= NORC = STPLIM
        PARAM[10]= ORF  = GAMMA
        PARAM[11]= BETA
        PARAM[12]= UTSKR= IUT3 '''

    TD     = 1.E-5
    ALFA   = 1.6
    SIGLIM = 2

    PCONT  = 6
    DEPSI  = 0.005

    AMMAX  =100.*MFIRST
    ERRM   = 0.

    NOR    = 0
    STPLIM = 6
    GAMMA  = 0.1
    BETA   = 6
    NLB    = 0
    MNRES  = 3
    ICONV  = 0

    IUT1   = 0
    IUT2   = 1
    IUT3   = 0
    IUT4   = 1
    IUT5   = 0
    IUT6   = 0
    IUT7   = 0
    IUT8   = 0
    NHV=0
    ''' SWITCHAR F@R UTSKRifTER : 1 GER UTSKRifT.
        IUT1 = DERIVATABER.
        IUT2 = UTSKRifT AV AM
        IUT3 = UTSKRifT AV F,X OCH G-V#RDEN VID VARJE FUNKTIONSANROP.
        IUT4 = ENKLA EL. DUBBLA DifFBER.
        IUT5 = UTSKRifT AV FDELTA OCH RES.
        IUT6 = UTSKRifT AV AMAX.
        IUT7 = UTSKRifT AV SLUTRES. 5 SISTA CYKLERNA
        IUT8 = TEST AV LP-L@SNING '''
    
    if(PARAM[0] !=0.):
        if(PARAM[1] != 0.): TD     = PARAM[1]
        if(PARAM[2] != 0.): ALFA   = PARAM[2]
        if(PARAM[3] != 0.): SIGLIM = PARAM[3]
        if(PARAM[4] != 0.): PCONT  = PARAM[4]
        if(PARAM[5] != 0.): DEPSI  = PARAM[5]
        if(PARAM[6] != 0.): AMMAX  = PARAM[6]
        if(PARAM[7] != 0.): ERRM   = PARAM[7]
        if(PARAM[8] != 0.): NOR    = PARAM[8]
        if(PARAM[9] != 0.): STPLIM = PARAM[9]
        if(PARAM[10] != 0.): GAMMA  = PARAM[10]
        if(PARAM[11] != 0.):BETA   = PARAM[11]
        if(PARAM[12] != 0.):IUT3   = PARAM[12]
        if(PARAM[0] !=1.):
            if(PARAM[13] != 0.):IUT4   = PARAM[13]
            if(PARAM[14] != 0.):IUT1   = PARAM[14]
            if(PARAM[15] != 0.):IUT2   = PARAM[15]
            if(PARAM[16] != 0.):IUT5   = PARAM[16]
            if(PARAM[17] != 0.):IUT6   = PARAM[17]
            if(PARAM[18] != 0.):IUT7   = PARAM[18]
            if(PARAM[19] != 0.):IUT8   = PARAM[19]
            if(PARAM[20] != 0.):NLB    = PARAM[20]
            if(PARAM[21] != 0.):MNRES  = PARAM[21]
            if(PARAM[0] !=2):
                if(PARAM[22] != 0.):NHV    = PARAM[22]

    NPP=0
    NBP=0
    NL=0
    for I in range(1,N+1):
        if(XREL[I-1] == 0): NPP=NPP+1
    for I in range(1,NB+1):
        if(GREL[I-1] == 0): NBP=NBP+1
        if(GREL[I-1] < 0.):NL=NL+1

    ME=2*N+NB
    LCOLE=ME+2*N-NL+1

    I1=1
    I2=I1+(ME-2*NPP-NBP+1)*(LCOLE-4*NPP-NBP)
    I3=I2+(NB-NBP+1)*(N-NPP)
    I4=I3+(N-NPP+1)*(N-NPP)
    I5=I4+5*N
    I6=I5+(N-NPP+1)*2
    I7=I6+N-NPP
    I8=I7+N-NPP
    I9=I8+NB
    I10=I9+N-NPP
    I11=I10+N-NPP
    I12=I11+N-NPP
    I13=I12+2*N
    I14=I13+N
    I15=I14+N-NPP
    I16=I15+NB
    I17=I16+NB
    I18=I17+N-NPP
    I19=I18+N+1
    I20=I19+5*NB
    I21=I20+8*ME+8*N+10+NL
    I22=I21+N-NPP
    I23=I22+NB
    I24=I23+NB
    I25=I24+N
    I26=I25+N
    I27=I26+NB
    I28=I27+NB-NBP
    BNHV=I28

    if(PARAM[0] == 3):
        if(NHV < BNHV):ICONV = -3

    PARAM[22]=BNHV

    J1=I20
    J2=I20+N
    J3=I20+4*N+NB+1
    J4=J3+ME+1

    
    ''' HV[I1-1] = E
        HV[I2-1] = G
        HV[I3-1] = P
        HV[I4-1] = LASTX
        HV[I5-1] = SIGNAL
        HV[I6-1] = AM
        HV[I7-1] = F
        HV[I8-1] = G0
        HV[I9-1] = LIMIT
        HV[I10-1]= XF
        HV[I11-1]= X0
        HV[I12-1]= XDELTA
        HV[I13-1]= XC
        HV[I14-1]= XX
        HV[I15-1]= G1
        HV[I16-1]= G2
        HV[I17-1]= SIGMA
        HV[I18-1]= ALFA1
        HV[I19-1]= LASTG
        HV[I20-1]= HV
        HV[I21-1]= INDEX
        HV[I22-1]= G3
        HV[I23-1]= GC
        HV[I24-1]= AMAX
        HV[I25-1]= CENT
        HV[I26-1]= EQLP
        HV[I27-1]= INDG

        SPECIALUPPDELNINGAR AV HV[I20-1]. SLASKAREOR
    
        HV[J1-1]= CD
        HV[J2-1]= AA
        HV[J3-1]= EQG '''

    NE=ME+1-2*NPP-NBP
    NG=NB+1-NBP
    NP=N+1-NPP
    

    (NLB,X,F,NF,NCYK,ICONV,BETA,IUT1,IUT2,IUT3,
     IUT4,IUT5,IUT6,IUT7,IUT8,HV[I1-1],HV[I2-1],
     HV[I3-1],HV[I4-1],HV[I5-1],HV[I6-1],HV[I7-1],
     HV[I8-1],HV[I9-1],HV[I10-1],HV[I11-1],HV[I13-1],
     HV[I14-1],HV[I15-1],HV[I16-1],HV[I17-1],HV[I18-1],
     HV[I19-1],HV[I20-1],HV[I21-1],HV[I22-1],HV[I23-1],
     HV[I24-1],HV[I25-1],HV[I26-1],HV[I27-1],HV[J1-1],
     HV[J2-1],HV[J3-1])= LM1A(N,NB,NLB,X,F,XREL,GREL,NFMX,
                             NF,NCYK,ITR,ICONV,ALFA,SIGLIM,BETA,
                             STPLIM,MFIRST,PCONT,DELTA,EPSI,FEPSI,
                             DEPSI,GAMMA,TD,NE,NP,IUT1,IUT2,IUT3,
                             IUT4,IUT5,IUT6,IUT7,IUT8,AMMAX,ERRM,NOR,PARAM,
                             MNRES,NHV,BNHV,HV[I1-1],HV[I2-1],HV[I3-1],HV[I4-1],
                             HV[I5-1],HV[I6-1],HV[I7-1],HV[I8-1],HV[I9-1],
                             HV[I10-1],HV[I11-1],HV[I12-1],HV[I13-1],HV[I14-1],
                             HV[I15-1],HV[I16-1],HV[I17-1],HV[I18-1],HV[I19-1],
                             HV[I20-1],HV[I21-1],HV[I22-1],HV[I23-1],HV[I24-1],
                             HV[I25-1],HV[I26-1],HV[I27-1],HV[J1-1],HV[J2-1],HV[J3-1])

    return (X,F,NCYK,NF,HV,PARAM,ICONV)

@with_goto
def LM1A(NVAR,K1,KL1,X,F0,XREL,GREL,NFMX,
             NF,NCYK,ITR,CONV,
            ALFA,SIGLIM,BETA,STPLIM,MFIRST,PCONT,DELTA,
            EPSI,FEPSI,DEPSI,GAMMA,TD,NE,NP,
            IUT1,IUT2,IUT3,IUT4,IUT5,IUT6,IUT7,IUT8,
            AMMAX,ERRM,NOR,PARAM,MNRES,NHV,BNHV,
            E,G,P,LASTX,SIGNAL,
            AM,F,G0,LIMIT,XF,X0,XDELTA,
            XC,XX,G1,G2,SIGMA,ALFA1,LASTG,HV,INDEX,G3,GC,
            AMAX,CENT,EQLP,INDG,CD,AA,EQG):

    VP='X('
    VP2='G('
    VP3='GREL('
    VP4='A('
    BL=' '
    IND=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,0,0]

    ''' INITALIZE THE PROGRAM ............................................ '''
    LASTX=[[0. for i in range(NVAR)] for i in range(5)]
    XC=[0. for i in range(NVAR)]
    
    if(CONV != -3):
        N=0
        for NN in range(1,NVAR+1):
            for J in range(1,6):
                LASTX[J-1][NN-1]=X[NN-1]

            XC[NN-1]=LM10 (XC[NN-1],' C',1)

            if(XREL[NN-1] == 0.):continue
            N=N+1
            INDEX[N-1]=NN
            XC[NN-1]=LM10 (XC[NN-1],BL,1)
            X0[N-1]=X[NN-1]/XREL[NN-1]

        K=0
        KL=0
        PE=0
        II=0
        JJ=0
        NZ=0

        if(K1 != 0):
            for I in range(1,K1+1):
                if(GREL[I-1] == 0.):NZ=NZ+1
                if(GREL[I-1] < 0.):PE=PE+1
                GC[I-1]=LM10 (GC[I-1],BL,1)
            III=K1-PE-NZ
            for I in range(1,K1+1):
                EQLP[I-1]=LM10 (EQLP[I-1],BL,1)
                GC[I-1]=LM10 (GC[I-1],'I',1)
                if(GREL[I-1] == 0):continue
                K=K+1
                if(I <= abs(KL1)):KL=KL+1
                GC[I-1]=LM10 (GC[I-1],BL,1)
                if(GREL[I-1] < 0.): GC[I-1]=LM10 (GC[I-1],'E',1)
                if(GREL[I-1] < 0.): JJ=JJ+1
                if(GREL[I-1] < 0.): INDG[III+JJ-1]=I
                if(GREL[I-1] > 0.): II=II+1
                if(GREL[I-1] > 0.): INDG[II-1]=I

        for NN in range(1,N+1):AMAX[NN-1]=AMMAX

        N2=N*2
        ME=2*N+K
        LCOLE=ME+2*N-PE+1
        NF=0
        NRES=0
        NCYK=0
        CONV=0
        START= True

        ''' LINEARIZATION '''

        DELTA1=DELTA

        ''' LP-SOLUTION '''
        LM8 (NE,ME,N2,PE)

        '''.......................................................................'''
        if(ITR == 0):
            goto ._15

        ''' STARTL@SNING '''
        ''' CALCULATION '''
        F0,G0,NF,X,G3,IRET1=LM9A (X0,G0,N,NF,X,INDEX,XREL,GREL,K1)
        if (IRET1  ==  1): label ._145
        if(ITR > 0):
            goto ._12

    ''' WRITE(6,500)NVAR,K1,EPSI,FEPSI,DELTA,MFIRST,NFMX,ITR '''
    if(PARAM[0] != 0.):
        ''' WRITE(6,620)
            WRITE(6,520) IND[0],ifIX(PARAM[0]) '''
        if(PARAM[1] != 0.): ''' WRITE(6,510) IND[1],TD '''
        if(PARAM[2] != 0.): ''' WRITE(6,510) IND[2],ALFA '''
        if(PARAM[3] != 0.): ''' WRITE(6,520) IND[3],SIGLIM '''
        if(PARAM[4] != 0.): ''' WRITE(6,520) IND[4],PCONT '''
        if(PARAM[5] != 0.): ''' WRITE(6,510) IND[5],DEPSI '''
        if(PARAM[6] != 0.): ''' WRITE(6,510) IND[6],AMMAX '''
        if(PARAM[7] != 0.): ''' WRITE(6,510) IND[7],ERRM '''
        if(PARAM[8] != 0.): ''' WRITE(6,520) IND[8],NOR '''
        if(PARAM[9] != 0.): ''' WRITE(6,520) IND[9],STPLIM '''
        if(PARAM[10] != 0.): ''' WRITE(6,510) IND[10],GAMMA '''
        if(PARAM[11] != 0.): ''' WRITE(6,510) IND[11],BETA '''
        if(PARAM[12] != 0.): ''' WRITE(6,520) IND[12],IUT3 '''
        if(PARAM[0] != 1): 
            if(PARAM[13] != 0.): ''' WRITE(6,520) IND[13],IUT4 '''
            if(PARAM[14] != 0.): ''' WRITE(6,520) IND[14],IUT1 '''
            if(PARAM[15] != 0.): ''' WRITE(6,520) IND[15],IUT2 '''
            if(PARAM[16] != 0.): ''' WRITE(6,520) IND[16],IUT5 '''
            if(PARAM[17] != 0.): ''' WRITE(6,520) IND[17],IUT6 '''
            if(PARAM[18] != 0.): ''' WRITE(6,520) IND[18],IUT7 '''
            if(PARAM[19] != 0.): ''' WRITE(6,520) IND[19],IUT8 '''
            if(PARAM[20] != 0.): ''' WRITE(6,520) IND[20],KL1 '''
            if(PARAM[21] != 0.): ''' WRITE(6,520) IND[21],MNRES '''
            if(PARAM[0] != 2):
                if(PARAM[22] != 0.):''' WRITE(6,520) IND[22],NHV '''

    if(CONV == -3):
        ''' WRITE(6,626) BNHV
                WRITE(6,613) CONV '''
        return (KL1,X,F0,NF,NCYK,CONV,BETA,
            IUT1,IUT2,IUT3,IUT4,IUT5,IUT6,IUT7,IUT8,
            E,G,P,LASTX,SIGNAL,
            AM,F,G0,LIMIT,XF,X0,
            XC,XX,G1,G2,SIGMA,ALFA1,LASTG,HV,INDEX,G3,GC,
            AMAX,CENT,EQLP,INDG,CD,AA,EQG)
        
    ''' WRITE(6,502)(I,X[I-1],XC[I-1],I,XREL[I-1],I=1,NVAR)
          WRITE(6,615)(VP3,J,GREL(J),J=1,K1)

          WRITE(6,608)
          WRITE(6,609) F0
          WRITE(6,603)(VP,J,X(J),XC(J),J=1,NVAR)
          WRITE(6,606)(VP2,J,G3(J),EQLP(J),GC(J),J=1,K1)
          WRITE(6,601) '''

    label ._12
    for I in range(1,NVAR+1):
        CD[I-1]=LM10 (CD[I-1],' .',1)
        AA[I-1]=0.
    
    ''' ....................................................................... '''
    label ._15
    if(IUT8 == 1):
        ''' WRITE(42,280) N2+1,N2+2,ME+1 '''
    BETA=BETA/STPLIM
    IRES=1
    RES=1

    if(KL1 < 0):
        LIN=True
        KL1=-KL1
    
    else:LIN=False

    ''' CONTROL '''
    (CONV,LASTF,LASTNF,LASTNX,LASTX,LASTG)=LM2 (CONV,EPSI,FEPSI,F0,LASTF,LASTNF,LASTNX,LASTX,
         N,START,XDELTA,INDEX,LASTG,G3,K1)

    ''' START OF MINIMIZATION ............................................ '''

    ''' **** NEWITERATION **** '''
    ''' LINEARIZATION '''
    label ._40
    (CENT,F,F0,G,G0,PP,XX,G1,G2,AMAX,NF,X,G3,IRET1)=LM3A (CENT,DELTA1,DEPSI,F,F0,G,G0,K,KL,LIN,N,PCONT,
          PP,START,X0,TD,G1,G2,AMAX,ERRM,NF,X,
          INDEX,XREL,GREL,K1)
    if (IRET1  ==  1):goto ._145

    ''' NEWLIMITS '''
    (AM,B,LIMIT,P,SCALAR,SIGNAL,
            STEPS,START,XF,SIGMA,ALFA1)=LM4 (ALFA,AM,BETA,B,GAMMA,LIMIT,N,P,NP,SCALAR,SIGNAL,
         STEPS,START,XF,X0,XDELTA,MFIRST,STPLIM,ILP,NOR,
         SIGMA,SIGLIM,ALFA1)

    ''' **** TRY AGAIN **** '''

    label ._50
    if(IRES == 1):
        for NN in range(1,N+1):AM[NN-1]=MFIRST

    if(RES >= 2 and RES <= 4):
        for NN in range(1,N+1):AM[NN-1]=ALFA*AM[NN-1]

    ''' PREPARATION '''
    AM,E,AMAX=LM7 (AM,E,F,G,G0,K,LCOLE,ME,N,P,PE,AMAX,EPSI,RES)

    ''' LP-SOLUTION '''
    RES,X,Z,HV=EPLM8 (E,M,N,P,TD,HV)

    if(RES != 1):
        ''' CALCULATION  (ONLY TO GET RIGHT OUTPUT) '''
        if(RES == 5):CONV=-2
        if(RES != 5):
            NRES=NRES+1
            ''' if(NRES >= MNRES):CONV=3 '''
            if(NRES >= MNRES):CONV=-2

            if(IRES == 1):IRES=0
    else:
        for NN in range(1,N+1):
            NN2=2*NN
            NN21=NN2-1
            X0[NN-1]=X0[NN-1]+XDELTA[NN21-1]-XDELTA[NN2-1]

        if(IRES == 1):IRES=2
        if(IRES == 0):IRES=1

        if(IUT8 != 0):
      
            ''' **** TEST AV LP-L@SN. ****
                GENOM ATT S#TTA IN ERH$LLNA X-V#RDEN I EKV-SYSYEMET
                OCH JFR. MED H@GERLEDET KAN LP-L@SN. KONTROLLERAS.
                OM VL > HL  FEL.
                OM VL < HL  OK
                OM VL = HL  OK. BEG. LIGGER IMOT.
                DUALA VARIABLER  HV(2*N+1,4*N+K)
                HV(2*N+1,4*N) BEG. P$ DE FRIA VARIABLERNA
                HV(4*N+1,4*N+K) IMPLICITA BEG. (=G-BEG.)
                OM D.V. SKILLDA FR$N NOLL LIGGER BEG. MOT. JFR. VL=HL OVAN.
                MINST N-ST. BEG. SKALL LIGGA MOT.

                EKV.SYSTEMET(E-MATRISEN) ORDNAS GENOM ANROP AV EPLM7 '''

            AM,E,AMAX=LM7 (AM,E,F,G,G0,K,LCOLE,ME,N,P,PE,AMAX,EPSI,RES)
            VL=0
            NC=0
            for II in range(2,ME+2):
                HL=E[II-1][LCOLE-1]
                for NN in range(1,N2+1):VL=VL+XDELTA[NN-1]*E[II-1][NN-1]
                if(abs(VL-HL) >= 0.001):
                    if(VL >= HL):
                        ''' VL > HL  FEL '''
                        ''' WRITE(42,290)NF,II,VL,HL '''
                    VL=0
                else:
                    NC=NC+1
                    EQG[NC-1]=II
                    VL=0
            ''' WRITE(42,300) NF
                WRITE(42,310) (EQG(II),II=1,NC) '''

            NC=0
            for II in range(N2+1,N2+ME+1):
                if(abs(HV[II-1]) < 1.E-7):continue
                NC=NC+1
                EQG[NC-1]=II-N2+1

        ''' WRITE(42,320)(EQG(II),II=1,NC) '''
        ''' **** SLUT P$ TEST **** '''

        ILP=0
        if(NRES == 0):ILP=1
        NRES=0

        ''' CALCULATION '''
        F0,G0,NF,X,G3,IRET1=LM9A (X0,G0,N,NF,X,INDEX,XREL,GREL,K1)
        if (IRET1  ==  1): goto ._145

        ''' CONTROL '''
        (CONV,LASTF,LASTNF,LASTNX,LASTX,LASTG)=LM2 (CONV,EPSI,FEPSI,F0,LASTF,LASTNF,LASTNX,LASTX,
                                                    N,START,XDELTA,INDEX,LASTG,G3,K1)

    ''' ....................................................................... '''

    NCYK=NCYK+1
    if(NF > NFMX):CONV=-1
    if(ITR == 0):goto ._110
    I=numpy.mod(NCYK,int(abs(ITR)))
    if(I != 0 and ILP == 0 and CONV != 0): goto ._97
    if(I != 0 and NCYK != 1 and CONV == 0):goto ._110

    label ._97
    
    if ITR==0:goto ._110
    elif ITR >0:goto ._160
    else :pass
    ''' WRITE(6,602)NCYK,NF '''
    if(RES == 1): ''' WRITE(6,609)F0 '''
    if(IUT5 == 1): ''' WRITE(6,260) Z,RES '''
    if(RES == 1) :
        ''' WRITE(6,603)(VP,J,X(J),XC(J),J=1,NVAR)
            BEG. SOM LIGGER IMOT MARKERAS MED EN *
            SE TEST AV LP-L@SNING OVAN '''
        for I in range(1,K+1):
            EQLP[INDG[I-1]-1]=LM10 (EQLP[INDG[I-1]-1],'*',1)
            if(abs(HV[4*N+I-1]) < 1.E-7): EQLP[INDG[I-1]-1]=LM10 (EQLP[INDG[I-1]-1],BL,1)

        ''' WRITE(6,606)(VP2,J,G3(J),EQLP(J),GC(J),J=1,K1) '''
    IVAL=1

    label ._99
    II=0
    ''' @VERLAGRING AV CENT TILL CD (F@R UTSKRifT) '''

    for I in range(1,NVAR+1):
        CD[I-1]=LM10 (CD[I-1],' .',1)
        if(XREL[I-1] == 0.):continue
        II=II+1
        CD[I-1]=LM10 (CD[I-1],' F',1)
        if(CENT[II-1]): CD[I-1]=LM10 (CD[I-1],' C',1)

    if(IUT4 == 1): ''' WRITE(6,250)(CD[I-1],I=1,NVAR) '''

    ''' @VERLAGRING AV AM TILL AA (F@R UTSKRifT) '''
    
    II=0
    for I in range(1,NVAR+1):
        AA[I-1]=0
        if(XREL[I-1] == 0.):continue
        II=II+1
        AA[I-1]=AM[II-1]

    if(IUT2 == 1): ''' WRITE(6,240)(VP4,J,AA(J),J=1,NVAR) '''
    if(IVAL == 2): goto ._110
    if(IVAL == 3): return (KL1,X,F0,NF,NCYK,CONV,BETA,
            IUT1,IUT2,IUT3,IUT4,IUT5,IUT6,IUT7,IUT8,
            E,G,P,LASTX,SIGNAL,
            AM,F,G0,LIMIT,XF,X0,
            XC,XX,G1,G2,SIGMA,ALFA1,LASTG,HV,INDEX,G3,GC,
            AMAX,CENT,EQLP,INDG,CD,AA,EQG)

    ''' UTSKRifT AV DERIVATABER#KNINGEN '''

    if(IUT1 != 0):
        ''' WRITE(6,210)(F[I-1],I=1,N) '''
        for I in range(1,K+1): ''' WRITE(6,220) I,(G(I,J),J=1,N) '''


    if(IUT6 == 1):''' WRITE(6,270) (AMAX(II),II=1,N) '''
    ''' WRITE(6,620) '''

    if(CONV == 0):goto ._115
    ''' WRITE(6,601) '''
    if(CONV == (-1)):''' WRITE(6,610) '''
    if(CONV == (-2)):''' WRITE(6,611)'''
    if(CONV > 0): ''' WRITE(6,612) '''

    label ._104
    '''WRITE(6,602)NCYK,NF
    WRITE(6,609)F0
    WRITE(6,613) CONV
        WRITE(6,603)(VP,J,X(J),XC(J),J=1,NVAR)
        WRITE(6,606)(VP2,J,G3(J),EQLP(J),GC(J),J=1,K1) '''

    if(IVAL == 3 or CONV == -3):return (KL1,X,F0,NF,NCYK,CONV,BETA,
            IUT1,IUT2,IUT3,IUT4,IUT5,IUT6,IUT7,IUT8,
            E,G,P,LASTX,SIGNAL,
            AM,F,G0,LIMIT,XF,X0,
            XC,XX,G1,G2,SIGMA,ALFA1,LASTG,HV,INDEX,G3,GC,
            AMAX,CENT,EQLP,INDG,CD,AA,EQG)
    if(IUT7 != 1):goto ._110
    ''' WRITE(6,604) (NCYK+1-I-NRES,I=1,5),(LASTF(J),J=1,5) '''
    for NN in range(1,NVAR+1): ''' WRITE(6,605)NN,(LASTX(JJ,NN),JJ=1,5) '''

    ''' WRITE(6,620) '''
    for NN in range(1,K1+1):''' WRITE(6,622)NN,(LASTG(JJ,NN),JJ=1,5) '''

    goto ._110

    label ._160
    IVAL=2
    goto ._99

    ''' ....................................................................... '''

    label ._110
    if(CONV != 0):return (KL1,X,F0,NF,NCYK,CONV,BETA,
            IUT1,IUT2,IUT3,IUT4,IUT5,IUT6,IUT7,IUT8,
            E,G,P,LASTX,SIGNAL,
            AM,F,G0,LIMIT,XF,X0,
            XC,XX,G1,G2,SIGMA,ALFA1,LASTG,HV,INDEX,G3,GC,
            AMAX,CENT,EQLP,INDG,CD,AA,EQG)

    label ._115
    if(RES == 1):goto ._40
    goto ._50

    if(ITR ==0):return (KL1,X,F0,NF,NCYK,CONV,BETA,
            IUT1,IUT2,IUT3,IUT4,IUT5,IUT6,IUT7,IUT8,
            E,G,P,LASTX,SIGNAL,
            AM,F,G0,LIMIT,XF,X0,
            XC,XX,G1,G2,SIGMA,ALFA1,LASTG,HV,INDEX,G3,GC,
            AMAX,CENT,EQLP,INDG,CD,AA,EQG)
    elif ITR >0: goto ._180
    else:pass
    ''' WRITE(6,624) '''

    label ._180
    IVAL=3
    if(ITR <0):
        goto ._104
    elif ITR >0:goto ._99
    else: return (KL1,X,F0,NF,NCYK,CONV,BETA,
            IUT1,IUT2,IUT3,IUT4,IUT5,IUT6,IUT7,IUT8,
            E,G,P,LASTX,SIGNAL,
            AM,F,G0,LIMIT,XF,X0,
            XC,XX,G1,G2,SIGMA,ALFA1,LASTG,HV,INDEX,G3,GC,
            AMAX,CENT,EQLP,INDG,CD,AA,EQG)

    return (KL1,X,F0,NF,NCYK,CONV,BETA,
            IUT1,IUT2,IUT3,IUT4,IUT5,IUT6,IUT7,IUT8,
            E,G,P,LASTX,SIGNAL,
            AM,F,G0,LIMIT,XF,X0,
            XC,XX,G1,G2,SIGMA,ALFA1,LASTG,HV,INDEX,G3,GC,
            AMAX,CENT,EQLP,INDG,CD,AA,EQG)

    '''
  210 FORMAT('0DERIVATES'/' FGRAD',6X,1P,7E14.5,(/1H ,12X,1P,7E14.5))
  220 FORMAT(' GGRAD.ROW',I2,1P,7E14.5,(/1H ,11X,1P,7E14.5))
  240 FORMAT((1X,3(A2,I2,')=',1PE13.5,6X)))
  250 FORMAT(1X,'FORW.OR CENTR.DifF.',5X,20A2)
  260 FORMAT(1H ,19X,'(LP: FDELTA=',1PE13.5,' RES=',I2,' )')
  270 FORMAT(' AMAX',7X,1P,7E14.5,(/1H ,8X,1P,7E14.5))
  280 FORMAT(1H0,'TEST OF LP-SOLUTION'/1X,19(1H*)//,
     &' X.ROW =  2 -',I3/' G.ROW =',I3,' -',I3///)
  290 FORMAT(' FAULT. NF=',I4,' E-ROW=',I3,' VL=',1PE15.8,' HL=',E15.8)
  300 FORMAT(1H0,'NF',14X,'=',I4)
  310 FORMAT(' EQ E-ROW(VL=HL) =',30I3)
  320 FORMAT(' EQ DUALA VAR.   =',30I3)
  500 FORMAT(1H0///1X,'INPUT DATA TO MINIMIZATION ROUTINE LMIN'/1X,
     &39(1H*)//1X,
     &'N      =',I10/1X,
     &'M      =',I10/1X,
     &'EPS    =',1PE10.3/1X,
     &'FEPS   =',E10.3/1X,
     &'DRV    =',1PE10.3/1X,
     &'AF     =',E10.3/1X,
     &'NFMX   =',I10/1X,
     &'ITR    =',I10)
  502 FORMAT(1X/(1X,'X(',I2,') =',1PE10.3,A2,
     & 4X,'XREL(',I2,') =',E10.3))
  510 FORMAT(1X,'PARAM(',I2,')=',1PE10.3)
  520 FORMAT(1X,'PARAM(',I2,')=',I10)
  601 FORMAT(1H0)
  602 FORMAT(1H0,'CYCLE NUMBER',I3,',',I5,' CALCULATIONS')

  603 FORMAT(1X,'VARIABLES'/(1X,3(A2,I2,')=',1PE13.5,A2,4X)))

  604 FORMAT(/1X,'RESULTS FROM THE LAST 5 CYCLES',/1X,30(1H*)//1X,
     & 'CYCLE NR.',6X,I4,4(11X,I4)//1X,'F   =',5(3X,1PE12.5)//)

  605 FORMAT(2X,1HX,I2,1H=,5(3X,1PE12.5))

  606 FORMAT(1X,'CONSTRAINTS'/(1X,3(A2,I2,')=',1PE13.5,1X,2A1,3X)))

  608 FORMAT('0INITIAL SOLUTION')

  609 FORMAT(1X,'F =',1PE13.5)

  610 FORMAT(1H0,'*** MINIMIZATION DELETED ***'//1X,
     & 'GIVEN NFMX REACHED')

  611 FORMAT(1H0,'*** MINIMIZATION DELETED ***'//1X,
     & 'LP-ALGORITHM UNSUCCESSFUL')

  612 FORMAT(1H0,'OPTIMUM INDICATED'/1X,17(1H*))
  613 FORMAT(1H0,'CONVERGENCE (ICONV) =',I2/1X)
  615 FORMAT(1X/(1X,3(A5,I2,')=',1PE12.5,3X)))
  620 FORMAT(1X)
  622 FORMAT(2X,1HG,I2,1H=,5(3X,1PE12.5))
  624 FORMAT(1H0,'MINIMIZATION DELETED FROM'/
     &          1X,'SUBROUTINE FUNK'/1X,25(1H*)//)
  626 FORMAT(1H0,'*** MINIMIZATION DELETED ***'//1X,
     & 'HV-VECTOR TOO SMALL , MUST BE AT LEAST:',I10) '''

      
''' LM3A LINEARIZATION '''

def LM3A (CENT,DELTA1,DEPSI,F,F0,G,G0,K,KL,LIN,N,PCONT,
          PP,START,X0,TD,G1,G2,AMAX,ERRM,NF,X,
          INDEX,XREL,GREL,K1):

    for NN in range(1,N+1):
        XX[NN-1]=X0[NN-1]

    if(START):
        ''' CALCULATION '''
        F0,G0,NF,X,G3,IRET1=LM9A (XX,G0,N,NF,X,INDEX,XREL,GREL,K1)
        if (IRET1  ==  1):return
        if(KL > 0):
            DELTA2=DELTA1*10.
            for NN in range(1,N+1):
                XX[NN-1]=X0[NN-1]+DELTA2
                ''' CALCULATION '''
                F2,G2,NF,X,G3,IRET1=LM9A (XX,G2,N,NF,X,INDEX,XREL,GREL,K1)
                if (IRET1  ==  1):return
                XX[NN-1]=X0[NN-1]
                if(LIN):
                    F[NN-1]=(F2-F0)/DELTA2

                for KK in range(1,KL+1):
                    G[KK-1][NN-1]=(G2[KK-1]-G0[KK-1])/DELTA2
   

        PP=0
        for NN in range(1,N+1):
            CENT[NN-1]=True
        CONT=True

    else:
        PP=PP+1
        if(PP < PCONT):
            CONT=False
        else:    
            PP=0
            CONT=True

    temp75=True
    for NN in range(1,N+1):
        if(CONT):temp75=True
        if(not CENT[NN-1]):temp75=False

        ''' CENTRAL DifFERENCES '''
        if temp75:
            XX[NN-1]=XX[NN-1]-DELTA1/2.0
            ''' CALCULATION '''
            F1,G1,NF,X,G3,IRET1=LM9A (XX,G1,N,NF,X,INDEX,XREL,GREL,K1)
            if (IRET1  ==  1):return

            XX[NN-1]=XX[NN-1]+DELTA1
            ''' CALCULATION '''
            F2,G2,NF,X,G3,IRET1=LM9A (XX,G2,N,NF,X,INDEX,XREL,GREL,K1)
            if (IRET1  ==  1):return
            X[NN-1]=X0[NN-1]
            if(not LIN):F[NN-1]=(F2-F1)/DELTA1

            if(ERRM != 0.):
                YERROR= max1(abs(F0-0.5*(F1+F2)),1.E-20)
                AMAX[NN-1]=DELTA1*numpy.sqrt(ERRM*(max(abs(F0),abs(AMAX[NN-1]*F[NN-1]))+TD)
                                     /YERROR)
                AMXF=AMAX[NN-1]
                AMXG=1.E30
   
            KJ=KL+1
            if(KJ > K):continue
            for KK in range(KJ,K+1):
                G[KK-1][NN-1]=(G2[KK-1]-G1[KK-1])/DELTA1

                if(ERRM == 0.): continue
                YERROR= max(abs(G0[KK-1]-0.5*(G1[KK-1]+G2[KK-1])),1.E-20)
                AMM=DELTA1*numpy.sqrt(ERRM*(max(abs(G0[KK-1]),abs(AMAX[NN-1]*G[KK-1][NN-1]))+TD)
                              /YERROR)
                AMXG=min(AMXG,AMM)
        
            if(ERRM != 0.): AMAX[NN-1]=min(AMXF,AMXG)
            continue

        ''' SIMPLE DifFERENCES '''
        XX[NN-1]=XX[NN-1]+DELTA1
        ''' CALCULATION '''
        F2,G2,NF,X,G3,IRET1=LM9A (XX,G2,N,NF,X,INDEX,XREL,GREL,K1)
        if (IRET1  ==  1):return
        XX[NN-1]=X0[NN-1]
        if(not LIN):F[NN-1]=(F2-F0)/DELTA1
        KJ=KL+1
        if(KJ > K):continue
    
        for  KK in range(KJ,K+1):
            G[KK-1][NN-1]=(G2[KK-1]-G0[KK-1])/DELTA1

    if( not CONT):return

    for NN in range(1,N+1):
        CENT[NN-1]=True
        XX[NN-1]=X0[NN-1]+DELTA1
        ''' CALCULATION '''
        F1,G1,NF,X,G3,IRET1=LM9A (XX,G1,N,NF,X,INDEX,XREL,GREL,K1)
        if (IRET1  ==  1):return
        XX[NN-1]=X0[NN-1]
        if(not LIN):
            if((abs(F[NN-1]-(F1-F0)/DELTA1)) > (abs(F[NN-1])*DEPSI+TD)):continue

        if(KJ <= K):
            for KK in range(KJ,K+1):
                if((abs(G[KK-1][NN-1]-(G1[KK-1]-G0[KK-1])/DELTA1)) >
                   (DEPSI*max(abs(G0[KK-1]/AMAX[NN-1]),abs(G[KK-1][NN-1]))+TD)):break

        else:
            CENT[NN-1]=False

    return (CENT,F,F0,G,G0,PP,XX,G1,G2,AMAX,NF,X,G3,IRET1)

''' LM9A CALCULATION '''

def LM9A (X0,G,N,NF,X,INDEX,XREL,GREL,K1):

    IRET1=0
    
    for NN in range(1,N+1):
        IND=INDEX[NN-1]
        X[IND-1]=X0[NN-1]*XREL[IND-1]

    NF=NF+1

    a,X,G3,F=FUNK(X)
    if a==1:
        IRET=1
        return (F,G,NF,X,G3,IRET1)
    II=0

    for I in range(1,K1+1):
        if(GREL[I-1] <= 0.):continue
        II=II+1
        G[II-1]=G3[I-1]/GREL[I-1]
        
    for I in range(1,K1+1):
        if(GREL[I-1] >= 0.):continue
        II=II+1
        G[II-1]=G3[I-1]/abs(GREL[I-1])
        
    ''' UTSKRifT VID VARJE FUNKTIONSANROP '''
    
    return (F,G,NF,X,G3,IRET1)
      
''' LM2 CONTROL '''

def LM2 (CONV,EPSI,FEPSI,F0,LASTF,LASTNF,LASTNX,LASTX,
         N,START,XDELTA,INDEX,LASTG,G3,K1):

    NNX=3
    NNF=3
    N2=1
    if(START):
        CONV=0
        LASTNF=0
        LASTNX=0
        for I in range(1,6):
            LASTF[I-1]=1E20
            for J in range(1,N+1):
                IND=INDEX[J-1]
                LASTX[I-1][IND-1]=0

        return (CONV,LASTF,LASTNF,LASTNX,LASTX,LASTG)

    temp60=False
    for I in range(1,N+1):
        I2=2*I
        I21=I2-1
        if(abs(XDELTA[I21-1]-XDELTA[I2-1]) <= EPSI):continue
        else:
            LASTNX=0
            temp60=True        
            break

    else:
        LASTNX=LASTNX+1
        if(LASTNX < NNX):
            temp60=True
        else:CONV=1

    if temp60:
        if(abs(F0-LASTF[N2-1]) <= FEPSI):
            LASTNF=LASTNF+1
            if(LASTNF >= NNF):CONV=2
        else:LASTNF=0

    for I in range(1,5):
        J=6-I
        JJ=J-1
        LASTF[J-1]=LASTF[JJ-1]
        for NN in range(1,N+1):
            IND=INDEX[NN-1]
            LASTX[J-1][IND-1]=LASTX[JJ-1][IND-1]


    LASTF[0]=F0

    for NN in range(1,N+1):
        IND=INDEX[NN-1]
        LASTX[0][IND-1]=X[IND-1]

    for I in range(1,5):
        for NN in range(1,K1+1):
            LASTG[5-I][NN-1]=LASTG[4-I][NN-1]
    for NN in range(1,K1+1):
        LASTG[0][NN-1]=G3[NN-1]

    return (CONV,LASTF,LASTNF,LASTNX,LASTX,LASTG)

''' LM4 NEWLIMITS '''

def LM4 (ALFA,AM,BETA,B,GAMMA,LIMIT,N,P,NP,SCALAR,SIGNAL,
         STEPS,START,XF,X0,XDELTA,MFIRST,STPLIM,ILP,NOR,
         SIGMA,SIGLIM,ALFA1):

    if(START):
        START=False

        for NN in range(1,N+1):
            NN1=NN+1
            LIMIT[NN-1]=True
            SIGNAL[NN-1][0]=1
            SIGNAL[NN-1][1]=1

            for I in range(1,N+1):
                P[NN1-1][I-1]=0.0

            NN2=NN-1
            if(NN == 1):P[1][0]=1
            if(NN != 1):P[NN1-1][NN-1]=(-1)**(NN2)
            AM[NN-1]=MFIRST
            XF[NN-1]=X0[NN-1]

        B=1.0
        STEPS=1
        STEP2=0
        return (AM,B,LIMIT,P,SCALAR,SIGNAL,
                STEPS,START,XF,SIGMA,ALFA1)

    if(STEPS >= STPLIM):
        if(STEP2 < NOR):
            STEP2=STEP2+1
            STEPS=1
            SCALAR=0.0

            for NN in range(1,N+1):
                SCALAR=SCALAR+ (X0[NN-1]-XF[NN-1])**2

            if(SCALAR >= (GAMMA**2)):
                for NN in range(1,N+1):
                    P[0][NN-1]=X0[NN-1]-XF[NN-1]
                    XF[NN-1]=X0[NN-1]
                    LIMIT[NN-1]=True
                    SIGNAL[NN-1][0]=1
                    SIGNAL[NN-1][0]=1

                AM[0]=numpy.sqrt(SCALAR)*BETA/B
                B=1.0

                ''' ORTONORMALATION '''
                P,SIGMA,ALFA1=LM5 (N,P,NP)
                return (AM,B,LIMIT,P,SCALAR,SIGNAL,
                        STEPS,START,XF,SIGMA,ALFA1)
            B=B+1.0
        else:STEPS=STEPS+1
    else:STEPS=STEPS+1

    for I in range(1,N+1):
        SCALAR=0.0
        I1=I+1
        for NN in range(1,N+1):
            NN2=NN*2
            NN21=NN2-1
            SCALAR=SCALAR+P[I1-1][NN-1]*(XDELTA[NN21-1]-XDELTA[NN2-1])

        if(STEPS > 2 and B > 1.1 or ILP != 0):
            if(SCALAR <= 0.0 and not LIMIT[I-1]):
                if(not LIMIT[I-1] and SCALAR < 0.0):

                    ''' AGAIN '''
                    AM,SIGNAL=LM6 (ALFA,AM,SCALAR,SIGNAL,SIGLIM,2,I)
                    SIGNAL[I-1][0]=1
    
                else:
                    AM[I-1]=AM[I-1]/ALFA
                    SIGNAL[I-1][0]=1
                    SIGNAL[I-1][1]=1
            else:
                ''' AGAIN '''
                AM,SIGNAL=LM6 (ALFA,AM,SCALAR,SIGNAL,SIGLIM,1,I)
                SIGNAL[I-1][1]=1
                
        LIMIT[I-1]=True
        if(SCALAR <= 0.0):LIMIT[I-1]=False

    return (AM,B,LIMIT,P,SCALAR,SIGNAL,
            STEPS,START,XF,SIGMA,ALFA1)
      
''' ORTONORMALISATION '''

def LM5 (N,P,NP):

    ''' THIS PROCEDURE IS BASED ON THE ARTICLE BY POWEL IN
        COMPUTER JOURNAL VOL.19 P.J02 '''

    NN=N+1

    for I in range(1,NN+1):

        ALFA[I-1]=0
        for J in range(1,N+1):
            ALFA[I-1]=ALFA[I-1]+P[0][J-1]*P[I-1][J-1]

    ALFA[0]=numpy.sqrt(ALFA[0])

    NM=N+2
    for JT in range(1,N+1):
        T=NM-JT
        if(abs(ALFA[T-1]) > (ALFA[0]*1E-7)):break

    ''' START '''
    S=0.0

    for I in range(1,N+1):
        SIGMA[I-1]=0.0

    ''' HERE '''
    
    while (T > 2):
        
        S=S+ALFA[T-1]**2

        for J in range(1,N+1):
            SIGMA[J-1]=SIGMA[J-1]+ALFA[T-1]*P[T-1][J-1]

        TT=T-1
        for J in range(1,N+1):
            P[T-1][J-1]=(S*P[TT-1][J-1]-ALFA[TT-1]*SIGMA[J-1])/numpy.sqrt(S*(S+ALFA[TT-1]**2))

        T=TT
      
    ''' READY '''
    for J in range(1,N+1):
        P[1][J-1]=P[0][J-1]/ALFA[0]

    return P,SIGMA,ALFA
    
    '''LM6 AGAIN '''

def LM6 (ALFA,AM,SCALAR,SIGNAL,SIGLIM,K,NN):

    if(SIGNAL[NN-1][K-1] < SIGLIM):
        SIGNAL[NN-1][K-1]=SIGNAL[NN-1][K-1]+1
        return AM,SIGNAL
    if(abs(SCALAR) < (0.99*AM[NN-1])):
        SIGNAL[NN-1][K-1]=SIGNAL[NN-1][K-1]+1
        return AM,SIGNAL

    SIGNAL[NN-1][K-1]=1
    AM[NN-1]=AM[NN-1]*ALFA
    return AM,SIGNAL
          
    '''LM7 PREPARATION '''

def LM7 (AM,E,F,G,G0,K,LCOLE,ME,N,P,PE,AMAX,EPSI,RES):

    JJ=2*N+1
    for J in range(JJ,LCOLE+1):
        E[0][J-1]=0.0

    ME1=ME+1
    LC1=LCOLE-1

    for I in range(2,ME1+1):
        for J in range(JJ,LC1+1):
            E[I-1][J-1]=0.0

    ME2=ME1-PE

    for I in range(2,ME2+1):
        IN=2*N-1+I
        E[I-1][IN-1]=1.0
   
    for J in range(1,N+1):
        J2=2*J
        J21=J2-1
        E[0][J21-1]=F[J-1]
        E[0][J2-1]=-F[J-1]

    for I in range(1,N+1):
        I1=I+1
        I2=2*I
        I21=I2+1
        for J in range(1,N+1):
            J2=2*J
            J21=J2-1
            E[I2-1][J21-1]=P[I1-1][J-1]
            E[I21-1][J2-1]=P[I1-1][J-1]
            E[I2-1][J2-1]=-P[I1-1][J-1]
            E[I21-1][J21-1]=-P[I1-1][J-1]

    if(RES == 1):
        for NN in range(1,N+1):
            AMAX[NN-1]=max(AMAX[NN-1],AM[NN-1]*0.5,EPSI*4.0)
            SLMX=1.E8
            I1=NN+1
            for J in range(1,N+1):
                SLMX=min(SLMX,AMAX[NN-1]/(abs(P[I1-1][J-1]+1.E-10)))
                AM[NN-1]=min(AM[NN-1],SLMX)

    for I in range(1,N+1):
        I2=2*I
        I21=I2+1
        E[I2-1][LCOLE-1]=AM[I-1]
        E[I21-1][LCOLE-1]=AM[I-1]

    for I in range(1,K+1):
        N21=2*N+1+I
        for J in range(1,N+1):
            J2=2*J
            J21=J2-1
            E[N21-1][J21-1]=G[I-1][J-1]
            E[N21-1][J2-1]=-G[I-1][J-1]
        E[N21-1][LCOLE-1]=-G0[I-1]

    return AM,E,AMAX

''' LP-SOLUTION '''

def LM8 (NE,M,N,P):

    LCOL=M+N-P+1
    I1=1
    I2=I1+N+M
    I3=I2+LCOL
    I4=I3+LCOL
    I5=I4+LCOL
    I6=I5+NE
    I7=I6+NE
    I8=I7+NE
    I9=I8+NE

    return 

def EPLM8 (E,M,N,P,TD,HV):

    X=['' for i in range(N)]
    (E,RES,HV[I1-1],HV[I2-1],HV[I3-1],HV[I4-1],
         HV[I5-1],HV[I6-1],HV[I7-1],HV[I8-1])=LLP1(M,N,P,E,TD,HV[I1-1],HV[I2-1],HV[I3-1],HV[I4-1],
                                                   HV[I5-1],HV[I6-1],HV[I7-1],HV[I8-1])


    Z=-E[0][LCOL-1]
    for I in range(1,N+1):
        X[I-1]=HV[I-1]

    return RES,X,Z,HV

''' UNCAS TRANSFORM, CHARACTER INTO NONE CHARACTER VECTOR. '''

def LM10 (R,C,N):
    R=['' for i in range(N)]
    for I in range(1,N+1):
        R[I-1]=C[I-1]

    return R
