import numpy
def RNOLO(TYP, BLIMB, FREKV, OKF, SBF, CORR,
          GB1, GB2, GO, GH,PSPL1,  PSPL2,  PSPL3,
          PSPHD1, PSPHD2, PSPHD3,PSPHT1, PSPHT2, PSPHT3,
          PSPTY1, PSPTY2, PSPTY3):

    ITYP   = int(TYP+0.1)
    print("starting of RNOLO")

    PB1=0
    PB2=0
    PO=0
    PH=0    

    SINGPH=(ITYP==1 or ITYP==7 or ITYP==8 or ITYP==9)
    SIDELI=(ITYP >= 7)

    if(BLIMB > 1.8):
        PB1 = GB1 * numpy.polyval(PSPL3[::-1], BLIMB)
        PO  = GO  * numpy.polyval(PSPL3[::-1], BLIMB/OKF)
        if(SIDELI):
            PB2 = GB2 * numpy.polyval(PSPL3[::-1],  BLIMB/SBF)
        if(not(SINGPH or ITYP ==10) ):
            PH  = GH  * numpy.polyval(PSPHT3[::-1], BLIMB)
            
        else:
            if(not(ITYP==10)):
                PH  = GH  * numpy.polyval(PSPHD3[::-1], BLIMB)
            else: 
                PH  = GH  * numpy.polyval(PSPTY3[::-1], BLIMB)

    elif(1.3<=BLIMB<=1.8):
        PB1 = GB1 * numpy.polyval(PSPL2[::-1],  BLIMB)
        PO  = GO  * numpy.polyval(PSPL2[::-1],  BLIMB/OKF)
        if(SIDELI):
            PB2 = GB2 * numpy.polyval(PSPL2[::-1],  BLIMB/SBF)

        if(not(SINGPH or ITYP==10)):
            PH  = GH  * numpy.polyval(PSPHT2[::-1], BLIMB)
            
        else:
            if(not(ITYP==10)):
                PH  = GH  * numpy.polyval(PSPHD2[::-1], BLIMB)
            else:
                PH  = GH  * numpy.polyval(PSPTY2[::-1], BLIMB)

    else:
        PB1 = GB1 * numpy.polyval(PSPL1[::-1],  BLIMB)
        PO  = GO  * numpy.polyval(PSPL1[::-1],  BLIMB/OKF)

        if(SIDELI):
            PB2 = GB2 * numpy.polyval(PSPL1[::-1],  BLIMB/SBF)

        if(not(SINGPH or ITYP ==10)):
            PH  = GH  * numpy.polyval(PSPHT1[::-1], BLIMB)
    
        else:
            if(not(ITYP==10)):
                PH  = GH  * numpy.polyval(PSPHD1[::-1], BLIMB)

            else:
                PH  = GH  * numpy.polyval(PSPTY1[::-1],BLIMB)

    RNOLO = ( PB1 + PB2 + PO + PH )
    if(FREKV>55): RNOLO = RNOLO * CORR
    print("ending of RNOLO")
    return RNOLO
