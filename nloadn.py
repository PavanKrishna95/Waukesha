import math
from frnat import FRNAT
from snolo import SNOLO
from pnolo import PNOLO
from rnolo import RNOLO
from soundp import SOUNDP
def NLOADN(BBRESC):
    print("start of nloadn")
    import com as C
    #Start of the declarations block
    BLIM=[0 for i in range(3)]
    FR1=0
    FR2=0

    #End of the declarations block
    BLIM[0]=C.BLIMB
    BLIM[1]=C.BLIMB*C.BMAXPU
    BLIM[2]=C.BLIMB*C.BMINPU
    SEQ=C.SEQU2W*float(C.NWOULI)
    BLADN=C.AARR[139]
    PCORR = 1
    QCORR = 1

    BBRES=False

    #Calculate resonant frequencies
    #If required

    if(BBRESC):
    #Calculate
    # NO Side-limbs  
        if((C.TYPCOR==1)or(C.TYPCOR)==3):
    
    #calculate        
            BBRES,FR1,FR2=FRNAT(C.TYPCOR,C.FREQ,C.DCORE,C.PLIMB,C.HLIMB)        #watchout  
            CORRES='Core resonance NOT likely(ZK-TA 4567-101E)'

            if(BBRES):
                CORRES='>> Core resonance likely (ZK-TA 4567-101E)'

            C.JFC="Natural frequencies (F1,F2)={0},{1} Hz, {2} ".format(round(FR1),round(FR2),CORRES)

    #Side-limbs
    # No calc
        else:
            CORRES='No check on core resonance done (ZK-TA 4567-101E)'    

            C.JFC=CORRES

    BBSTOP=False

    # For each tap

    for I in range(1,4):
    #Calculate sound level and loss values
    
    #If not BBSTOP
        if(not BBSTOP):
    #TA1 Core
            if(C.KCORE==101):
                if(C.UARR[22]=='YES'):
                    TSTP=1
                else:
                    TSTP=0

            else:
                if(C.EXTCOR):
                    CORR=1.33
                    print("NLOADN calling RNOLO")
                    C.P00[I-1]= RNOLO( C.TYPCOR, BLIM[I-1], C.FREQ, C.YOKAMP, C.SBF,CORR,
                                       C.GLIMBM, C.GLIMBY, C.GYOKE, C.GCORN,
                                       C.PSPL1,  C.PSPL2,  C.PSPL3,C.PSPHD1,
                                       C.PSPHD2, C.PSPHD3,C.PSPHT1, C.PSPHT2,
                                       C.PSPHT3,C.PSPTY1, C.PSPTY2, C.PSPTY3)
                    print(C.P00,I,'pavan')

                    CORR=1.25
                    print("NLOADN calling RNOLO")
                    C.Q00[I-1]= RNOLO( C.TYPCOR, BLIM[I-1], C.FREQ, C.YOKAMP, C.SBF,CORR,
                                       C.GLIMBM, C.GLIMBY, C.GYOKE, C.GCORN,C.SSPL1,C.SSPL2,
                                       C.SSPL3,C.SSPHD1, C.SSPHD2, C.SSPHD3,C.SSPHT1,
                                       C.SSPHT2, C.SSPHT3,C.SSPTY1, C.SSPTY2, C.SSPTY3)

                else:
                    print("NLOADN calling PNOLO")
                    C.P00[I-1]=PNOLO(C.TYPCOR,BLIM[I-1],C.FREQ,C.YOKAMP,C.SBF,C.ISTGRD,
                                     C.GLIMBM,C.GLIMBY,C.GYOKE,C.GCORN,BLADN)
                    print("NLOADN calling SNOLO")
                    C.Q00[I-1]=SNOLO(C.TYPCOR,BLIM[I-1],C.FREQ,C.YOKAMP,C.SBF,C.ISTGRD,
                                     C.GLIMBM,C.GLIMBY,C.GYOKE,C.GCORN,BLADN)

                BBSTOP=(not C.BBVFR)

            print("NLOADN calling SOUNDP")
            C.SOUND0[I-1]=SOUNDP(C.TYPCOR,C.DCORE,C.PLIMB,C.HLIMB,C.ISTGRD,BLIM[I-1],C.FREQ,C.JFC)

        if(C.BB132):   C.SOUND0[I-1]=C.SOUND0[I-1]-10

    #Adjust sound level and loss values   
     
    # If not variable flux regulation
    
    # Reduction between sound power level and sound pressure level    
    if(abs(C.HTANK)<1.E-6):
        C.SPRED=0
    else:
        C.SPRED=10*math.log10(1.25*C.HTANK*(2*C.BTANK+2*C.RLTANK+1.9))

    if(not C.BBVFR):
        C.SOUND0[1]=C.SOUND0[0]
        C.P00[1]=C.P00[0]
        C.Q00[1]=C.Q00[0]

    print("ending of NLOADN")    
    return BBRES                 
