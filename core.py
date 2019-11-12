
''' Title:  Calculates the core-section for core types D and T. '''
from ftjbr import FTJBR
from tbaok import TBAOK
from tacok import TACOK
from tcaok import TCAOK
from ltsok import LTSOK
from wdgsup import WDGSUP
from avtral import AVTRAL
import numpy
def CORE(COM,RNP,B1,B3,K1,TP,TS):
    import common as CM
    IND=[0 for i in range(5)]
    CDUCT=[0 for i in range(11)]
    NPL=[0 for i in range(100)]
    X1=[0. for i in range(101)]
    Y1=[0. for i in range(101) ]
    Y2=[0. for i in range(100)]
    YG=[0. for i in range(101)]
    OK=[0. for i in range(100)]
    XG=[0. for i in range(100)]
    ZX=[0. for i in range(101)]
    ZY=[0. for i in range(101)]
    ZU=[0. for i in range(11)]
    
    POE=2.
    P=4.2
    DENCST=7.65E-4
    OLAPP=20.
    TISOL=2.
    TANSL=0

    ''' Internal designations and constants '''

    TYP    = COM[0]
    DCOR   = COM[1]
    DCORN  = COM[2]
    PLIMB  = COM[4]
    HLIMB  = COM[5]
    BSTEP  = round(COM[6])
    IPMIN  = COM[7]
    TCORST = COM[8]
    ETA    = COM[9]
    NCD    = round(COM[10])
    BLADN  = COM[11]
    B1MIN  = COM[12]
    B1MAX  = COM[13]
    AF     = COM[17]
    TT     = COM[18]
    TWSUPC = COM[32]
    TH     = COM[33]
    TB     = COM[34]
    KSERIE = round(COM[35])
    OHRED  = COM[36]
    ILACK  = round(COM[37])
    if(COM[39] == 0.): COM[39]= COM[9]
    ETAL   = COM[39]
    FINDR  = COM[40]
    DYL    = COM[41]
    IADON  = COM[42]
    BLEAK  = COM[43]
    
    TNCORS=TCORST*ETA
    print(TCORST,ETA)

    ''' Maximum number of widths '''

    N=int(int(B1MAX-B1MIN)/round(BSTEP)+1)
    ''' Laying out the limb-section '''

    RCORN=0.5*DCORN

    ''' Laying out packet No. 'N' '''

    X1[N]=0.5*B1MAX
    Y2[N-1]=numpy.sqrt(RCORN*RCORN-X1[N]*X1[N])
    TJBR=FTJBR(TNCORS,ETA,ETAL,ILACK,TYP,DCOR,B1MAX)
    Y2[N-1]=(BLADN*TJBR)*int(Y2[N-1]/(BLADN*TJBR))
    Y1[N]=Y2[N-1]

    ''' Laying out packet No. 'N-1' DOWN TO PACKET NO. 1 '''

    J1=N-1
    
    for JPKT in range(1,J1+1):
        
        IPKT=N-JPKT
        X1[IPKT]=X1[IPKT+1]-(0.5*BSTEP)
        Y2[IPKT-1]=numpy.sqrt(RCORN*RCORN-X1[IPKT]*X1[IPKT])
        TVAX=2.*X1[IPKT]
        TJBR=FTJBR(TNCORS,ETA,ETAL,ILACK,TYP,DCOR,TVAX)
        Y2[IPKT-1]=BLADN*TJBR*int(Y2[IPKT-1]/(BLADN*TJBR))
        Y1[IPKT]=Y2[IPKT-1]-Y2[IPKT]

    ''' Minimum thickness of packet '''
    
    X1[0]=0
    ZX[0]=0
    Y1[0]=0.
    ZY[0]=0.
    ITEST=0
    YTA1=0.
    YTA2=0.

    ''' From J=1 up to J=N '''

    M=1
    
    while(M != 3):
       
        if M ==1:
            for I in range(1,N+1):
                ZX[I]=X1[I]
                ZY[I]=Y1[I]

            N1=N
            J=1
            L=0
    
            while(L !=1):
                TJBR=FTJBR(TNCORS,ETA,ETAL,ILACK,TYP,DCOR,2.*ZX[J])
                PMIN=TJBR*float(IPMIN)-0.1
                if(ZY[J] < PMIN):
                    ZY[J]=ZY[J]+ZY[J+1]
                    N1=N1-1
                    K=J+1
                    for I in range(K,N1+1):
                        ZY[I]=ZY[I+1]
                        ZX[I]=ZX[I+1]

                    continue

                if(J ==N1):
                    L=1
                else:
                    J=J+1
    
            if (ITEST == 1) :
                for I in range(1,N1+1):
                    X1[I]=ZX[I]
                    Y1[I]=ZY[I]
 
                N=N1
                M=3
            else:
                for I in range(1,N1+1):
                    YTA1=YTA1+ZX[I]*ZY[I]
  
                M=2

        elif M==2:
            for I in range(1,N+1):
                ZX[I]=X1[I]
                ZY[I]=Y1[I]

            N2=N
            J=N2
            L=0
            while(L != 1):
                
                TJBR=FTJBR(TNCORS,ETA,ETAL,ILACK,TYP,DCOR,2.*ZX[J])
                PMIN=TJBR*float(IPMIN)-0.1

                if (ZY[J] < PMIN):
                    
                    if (J!=1) :
                        ZY[J-1]=ZY[J]+ZY[J-1]
    
                    N2=N2-1
                    K=J
                    for I in range(K,N2+1):
                        ZY[I]=ZY[I+1]
                        ZX[I]=ZX[I+1]
 
                    continue
                if (J == 1) :
                    L=1
                else:
                    J=J-1

            if (ITEST != 1):

                for I in range(1,N2+1):
                    YTA2=YTA2+ZX[I]*ZY[I]
 
                ITEST=1

                for I in range(1,N+1):
                    ZX[I]=X1[I]
                    ZY[I]=Y1[I]
 
                if (abs(YTA1-YTA2) > YTA1*0.001):
                    if (YTA1-YTA2 >=0.) :
                        M=1
                    else:
                        M=2

                else:
                    if (N1-N2 <= 0) :
                        M=1
                    else:
                        M=2
            
            else:
                for I in range(1,N2+1):
                    X1[I]=ZX[I]
                    Y1[I]=ZY[I]

                N=N2
                M=3

    X1MAX=X1[N]
    X1MIN=X1[1]
    Y2[N-1]=Y1[N]
    J1=N-1

    for J in range(1,J1+1):
        I=N-J
        Y2[I-1]=Y2[I]+Y1[I]

    IV=0
    L=0
    LNCD=0

    if (NCD == 0) :
        L=7
    else:
        L=1

    while(L != 8):

        if L==1:
            LNCD=NCD
            SL2=0.
            SL1=100.
            DY=TCORST*BLADN
            SLI=0.
            for I in range(0,11):
                CDUCT[I]=0
                ZU[I]=0.
 
            for I in range(1,N+1):
                SLI=SLI+X1[I]*Y1[I]


            RKYLY=2.*Y2[0]+X1MAX-float(LNCD)*P
            for I in range(1,int((LNCD+1)/2)+1):
                if (LNCD-2*(LNCD/2) == 0) :
                  M=int(float(N)*((2.*float(I)/float(LNCD))**(1./3.))+0.5)
                else:
                  M=int(float(N)*((2.*float(I)/float(LNCD+1))**0.25)+0.5)
                  IV=1

                SLI=SLI-P*X1[M]
                RKYLY=RKYLY+2.*X1[M]
            
            if (IV!=0) :
                SLI=SLI+0.5*P*X1[N]
                RKYLY=RKYLY-X1[N]

            RNY=SLI*ETA*DENCST*100.*POE/RKYLY

            if (IV!=1) :
                LNCD=LNCD/2
            else:
                LNCD=(LNCD-1)/2
                CDUCT[0]=N+1
                IANT=0
                IHO=0
                Y2[N]=0.5*P
                Y1[N]=Y1[N]-Y2[N]
       
            L=2

        elif L==2:
            RKYLY=X1[N]
            if (IV == 1): RKYLY=2.*RKYLY
            I=N
            SLI=0.
            AUX=ETA*DENCST*100.*POE
            IANT=1
            L=3
            
        elif L==3:
            X=(RNY*RKYLY-AUX*SLI)/(AUX*X1[I]-2.*RNY)
            L=4
    
        elif L==4:

            if (X > Y1[I] or IANT > LNCD):
                RKYLY=RKYLY+2.*Y1[I]
                SLI=SLI+X1[I]*Y1[I]
                if (I == CDUCT[IANT-1]) :
                    RKYLY=RKYLY-2.*(ZU[IANT-1]+P)
                    SLI=SLI-X1[I]*(ZU[IANT-1]+P)
                I=I-1
                if (I == 0) :
                    L=6
                else:
                    L=3
               
            elif (I !=CDUCT[IANT-1]):
                L=5
                
            elif (Y1[I]-X-ZU[IANT-1]-P >= 0.):
                X=X+ZU[IANT]+P
                L=5
                
            else:X=Y1[I]+10.
 
        elif L==5:

            if (Y1[I] >= 3.*P):
                if (X <= P) :
                    ZU[IANT]=P
                else:
                    if (X > Y1[I]-2.*P) :
                        ZU[IANT]=Y1[I]-2.*P
                    else:
                        ZU[IANT]=DY*int(X/DY)

            else:
                if (Y1[I] < 2.*P) :
                    I=I-1
                    ZU[IANT]=DY
                else:
                    if (X <=1.2) :
                        ZU[IANT]=1.2
                    else:
                        if (X >Y1[I]-6.) :
                            ZU[IANT]=Y1[I]-6.0
                        else:
                            ZU[IANT]=1.2
    
            CDUCT[IANT]=I
            RKYLY=2.*X1[I]
            SLI=0.
            IANT=IANT+1
            L=3
    
        elif L==6:
            WDM=AUX*SLI/RKYLY
            SLD=RNY-WDM
            if (abs(SLD) <= 0.050*RNY) :
                L=7
            else:
                if (RNY >= WDM and SL1 >= RNY): SL1=RNY
                if (RNY < WDM and SL2 < RNY): SL2=RNY
                if (SL1 < 100. and SL2 > 0.) :
                    RNY=(SL1+SL2)*0.5
                else:
                    RNY=RNY-SLD/(float(LNCD)+1.)

                if (abs(SL1-SL2)<0.11) :
                    WDM=(SL1+SL2)*0.5
                    L=7
                else:
                    IANT=0
                    IHO=IHO+1
                    if (IHO > 10) :
                        L=8
                    else:L=2


        elif L==7:
            NCD=LNCD

            for I in range(1,N+1):
                X1[I]=2.*X1[I]
        
            if (KSERIE == 2 and DCOR >=340.):
                ''' TBA -yoke '''
                OK,XG=TBAOK(N,BSTEP,X1,OLAPP,DCOR,TT,Y1,TWSUPC,
                            TH,TB,OHRED)

            elif(KSERIE == 4):
                ''' TCA-yoke '''
                KTEST=0
                L1=0

                while(L1 != 1):
                    temp=True
                    while(temp):
                        temp=False
                        OK,XG,CM.BBPPRT1,CM.BBPPRT2=TCAOK(TYP,N,OLAPP,BSTEP,DCOR,TWSUPC,AF,X1,
                              Y1,FINDR)
                        BBSLIM=False
                        if (BLEAK >= 1.E-6):
                            T=XG[0]
                            J=1
                            for I in range(1,N+1):
                                if (XG[I-1] <= T-1.E-5) :
                                    IND[J-1]=I
                                    J=J+1
    
                                T=XG[I-1]

                            TSUM=0.

                            for I in range(1,IND[0]):
                                TSUM=TSUM+Y1[I]

                            HEELS=TSUM
                            H1=OK[IND[0]-1]
                            H2=OK[IND[1]-1]
                            DUMMY=TWSUPC
                            KTEST,TWSUPC,TANSL,CM.WMARG,CM.TMARG=WDGSUP(FINDR,IADON,DYL,DCOR,HEELS,H1,H2,BLEAK,TWSUPC,
                                   BBSLIM)
                            if (DUMMY !=TWSUPC):
                                temp=True
                                continue

                            if (KTEST !=1) :L1=1
                            else:
                                FINDR=FINDR+0.1

                        else:L1=1

            elif ( KSERIE == 6):
                ''' TAC-yoke '''
                XG,OK=TACOK(DCOR,BSTEP,N,X1,Y1)

            else:
                ''' TAA-yoke '''

                OK[0]=X1[2]+OLAPP

                for I in range(2,N+1):
                    OK[I-1]=X1[I]+OLAPP

                for I in range(1,N+1):
                    XG[I-1]=0.
 
                if ( not CM.BBTAAE) :
                    XG[2]=OK[3]-OK[2]
                    XG[1]=OK[3]-OK[1]
                    XG[0]=XG[1]

                    ''' Extended TAA '''
                else:
                    M=N
                    IX1=1
                    XG=AVTRAL(M,IX1,XG,Y1,70.,14.)
                    IX1=1
                    XG=AVTRAL(M,IX1,XG,Y1,40.,70.)

                    N1=N-1
                    I=1
                    while(I <=N1):
                        if (XG[I]+OK[I] >= XG[I-1]+OK[I-1]) :
                            I=I+1
                        else:
                            OK[I]=OK[I]+BSTEP
    

                ''' TAA-modified '''

                if (KSERIE == 3) :OK=LTSOK(OK,float(N))

            NB=N
            IHO=0
            for I in range(1,N+1):
                TS[I-1]=0.
 
            IEND=0
            YG[0]=0.

            TJBR=FTJBR(TNCORS,ETA,ETAL,ILACK,TYP,DCOR,X1[1])
            NPL[0]=int(Y1[1]/TJBR+0.1)
            B1[1]=X1[1]
            B3[0]=OK[0]
            K1[0]=XG[0]
            TP[1]=float(NPL[0])*TJBR
            TS[0]=TP[1]

            I=2
            J=2
            IANT=NCD
            L1=1

            while(L1 != 6):

                if L1 ==1:
           
                    if (NCD == 0) :

                        L1=4
                    else:
                        if (I != CDUCT[IANT]) :

                            if (IHO > 0) :
                                L1=2
                            else:
                                L1=4

                        else:IHO=IHO+2

                        if (IHO != 2) :
                            YG[IHO-3]=Y1[I]-P-ZU[IANT]
                            YG[IHO-1]=ZU[IANT]-P-YG[IHO-2]
                            IANT=IANT-1
                        else:
                            YG[IHO-1]=Y1[I]-P-ZU[IANT]
                            YG[IHO]=ZU[IANT]
                            IANT=IANT-1
       
                elif L1==2:
                    TJBR=FTJBR(TNCORS,ETA,ETAL,ILACK,TYP,DCOR,X1[I])
                    NPL[J-1]=int(YG[IHO-1]/TJBR+0.1)
                    B1[J]=X1[I]
                    B3[J-1]=OK[I-1]
                    K1[J-1]=XG[I-1]
                    TP[J]=float(NPL[J-1])*TJBR
                    TS[J-1]=TS[J-2]+TP[J]
                    IHO=IHO-2
                    L1=3
       
                elif L1==3:
                    J=J+1
                    NPL[J-1]=1
                    B1[J]=X1[I]
                    B3[J-1]=OK[I-1]
                    K1[J-1]=XG[I-1]

                    if (IEND == 1):
                        TP[J]=0.5*P
                        TS[J-1]=TS[J-2]+TP[J]
                        L1=6
                    else:
                        TP[J]=P
                        TS[J-1]=TS[J-2]+TP[J]
                        J=J+1

                        if (IHO != 0) :
                            L1=2
                        else:
                            TJBR=FTJBR(TNCORS,ETA,ETAL,ILACK,TYP,DCOR,X1[I])
                            NPL[J-1]=int(YG[2]/TJBR+0.1)
                            B1[J]=X1[I]
                            B3[J-1]=OK[I-1]
                            K1[J-1]=XG[I-1]
                            TP[J]=float(NPL[J-1])*TJBR
                            TS[J-1]=TS[J-2]+TP[J]
                            IHO=0

                            if (I >=N) :
                                L1=5
                            else:
                                I=I+1
                                J=J+1
                                L1=1
                                

                elif L1==4:
                    TJBR=FTJBR(TNCORS,ETA,ETAL,ILACK,TYP,DCOR,X1[I])
                    NPL[J-1]=int(Y1[I]/TJBR+0.1)
                    B1[J]=X1[I]
                    B3[J-1]=OK[I-1]
                    K1[J-1]=XG[I-1]
                    TP[J]=float(NPL[J-1])*TJBR
                    TS[J-1]=TS[J-2]+TP[J]

                    if (I >=N) :
                        L1=5
                    else:
                        I=I+1
                        J=J+1
                        L1=1


                elif L1==5:
                    if (IV == 0) :
                        L1=6
                    else:
                        IEND=1
                        L1=3


            N=J
            ACORE=0.
            AOK=0.
            S1=0.
            S2=0.
            for I in range(1,N+1):
                ACORE=ACORE+float(NPL[I-1])*B1[I]
                AOK= AOK+float(NPL[I-1])*B3[I-1]
                S1=S1+float(NPL[I-1])*B1[I]*K1[I-1]
                S2=S2+float(NPL[I-1])*B1[I]*B3[I-1]
            
            ACORE=ACORE*TNCORS*2.E-2
            AOK=AOK*TNCORS*2.E-2
            UTURN0=ACORE*2.22144E-2
            OKF=AOK/ACORE
            FYFAKT=4.*ACORE/(numpy.pi*(DCOR*DCOR))*100.

            ''' GBEN=HLIMB*GB+G1, GOK=PLIMB*GO-G2, GHORN=GHORN '''

            NBEN=2
            if (TYP == 3.): NBEN=3
            GB=ACORE*float(NBEN)*DENCST
            G1=S1*TNCORS*DENCST*float(NBEN)*4.E-2
            GO=AOK*float(NBEN-1)*2.*DENCST
            GHORN=S2*TNCORS*DENCST*float(NBEN)*4.E-2
            G2=-0.667*GHORN
            if (TYP == 1.): G2=-0.5000*GHORN
            GBEN=HLIMB*GB+G1
            GOK=PLIMB*GO+G2

            COM[14]=GBEN
            COM[15]=GOK
            COM[16]=GHORN
            COM[19]=UTURN0
            COM[20]=FYFAKT
            COM[21]=ACORE
            COM[22]=OKF
            COM[23]=GB
            COM[24]=G1
            COM[25]=GO
            COM[26]=G2
            COM[27]=B3[N-1]
            COM[28]=2.*Y2[0]
            COM[29]=N
            COM[30]=NB
            COM[31]=AOK
            COM[32]=TWSUPC
            COM[40]=FINDR
            COM[44]=TANSL

            for I in range(1,N+1):
                RNP[I-1]=float(NPL[I-1])

            L=8
    
    return COM,RNP,B1,B3,K1,TP,TS
