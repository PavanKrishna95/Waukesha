
''' Title:  Calculates the Core Section
            for core types EY,DY and TY '''
from okdim import OKDIM
from dnet import DNET
from tcaok import TCAOK
from wdgsup import WDGSUP
import numpy
from ncdltb import NCDLTB
from ftjbr import FTJBR
from goto import with_goto
@with_goto
def CORE2(COM,SLZ,X1Z,B2Z,OKZ,XGZ,RK2Z,T1Z,YZ):

    import common as CM
    CDUCT=[0 for i in range(21)]
    IOK=[0 for i in range(100)]
    IXG=[0 for i in range(100)]
    Y2=[0. for i in range(100)]
    Z1=[0. for i in range(100)]
    IX1=[0 for i in range(101)]
    IZX=[0 for i in range(101)]
    Y1=[0. for i in range(101)]
    YG=[0. for i in range(101)]
    ZY=[0. for i in range(101)]
    ZU=[0. for i in range(20)]
    TASEC1=TASEC2=RNY=IHO=OKL=TANSL=OKF=TASEC=0.
    DENCST=7.65E-4
    INDATA  = COM[0]
    TYP     = COM[1]
    DCOR    = COM[2]
    PLIMB   = COM[3]
    PLIMBY  = COM[4]
    HLIMB   = COM[5]
    KSERIE  = COM[6]
    LCD     = COM[7]
    AF      = COM[8]
    DCORN   = COM[10]
    X1MIN   = COM[11]
    X1MAX   = COM[12]
    FINDR   = COM[15]
    TWSUPC  = COM[21]
    DYL     = COM[22]
    IADON   = COM[23]
    BLEAK   = COM[24]
    BSTEP   = round(COM[32])
    IPMIN   = COM[33]
    NFLPL   = COM[35]
    IBFLPL  = COM[36]
    ITFLPL  = COM[37]
    TCD     = COM[40]
    TCORST  = COM[41]
    ETA     = COM[42]
    ILACK   = COM[14]+0.1
    if (COM[13] <0.01): COM[13] = COM[42]
    ETAL    = COM[13]
    N       = COM[52]
    ACCTR   = COM[94]
    KOD     = COM[96]

    TNCORS=TCORST*ETA

    ''' Constants '''

    OLAPP=20.
    POE=2.
    P=4.2
    tempx=True
    if(INDATA != 3):
        DCORN=DNET(KSERIE,KOD,HLIMB,ACCTR,DCOR,TASEC1,TASEC2)
        BT=NFLPL/2*IBFLPL+NFLPL/2*5-5
        H=0.5*DCORN-0.5*numpy.sqrt(DCORN*DCORN-BT*BT)
        HS=H+float(ITFLPL)+3.
        if (KOD ==1 ):HS=HS+2.

        if (KSERIE !=4):

            ''' Calculate the net- and the gross-diameter '''

            DB=DCOR-int(1.3333E-3*DCOR+3.5)

            ''' Minimum and maximum width of limb-plates '''

            RKORDA=numpy.sqrt(4.*((0.5*DCORN)**2-(0.5*DCORN-HS)**2))
            X1MIN=10.*int((0.5*RKORDA-0.5*TCD)*0.1+1.)
            X1MIN=max(X1MIN,100.)
            X1MIX=10.*int((0.5*BT+10.)*0.1+1.)
            if (NFLPL == 4):X1MIN=max(X1MIN,X1MIX)
            X1MAX1=0.5*(DCOR-30.-TCD)+0.1
            if (DCOR >= 700.): X1MAX1=0.5*(DCOR-35.-TCD)+0.1
            X1MAX=10.*int(X1MAX1*0.1)

            ''' Calculating number of cooling ducts '''

            LCD=NCDLTB(TYP,DCOR)

        NCD=LCD

        ''' Maximum number of packets '''

        N=int(int((X1MAX-X1MIN))/round(BSTEP)+1)

        ''' Laying out the limb-section '''

        RCORN=0.5*DCORN
        Z1[N-1]=X1MAX+0.5*TCD
        Y1[N]=numpy.sqrt(RCORN*RCORN-Z1[N-1]*Z1[N-1])
        TJBR=FTJBR(TNCORS,ETA,ETAL,ILACK,TYP,DCOR,X1MAX)
        Y1[N]=int(Y1[N]/TJBR)*TJBR
        Y2[N-1]=Y1[N]
        Z1[N-1]=Z1[N-1]-0.5*TCD
        IX1[N]=int(Z1[N-1]+0.1)
        J1=N-1
        for J in range (1,J1+1):
            I=N-J
            Z1[I-1]=Z1[I]-BSTEP+0.5*TCD
            Y2[I-1]=numpy.sqrt(RCORN*RCORN-Z1[I-1]*Z1[I-1])
            if (Y2[0] > RCORN-HS and I ==1):Y2[I-1]=RCORN-HS
            TJBR=FTJBR(TNCORS,ETA,ETAL,ILACK,TYP,DCOR,Z1[I-1]-0.5*TCD)
            Y2[I-1]=int(Y2[I-1]/TJBR)*TJBR
            Y1[I]=Y2[I-1]-Y2[I]
            Z1[I-1]=Z1[I-1]-0.5*TCD
            IX1[I]=int(Z1[I-1]+0.1)

        ''' Minimum thickness of packets '''

        IX1[0]=0
        IZX[0]=0
        Y1[0]=0.
        ZY[0]=0.
        ITEST=0
        YTA1=0.
        YTA2=0.

        ''' From J=1 to J=N '''
        label ._350
        for I in range(1,N+1):
            IZX[I]=IX1[I]
            ZY[I]=Y1[I]
        N1=N
        J=1

        temp=True
        while temp:
            temp=False
            TJBR=FTJBR(TNCORS,ETA,ETAL,ILACK,TYP,DCOR,float(IZX[J]))
            PMIN=float(IPMIN)*TJBR-0.1
            if (ZY[J] < PMIN):
                ZY[J]=ZY[J]+ZY[J+1]
                N1=N1-1
                K=J+1
                I=K
                while True:
                    ZY[I]=ZY[I+1]
                    IZX[I]=IZX[I+1]
                    I=I+1
                    if (I > N1):break
                temp=True
                continue
            if (J !=N1):
                J=J+1
                temp=True
                continue

        if (ITEST !=1):
            for I in range(1,N1+1):
                YTA1=YTA1+float(IZX[I])*ZY[I]
        else:
            for I in (1,N1+1):
                IX1[I]=IZX[I]
                Y1[I]=ZY[I]
            N=N1
            goto ._500
            
        ''' From J=N up to J=1 '''
        label ._450
        for I in range(1,N+1):
            IZX[I]=IX1[I]
            ZY[I]=Y1[I]
        N2=N
        J=N2

        temp1=True
        while temp1:
            temp1=False
            TJBR=FTJBR(TNCORS,ETA,ETAL,ILACK,TYP,DCOR,float(IZX[J]))
            PMIN=float(IPMIN)*TJBR-0.1
            if (ZY[J]<PMIN):
                if (J != 1): ZY[J-1]=ZY[J]+ZY[J-1]
                N2=N2-1
                K=J
                for I in range(K,N2+1):
                    ZY[I]=ZY[I+1]
                    IZX[I]=IZX[I+1]
                temp1=True
                continue
            if (J == 1):break
            J=J-1
            temp1=True

        if (ITEST != 1):
            for I in range(1,N2+1):
                YTA2=YTA2+float(IZX[I])*ZY[I-1]
        else:
            for I in range(1,N2+1):
                IX1[I]=IZX[I]
                Y1[I]=ZY[I]
            N=N2
            goto ._500
        ITEST=1
        for I in range(1,N+1):
            IZX[I]=IX1[I]
            ZY[I]=Y1[I]
        if (abs(YTA1-YTA2) > YTA1*0.001):
            if (YTA1-YTA2 >=0):
                goto ._350
            else:goto ._450
        else:
            if(N1-N2 <=0):goto ._350
            else:goto ._450

        label ._500
        X1MAX=IX1[N]
        X1MIN=IX1[1]
        Y2[N-1]=Y1[N]
        J1=N-1
        for J in range(1,J1+1):
            I=N-J
            Y2[I-1]=Y2[I]+Y1[I]
        NB=N

        ''' Placing the cooling ducts '''

        SL2=0.
        SL1=100.
        DY=TCORST
        SLI=0.
        JV=0
        
        for I in range(1,11):
            CDUCT[I]=0
            ZU[I-1]=0.

        if (LCD != 0):
            for I in range(1,N+1):
                SLI=SLI+float(IX1[I])*Y1[I]
            I=1
            RKYLY=2.*Y2[0]+X1MAX-float(LCD)*P

            while(I <=(LCD+1)/2):
                if (LCD-2*(LCD/2) != 0):
                    M=int(float(N)*((2.*float(I)/float(LCD+1))**0.25)+0.5)
                    JV=1
                else:
                    M=int(float(N)*((2.*float(I)/float(LCD))**(1./3.))+0.5)

                SLI=SLI-P*float(IX1[M])
                RKYLY=RKYLY+2.*float(IX1[M])
                I=I+1

            if (JV != 0):
                SLI=SLI+0.5*P*float(IX1[N])
                RKYLY=RKYLY-float(IX1[N])

            RNY=SLI*ETA*DENCST*100.*POE/RKYLY
            if (JV == 1):
                LCD=(LCD-1)/2
                CDUCT[0]=N+1
                NUM=0
                IHO=0
                Y2[N]=0.5*P
                Y1[N]=Y1[N]-Y2[N]
            else:
                LCD=LCD/2

        label ._760
        RKYLY=float(IX1[N])
        if (JV == 1):RKYLY=2.*RKYLY
        I=N
        SLI=0.
        SLASK=ETA*DENCST*100.*POE
        NUM=1

        label ._770
        X=(RNY*RKYLY-SLASK*SLI)/(SLASK*float(IX1[I])-2.*RNY)

        label ._780
        if (X > Y1[I] or NUM > LCD) :
            RKYLY=RKYLY+2.*Y1[I]
            SLI=SLI+float(IX1[I])*Y1[I]
            if (I == CDUCT[NUM-1]) :
                RKYLY=RKYLY-2.*(ZU[NUM-2]+P)
                SLI=SLI-float(IX1[I])*(ZU[NUM-2]+P)
    
            I=I-1
            if (I == 0): goto ._850
            goto ._770

        if (I == CDUCT[NUM-1]): 
            if (Y1[I]-X-ZU[NUM-2]-P  < 0.):
                X=Y1[I]+10.
                goto ._780

            X=X+ZU[NUM-1]+P
        if (Y1[I] < 3.*P):goto ._820
        if (X >P):
            if (X > Y1[I]-2.*P): goto ._815
            ZU[NUM-1]=DY*int(X/DY)
            goto ._830
        ZU[NUM-1]=P
        goto ._830

        label ._815
        ZU[NUM-1]=Y1[I]-2.*P
        goto ._830

        label ._820
        if (Y1[I] >= 2.*P): goto ._821
        goto ._830

        label ._821
        if (X <= 1.2): goto ._822
        if (X > Y1[I]-6.): goto ._823
        ZU[NUM-1]=DY*int(X/DY)

        label ._822
        ZU[NUM-1]=1.2
        goto ._840

        label ._823
        ZU[NUM-1]=Y1[I]-6.0
        goto ._840
       
        label ._830
        if (Y1[I] < 2.*P) :
            I=I-1
            ZU[NUM-1]=DY

        label ._840
        CDUCT[NUM]=I
        RKYLY=2.*float(IX1[I])
        SLI=0.
        NUM=NUM+1
        goto ._770

        label ._850
        WDM=SLASK*SLI/RKYLY
        SLD=RNY-WDM
        if (abs(SLD) > 0.050*RNY) :
            if (RNY >= WDM and SL1 >=RNY):SL1=RNY
            if (RNY < WDM and SL2 < RNY):SL2=RNY

            if (SL1 >= 100. or SL2 <=0.) :RNY=RNY-SLD/(float(LCD)+1.)
            else:RNY=(SL1+SL2)*0.5

            if (abs(SL1-SL2) < 0.11) :WDM=(SL1+SL2)*0.5
            else:
                NUM=0
                IHO=IHO+1
                if (IHO > 10):return
                goto ._760

        ''' Calculating the yoke '''

        ''' TCA-Yoke '''

        if (KSERIE == 4):
            KTEST=0
            for I in range(1,N+1):
                X1Z[I]=IX1[I]

            temp2=True
            while temp2:
                temp2=False
                OKZ,XGZ,CM.BBPRT1,CM.BBPRT2=TCAOK(TYP,N,OLAPP,BSTEP,DCOR,TWSUPC,AF,X1Z,Y1,
                    FINDR)

                for I in range(1,N+1):
                    IOK[I-1]=OKZ[I-1]
                    IXG[I-1]=XGZ[I-1]

                BBSLIM= True

                if (BLEAK >=1.E-6):
                    T=IXG[0]
                    J=1
                    for I in range(1,N+1):
                        if (IXG[I-1] <= T-1.E-5):
                            IND[J-1]=I
                            J=J+1
    
                        T=IXG[I-1]
                        TSUM=0.
                    for I in range(1,IND[0]):
                        TSUM=TSUM+Y1[I]

                    HEELS=TSUM
                    H1=IOK[IND[0]-1]
                    H2=IOK[IND[1]-1]
                    DUMMY=TWSUPC
                    KTEST,TWSUPC,TANSL,CM.WMARG,CM.TMARG=WDGSUP(FINDR,IADON,DYL,DCOR,
                        HEELS,H1,H2,BLEAK,TWSUPC,BBSLIM)

                    if (DUMMY != TWSUPC):
                        temp2=True
                        continue
                    if (KTEST == 1):
                        FINDR=FINDR+0.1
                        temp2=True
                        continue
            
        else:
            COM[52]=N
            COM,IXG,IOK=OKDIM(COM,IX1,Y1,Y2,IXG,IOK)
            EL  = COM[95]


        IOH=IOK[N-1]

        ''' Calculating the number of plates per packet SL,
            Width of plates in outer-limb B2,
            The distance K2,The thickness of packets T1 and T2 and sum Y '''

        RKVCM=0.
        RKVCM1=0.
        RKVCM2=0.
        TX=0.
        TY=0.
        SLA=0.
        SLE=0.
        SLU=0.
        IHO=0
        for I in range(1,N+1):
            YZ[I-1]=0.
 

        ''' Packet No. 1 '''

        TJBR=FTJBR(TNCORS,ETA,ETAL,ILACK,TYP,DCOR,float(IX1[1]))
        SLZ[0]=int(Y1[1]/TJBR+0.499)
        X1Z[1]=IX1[1]
        B2Z[0]=IX1[1]+AF
        OKZ[0]=IOK[0]
        XGZ[0]=IXG[0]
        RK2Z[0]=(IX1[N]-B2Z[0])/2
        T1Z[1]=SLZ[0]*TJBR
        CM.T2Z[0]=int(T1Z[1]*9.85+0.5)
        CM.T2Z[0]=CM.T2Z[0]*0.1
        YZ[0]=T1Z[1]
        I=2
        J=2
        ISLUT=0
        NUM=LCD
        YG[0]=0.

        label ._1210
        if (LCD == 0):goto ._1300
        
        if (I == CDUCT[NUM]):
            IHO=IHO+2
            if (IHO == 2):
                YG[IHO-1]=Y1[I]-P -ZU[NUM-1]
                YG[IHO]=ZU[NUM-1]
            else:
                YG[IHO-3]=Y1[I]-P  -ZU[NUM-1]
                YG[IHO-1]=ZU[NUM-1]-P  -YG[IHO-2]

            NUM=NUM-1
            goto ._1210

        if (IHO <=0):goto ._1300

        label ._1260    
        TJBR=FTJBR(TNCORS,ETA,ETAL,ILACK,TYP,DCOR,float(IX1[I]))
        SLZ[J-1]=int(YG[IHO-1]/TJBR+0.499)
        X1Z[J]=IX1[I]
        B2Z[J-1]=IX1[I]+AF
        OKZ[J-1]=IOK[I-1]
        XGZ[J-1]=IXG[I-1]
        RK2Z[J-1]=(IX1[N]-IX1[I])/2
        T1Z[J]=SLZ[J-1]*TJBR
        CM.T2Z[J-1]=int(T1Z[J]*9.85+0.5)
        CM.T2Z[J-1]=CM.T2Z[J-1]*0.1
        YZ[J-1]=YZ[J-2]+T1Z[J]
        IHO=IHO-2

        label ._1275
        J=J+1
        SLZ[J-1]=1
        X1Z[J]=IX1[I]
        B2Z[J-1]=IX1[I]+AF
        OKZ[J-1]=IOK[I-1]
        XGZ[J-1]=IXG[I-1]
        RK2Z[J-1]=(IX1[N]-IX1[I])/2
        T1Z[J]=P
        if (ISLUT == 1):T1Z[J]=0.5*P
        CM.T2Z[J-1]=int(T1Z[J]*9.85+0.5)
        CM.T2Z[J-1]=CM.T2Z[J-1]*0.1
        YZ[J-1]=YZ[J-2]+T1Z[J]
        if (ISLUT == 1):
            return
        J=J+1
        if (IHO != 0):
            goto ._1260

        TJBR=FTJBR(TNCORS,ETA,ETAL,ILACK,TYP,DCOR,float(IX1[I]))
        SLZ[J-1]=int(YG[1]/TJBR+0.499)
        X1Z[J]=IX1[I]
        B2Z[J-1]=IX1[I]+AF
        OKZ[J-1]=IOK[I-1]
        XGZ[J-1]=IXG[I-1]
        RK2Z[J-1]=(IX1[N]-IX1[I])/2
        T1Z[J]=SLZ[J-1]*TJBR
        CM.T2Z[J-1]=int(T1Z[J]*9.85+0.5)
        CM.T2Z[J-1]=CM.T2Z[J-1]*0.1
        YZ[J-1]=YZ[J-2]+T1Z[J]
        IHO=0
        if (I >=N):
            goto ._1350
        I=I+1
        J=J+1
        goto ._1210
        
        label ._1300
        TJBR=FTJBR(TNCORS,ETA,ETAL,ILACK,TYP,DCOR,float(IX1[I]))
        SLZ[J-1]=int(Y1[I]/TJBR+0.499)
        X1Z[J]=IX1[I]
        B2Z[J-1]=IX1[I]+AF
        OKZ[J-1]=IOK[I-1]
        XGZ[J-1]=IXG[I-1]
        RK2Z[J-1]=(IX1[N]-B2Z[J-1])/2
        T1Z[J]=SLZ[J-1]*TJBR
        CM.T2Z[J-1]=int(T1Z[J]*9.85+0.5)
        CM.T2Z[J-1]=CM.T2Z[J-1]*0.1
        YZ[J-1]=YZ[J-2]+T1Z[J]
        if (I < N):
            I=I+1
            J=J+1
            goto ._1210

        label ._1350
        if (JV != 0):
                ISLUT=1
                goto ._1275
                
        ''' New N '''

        N=J
        tempx=False

    ''' Steps of outer-limb, thickness of packet, number of
        cooling ducts, yoke height, X1MAX for the core '''

    ''' The first packet '''
    if tempx:
        RK2Z[0]=(X1Z[N]-B2Z[0])/2
        T1Z[1]=SLZ[0]*TCORST
        YZ[0]=T1Z[1]
        for I in range(2,N+1):
            RK2Z[I-1]=(X1Z[N]-B2Z[I-1])/2
            if (SLZ[I-1] == 1):LCD=LCD+1
            T1Z[I]=SLZ[I-1]*TCORST
            if (SLZ[I-1] == 1):T1Z[I]=P
            YZ[I-1]=YZ[I-2]+T1Z[I]

        if (SLZ[N-1] <= 2):
            T1Z[N]=P*0.5
            YZ[N-1]=YZ[N-1]-P*0.5

        if (LCD !=0):
            if (LCD/2*2 != LCD):
                LCD=LCD*2-1
                if (SLZ[N-1] >=2):LCD=LCD+1
            else:
                LCD=LCD*2
                if (SLZ[N-1] == 1):LCD=LCD-1
        
        IOH=OKZ[N-1]
        X1MAX=X1Z[N]
        NCD=LCD
        NB=N-NCD
        X1MIN  = COM[48]
        DCORN  = COM[50]
        DB     = COM[51]

        ''' Space for supporting plate '''

        EL=0.
        for I in range(1,N+1):
            if (XGZ[I-1] <=TWSUPC):break
            EL=EL+T1Z[I]

    ''' Length of yoke '''
    
    B2MAX=B2Z[N-1]
    ITYP=TYP
    if (ITYP == 7):
        OKL=2.*PLIMBY+B2MAX
    elif (ITYP == 8):
        OKL=PLIMB+2.*PLIMBY+B2MAX
    elif (ITYP == 9 or ITYP == 10):
        OKL=2.*(PLIMB+PLIMBY)+B2MAX
       
    ''' Calculating turn voltage area, mass, yoke re-inforcement '''

    for I in range(1,N+1):
        RKVCM1=SLZ[I-1]*X1Z[I]+RKVCM1
        RKVCM2=SLZ[I-1]*B2Z[I-1]+RKVCM2
        RKVCM=SLZ[I-1]*OKZ[I-1]+RKVCM
        TX=TX+SLZ[I-1]*X1Z[I]*XGZ[I-1]
        TY=TY+SLZ[I-1]*B2Z[I-1]*XGZ[I-1]
        SLA=SLA+SLZ[I-1]*X1Z[I]*OKZ[I-1]
        SLE=SLE+SLZ[I-1]*B2Z[I-1]*OKZ[I-1]
        SLU=SLU+SLZ[I-1]*OKZ[I-1]*RK2Z[I-1]


    DA=TNCORS*8.*DENCST*1.E-2
    RKVCM1=RKVCM1*TNCORS*0.04
    UTURN0=RKVCM1*2.22*0.01
    TIT=TNCORS*0.02
    RKVCM2=RKVCM2*TIT
    RKVCM=RKVCM*TIT
    KF=2.*RKVCM/RKVCM1
    IHO=TYP-6
    if (IHO >3):IHO=3
    TX=TX*DA*float(IHO)
    RKB1=RKVCM1*float(IHO)*DENCST
    TY=TY*DA
    RKB2=RKVCM2*2.*DENCST
    SLS=RKB1+RKB2
    ITXTY=int(TX+TY+0.5)
    SLA=SLA*float(IHO)*DA
    SLE=SLA+SLE*DA
    ISLE=int(SLE+0.5)
    IHB=(TYP-6)*2
    if (abs(TYP-10.)< 0.001): IHB=3
    RKO1=RKVCM*2.*DENCST
    RKO2=-SLU*DA-float(IHB)*RKVCM*TCD*DENCST-SLE
    IKO2=int(RKO2+0.5)

    ''' Contact width of the winding support '''

    for I in range(1,N+1):
        if (XGZ[I-1] <=1):
            YB=YZ[N-1]-YZ[I-2]
            break
 
    FYFAKT=400.*RKVCM1/(numpy.pi*(DCOR*DCOR))
    ISLS=int(HLIMB*SLS+float(ITXTY)+0.5)
    ISLU=int(OKL*RKO1+RKO2+0.5)
    IVIKT=ISLS+ISLU+ISLE
    ISLS=ISLS+ISLE/2
    ISLU=ISLU+ISLE/2

    COM[15] = FINDR
    COM[21] = TWSUPC
    COM[25] = TANSL
    COM[43] = UTURN0
    COM[44] = FYFAKT
    COM[45] = RKVCM1+0.5
    COM[46] = OKF
    COM[47] = NB
    COM[48] = X1MIN
    COM[49] = X1MAX
    COM[50] = DCORN
    COM[51] = DB
    COM[52] = N

    ''' HLIMB*SLS+ITXTY,  OKL*RKO1+IKO2 '''

    COM[54] = SLS
    COM[55] = ITXTY
    COM[56] = RKO1
    COM[57] = IKO2
    COM[70] = TASEC1
    COM[71] = TASEC2
    COM[75] = 2.*RKVCM2/RKVCM1
    COM[76] = int(HLIMB*RKB1+TX+0.5)
    COM[77] = int(HLIMB*RKB2+TY+0.5)
    COM[78] = RKB1
    COM[79] = RKB2
    COM[80] = TX
    COM[81] = TY
    COM[82] = IVIKT
    COM[86] = NCD
    COM[87] = ISLS
    COM[88] = ISLU
    COM[89] = ISLE
    COM[90] = IOH
    COM[91] = 2.*YZ[N-1]
    COM[92] = OKL
    COM[93] = YB
    COM[95] = EL

    return (COM,SLZ,X1Z,B2Z,OKZ,XGZ,RK2Z,T1Z,YZ)
