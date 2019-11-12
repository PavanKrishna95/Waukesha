import numpy
def PNOLO(TYP,BLIMB,FREQ,OKF,SBF,ISTGRD,GB1,GB2,GO,GH,BLA):
    print("Starting of PNOLO")
    
 #   Coefficients for spec. iron losses. Constant term first

    PSP1=[0.12712500, -0.16000032, 0.42500013]
    PSP2=[-27.298521, 68.690477, -63.260419, 25.514539,
            -3.6788161]
    PSP3=[-2.2174400, 1.2000081, 0.49999783]

# Corner losses for Single phase cores

    PSPHD1=[0.0316053,-0.21666705,0.50000017]
    PSPHD2=[20.530720,-60.188503,66.224117,-32.081477,5.9078875]
    PSPHD3=[91.316943,-103.79994,29.999984]
# Corner losses for T-cores

    PSPH11=[-0.22683000, 0.50000002, 0.25000000]
    PSPH12=[76.056176, -207.05085, 212.08404, -96.271337,16.470603]
    PSPH13=[96.64430, -108.39995, 30.999986]

# Corner losses for TY-3 phase cores

    PSPH31=[0.13507766,-0.25555532,0.88888878]
    PSPH32=[-256.38768,669.21973,-650.81657,280.18065,-44.805779]
    PSPH33=[-38.897559,34.200064,-6.0000171]

    RK2=1.13
    PB1=0
    PB2=0
    PO=0
    PH=0

    if(BLA==4):
        RK3=1.16
    else:
        RK3=1

    ENFAS=(round(TYP)==1 or round(TYP)==7 or round(TYP)==8 or round(TYP)==9)

    BBSL=(round(TYP)>=7)

    if(BLIMB>1.8):
        PB1=GB1* numpy.polyval(PSP3[::-1],BLIMB)
        PO = GO* numpy.polyval(PSP3[::-1],BLIMB/OKF)
        if(BBSL): PB2=GB2*numpy.polyval(PSP3[::-1],BLIMB/SBF)

        if(round(TYP)==10):
            PH=GH* numpy.polyval(PSPH33[::-1],BLIMB)
        elif(ENFAS):
            PH=GH* numpy.polyval(PSPHD3[::-1],BLIMB)
        else:
            PH=GH* numpy.polyval(PSPH13[::-1],BLIMB)
    elif(BLIMB >= 1.3):
        PB1=GB1* numpy.polyval(PSP2[::-1],BLIMB)
        PO =GO * numpy.polyval(PSP2[::-1],BLIMB/OKF)
        if(BBSL): PB2=GB2* numpy.polyval(PSP2[::-1],BLIMB/SBF)

        if(round(TYP)==10):
            PH=GH* numpy.polyval(PSPH32[::-1],BLIMB)
        elif(ENFAS):
            PH=GH* numpy.polyval(PSPHD2[::-1],BLIMB)
        else:
            PH=GH* numpy.polyval(PSPH12[::-1],BLIMB)

    else:
        PB1=GB1* numpy.polyval(PSP1[::-1],BLIMB)
        PO =GO * numpy.polyval(PSP1[::-1],BLIMB/OKF)
        if(BBSL): PB2=GB2* numpy.polyval(PSP1[::-1],BLIMB/SBF)

        if(round(TYP)==10):
            PH=GH* numpy.polyval(PSPH31[::-1],BLIMB)
        elif(ENFAS):
            PH=GH* numpy.polyval(PSPHD1[::-1],BLIMB)
        else:
            PH=GH* numpy.polyval(PSPH11[::-1],BLIMB)
    PO=PO*RK2
    PH=PH*RK3 

    PNOLO=(PB1+PB2+PO+PH)*1.02 
    if(ISTGRD > 1):

        if(round(TYP)==1): 
            if (BLIMB>=1.85):
                RED =  0.4/1.5*BLIMB + 0.38
            elif (BLIMB>=1.75):
                RED =  0*BLIMB + 0.86
            elif (BLIMB>=1.4):
                RED = -1./3.5*BLIMB + 1.36
            elif (BLIMB>=1.2):
                RED = -0.25/2.*BLIMB + 1.135
            elif (BLIMB>=0.8):
                RED =  0.35/4.*BLIMB + 0.88
            else:
                RED = -0.5/8.*BLIMB + 1
            PNOLO  =  PNOLO * RED
            
        elif(round(TYP) in (2 ,4 ,5 ,6)):
            pass

        elif(round(TYP)==3):
            if (BLIMB>=1.80): 
                RED =  0.1*BLIMB + 0.705
            elif (BLIMB>=1.75):
                RED =  0*BLIMB + 0.885
            elif (BLIMB>=1.5):
                RED = -1.1/5*BLIMB + 1.27
            elif (BLIMB>=1.3):
                RED =  0*BLIMB + 0.94
            elif (BLIMB>=0.8):
                RED =  0.7/5*BLIMB + 0.758
            else:
                RED = -1.3/8*BLIMB + 1
            PNOLO  =  PNOLO * RED

        elif(round(TYP)==7):
            if (BLIMB>=1.75):
                RED = -0.1*BLIMB + 0.985
            elif (BLIMB>=1.6):
                RED = -1./3*BLIMB + 4.18/3
            elif (BLIMB>=1.4):
                RED = -0.1*BLIMB + 1.02
            elif (BLIMB>=0.8): 
                RED =  0.5/6*BLIMB + 2.29/3
            else:
                RED = -1.7/8*BLIMB + 1
            PNOLO  =  PNOLO * RED

        elif(round(TYP)==8):
            if (BLIMB>=1.75):
                RED = -0.1*BLIMB + 0.985
            elif (BLIMB>=1.6):
                RED = -1./3*BLIMB + 4.18/3
            elif (BLIMB>=1.4):
                RED = -0.1*BLIMB + 1.02
            elif (BLIMB>=0.8):
                RED =  0.5/6*BLIMB + 2.29/3
            else:
                RED = -1.7/8*BLIMB + 1
            PNOLO  =  PNOLO * RED
       
        elif(round(TYP)==9):
            if (BLIMB>=1.7):
                RED =  0.87
            elif (BLIMB>=1.2):
                RED =  -1.1/5*BLIMB + 6.22/5
            else:
                RED =  1
            PNOLO  =  PNOLO * RED

        elif(round(TYP)==10):    
            if (BLIMB>=1.7):
                RED =  0.9
            elif (BLIMB>=1.2):
                RED =  -0.8/5*BLIMB + 5.86/5
            else:
                RED =  1
            PNOLO  =  PNOLO * RED
    
    ''' Quality 4 (Plasmajet) inserted 90.01.11 '''

    if(ISTGRD ==3 or ISTGRD == 4):

        if (BLIMB < 1.4):
            PNOLO=PNOLO*(0.08713*BLIMB+0.6189848)*0.96
        else:
            PNOLO=PNOLO*(3.7922*BLIMB**4-25.7589*BLIMB**3
                         +65.05881*BLIMB**2-72.41348*BLIMB+30.71891)*0.96

        ''' Change after Memo 870924 from ZKDA  C. Bengtsson '''

        PNOLO = PNOLO * 0.995

        ''' Change after Memo 891005 from TDA  C. Bengtsson '''
        ''' JUSTERING FaR KVALITET PLJT '''

        if(ISTGRD == 4): PNOLO = PNOLO * 1.13

    ''' M5 - Core Plate Quality '''

    ''' Change after Memo 870924 from ZKDA  C. Bengtsson
        'Justering av farlustvrdena far 0.23 mm ZDKH och 0.30 mm M5' '''

    if (ISTGRD == 1): PNOLO = PNOLO * 0.965

    ''' ARLS ARMCO LASER SCRIBED FOR UAW, 89 % OF HIBI '''

    if(ISTGRD == 5): PNOLO = 0.89*PNOLO

    if(ISTGRD >= 11):
        ''' MORE REDUCTION FOR M5L-QUAL. '''

        if(BLIMB >= 1.5):
            RED = -0.1/2*BLIMB + 1.045
        elif (BLIMB >= 0.8):
            RED =  0*BLIMB + 0.97
        else:
            RED = -0.3/8*BLIMB + 1

        PNOLO = PNOLO * RED

    if(FREQ > 55.): PNOLO=PNOLO*1.33/1.02

    return PNOLO
