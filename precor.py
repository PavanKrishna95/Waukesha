
''' Title:  Calculates some input data required by
            the subroutine CORE '''
from dnet import DNET
import numpy
def PRECOR(DCOR,HLIMB,KSERIE,ACCTR,T1,T2,BBFLPL,
           KOD,BSMAX,BSTEP,TYP,TCD):

    TCAD=[0. for i in range(6)]
    FLPL=[0. for i in range(15)]
    RNFLPL=0.0
    TFLPL=0.0
    BFLPL=0.0
    FLPL[0]= 2.
    FLPL[1]=75.
    FLPL[2]=10.
    FLPL[3]= 2.
    FLPL[4]=75.
    FLPL[5]=12.
    FLPL[6]= 2.
    FLPL[7]=75.
    FLPL[8]=15.
    FLPL[9]= 4.
    FLPL[10]=60.
    FLPL[11]=12.
    FLPL[12]= 4.
    FLPL[13]=75.
    FLPL[14]=12.

    TCAD[0]= 4.
    TCAD[1]=75.
    TCAD[2]=12.
    TCAD[3]= 6.
    TCAD[4]=75.
    TCAD[5]=12.

    ''' Net Diameter, Maximum Limb-plate width
        Number of and space for flitch plates '''

    if (TYP >=7.) :
        R=0.5
        THLP=TCD
    else :
        R=1.
        THLP=0.

    ''' TAA and TAC '''

    DCORN=DNET(KSERIE,KOD,HLIMB,ACCTR,DCOR,T1,T2)
    print(DCORN)
    if KSERIE %5==1:
        if (BBFLPL) :
            if (DCOR >= 700.) :
                B1MAX=DCOR-34.9
            else :
                B1MAX=DCOR-29.9

        else :
            if (DCOR > 400.) :
                S=45.
            else :
                S=25.
    
            H=0.5*DCORN-0.5*numpy.sqrt(DCORN*DCORN-S*S)
            B1MAX=DCORN-2.*H
    
        B1MAX=10.*int(B1MAX*0.1)
        HLP=abs(BSMAX-B1MAX)
        B1MAX=B1MAX-numpy.mod(HLP,BSTEP)
        BT=0.
        TT=0.

        if (not BBFLPL) :
            if (KOD == 1) :
                if (RNFLPL < 4.) :
                    BT=80.
                elif (not(RNFLPL >=4. and BFLPL == 75.)) :
                    BT=130.
                else :
                    BT=160.

                TT=2.+TFLPL+2.+0.5
            else :
                BT=int(RNFLPL)/2*BFLPL+int(RNFLPL)/2*5-5
                TT=TFLPL+2.
    
        B1M=90.

        ''' TBA '''

    elif KSERIE %5 ==2:
        if (DCOR >= 700.) :
            B1MAX=DCOR-34.9
        else :
            B1MAX=DCOR-29.9

        B1MAX=10.*int(B1MAX*0.1)
        HLP=abs(BSMAX-B1MAX)
        B1MAX=B1MAX-numpy.mod(HLP,BSTEP)
        BT=0.
        TT=0.

        if ( not BBFLPL) :
            if (DCOR < 360.) :
                J=1
            elif (DCOR < 450.) :
                J=4
            elif (DCOR < 590.) :
                J=7
            elif (DCOR < 805.) :
                J=10
            else :
                J=13

            RNFLPL=FLPL[J-1]
            BFLPL=FLPL[J]
            TFLPL=FLPL[J+1]

        BT=int(RNFLPL)/2*BFLPL+int(RNFLPL)/2*5-5
        if (KOD == 1) :
            TT=2.+TFLPL+2.
        else :
            TT=TFLPL+2.
 
        B1M=60.
       
        ''' TAA-M '''

    elif KSERIE % 5 ==3:
        if (BBFLPL) :
            if (DCOR >= 700.) :
                B1MAX=DCOR-34.9
            else :
                B1MAX=DCOR-29.9

        else :
            if (DCOR > 400.) :
                S=45.
            else :
                S=25.

            H=0.5*DCORN-0.5*SQRT(DCORN*DCORN-S*S)
            B1MAX=DCORN-2.*H

        B1MAX=10.*int(B1MAX*0.1)
        HLP=abs(BSMAX-B1MAX)
        B1MAX=B1MAX-numpy.mod(HLP,BSTEP)
        BT=0.
        TT=0.

        if ( not BBFLPL) :
            if (KOD == 1) :
                if (RNFLPL < 4.) :
                    BT=80.
                elif (BFLPL != 75.) :
                    BT=130.
                else :
                    BT=160.

                TT=2.+TFLPL+2.+0.5
            else :
                BT=int(RNFLPL)/2*BFLPL+int(RNFLPL)/2*5-5
                TT=TFLPL+2.

        B1M=90.

        ''' TCA '''

    elif KSERIE%5 ==4:
        if (DCOR >= 700.) :
            B1MAX=R*(DCOR-34.9-THLP)

        else :
            B1MAX=R*(DCOR-29.9-THLP)
 
        B1MAX=10.*int(B1MAX*0.1)
        HLP=abs(BSMAX-B1MAX)
        B1MAX=B1MAX-numpy.mod(HLP,BSTEP)

        if ( not BBFLPL) :
            if (DCOR > 1040.) :
                J=4
            else :
                J=1

            RNFLPL=TCAD[J-1]
            BFLPL=TCAD[J]
            TFLPL=TCAD[J+1]
        
        BT=int(RNFLPL)/2*BFLPL+int(RNFLPL)/2*10-10
        TT=TFLPL+6.
        B1M=100.

        ''' Divided Core '''

    elif KSERIE %5==0:
        pass
 
    ''' Minimum Core Plate Width in the limb '''

    HX=0.5*DCORN-0.5*numpy.sqrt(DCORN*DCORN-BT*BT)
    print(BT,DCORN)
    HS=HX+TT
    
    RCORDA=numpy.sqrt(4.*((0.5*DCORN)**2-(0.5*DCORN-HS)**2))

    B1MIN=10.*int((R*RCORDA-R*THLP)*0.1+1.)
    
    B1MIN=max(B1MIN,B1M)
    
    return DCORN,B1MAX,B1MIN,BT,TT,RNFLPL,BFLPL,TFLPL
