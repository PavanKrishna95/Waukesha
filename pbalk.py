#PBALK - MASS OF CORE CLAMPS
# MASS OF CORE CLAMPS
#      #####################
#
#
#      BBPRNT  PRINTOUT OF INPUT/OUTPUT DATA IF TRUE
#      JFC     FILECODE FOR PRINTOUT
#      KCORE = CORE SERIES CODE
#              1 = TAA
#              2 = TBA
#              3 = -
#              4 = TCA (WITH AND WITHOUT SIDELIMBS)
#              5 = LTB
#
#      NCOR  = CORE TYPE CODES:
#              1     3     7     8      9      10
#              D     T     EY    DY     TY-1   TY-3
#
#      DCORE = CORE DIAMETER    (MM)
#      OH    = YOKE HEIGHT      (MM)
#      BH    = LIMB HEIGHT      (MM)
#      BD    = LIMB PITCH       (MM)
#      TLIT  = THICKNESS OF WINDING SUPPORT (MM)
#      SMVA  = RATED POWER      (MVA)
#      OL    = YOKE LENGTH      (MM)
#      TK    = CORE THICKNESS   (MM)
#      BBSLIM= .TRUE.  IF SIDE LIMB CORE
#              .FALSE. IF NOT SIDE LIMB CORE
#      BBEXAC= .TRUE.  DURING  EXACT CALCULATION
#              .FALSE. DURING OPTIMIZING

def PBALK(BBPRNT,JFC,DCORE,OH,BH,BD,TLIT,BBEXAC,SMVA,OL,TK,KCORE,NCOR,BBSLIM):
    import common as CM
    
    B=[120,200,260]
    G=[43.6E-3,59.3E-3,75.0E-3]
    B85=[100,150,200]
    G1=[10.9E-3,22.3E-3,43.6E-3]
    G2=[2.47E-3,5.55E-3,7.99E-3]
    H86=[200,250,300]
    G3=[1.58E-3,2.47E-3,3.55E-3]

    if(BBPRNT):
       #WRITE(JFC,*) '===== INPUT DATA TO PBALK ====='
       #WRITE(JFC,*) DCORE,OH,BH,BD
       #WRITE(JFC,*) TLIT,BBEXAC,SMVA,OL
       #WRITE(JFC,*) TK,KCORE,NCOR,BBSLIM
        pass
    if(BBSLIM):
        QK1 =  0.93
        QK2 =  1900
        QK3 =  1975

        if(NCOR!=10):
            QK1 =  1.0
            QK2 =  805
            QK3 =  1045
        QK4 =  0.9917
        CM.TBALK = 40

        CM.GSN211 =QK4* (OH*OL*CM.TBALK* QK1 * 32.E-6 + QK2 + QK3)

        return JFC

    if(KCORE==1):
        if(BBEXAC):
            CM.IPBALK=1
            if(DCORE>315): CM.IPBALK = 2
            if(DCORE>430): CM.IPBALK = 3

        RL851 = 2* B85[CM.IPBALK-1] + TK + 130
        Q851 = 8*  G3[CM.IPBALK-1]*RL851
        RL850 = OH + BH + H86[CM.IPBALK-1] + 160
        Q850 = 8 * G2[CM.IPBALK-1]*RL850
        Q033 = G1[CM.IPBALK-1] * TK * 4.
        Q032 = (2*B85[CM.IPBALK-1] + TK +8)*0.1536
        CM.GSN211 =(G[CM.IPBALK-1]*4*(3*BD+B[CM.IPBALK-1])+Q032+Q033+Q850+Q851)*1.06  

        return JFC

    Q4=0.99
    if(BBEXAC):
        if(TLIT <= 0.1):
            CM.SBALK1 = 1.082

            HELP=  (BD-DCORE)/2
            CM.SBALK2 = 188
            if(HELP>285.):  CM.SBALK2 = 240
            if(HELP>350.):  CM.SBALK2 = 370

            CM.TBALK = 20
            if(DCORE >= 580): CM.TBALK = 30
            if(BD >= 1000):   CM.TBALK = 30
            if(DCORE>=800): CM.TBALK = 40
            if(BD >= 1400):   CM.TBALK = 40

            CM.SBALK3 = 421
            if(SMVA > 40):   CM.SBALK3 = 615
            CM.GSN211 =(OH*OL*CM.TBALK*CM.SBALK1*32.E-6 + CM.SBALK2 + CM.SBALK3 )* Q4
            return JFC
        CM.SBALK1 = 1.013

        CM.SBALK2 =  530
        if( (BD-DCORE)/2 > 350.): CM.SBALK2 = 857

        CM.SBALK3 =  875
        if( DCORE>800):  CM.SBALK3 = 1605

        CM.TBALK =  30    
        CM.GSN211 =(OH*OL*CM.TBALK*CM.SBALK1*32.E-6 + CM.SBALK2 + CM.SBALK3 )* Q4
        return JFC

    CM.GSN211 =(OH*OL*CM.TBALK*CM.SBALK1*32.E-6 + CM.SBALK2 + CM.SBALK3 )* Q4
    return JFC    
