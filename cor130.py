
''' TITLE:  CALCULATION OF CORE DATA FOR "130 KV CORE" '''

''' Used Glued core for all cores blow 553 mm, also
    if cooling ducts are used.
    In case of cooling ducts use formula for banded
    core, but add 3 mm to the diameter when calculating the area. '''
import math
def COR130(ZLIMB, DCORE, NPHAS, FREQ, BLIMB, UMAXPU,HLIMB, PLIMB,
           STKFAC,NCOOLI, SPFADJ):

    PI     = 3.14159
    SQR2   = 1.41421
    RAAFEC = 7650.

    ''' START  OF COPY FROM THE OLD ROUTINE CORE1 FROM R31009 '''

    GCORN  = ZLIMB*(5193.96+DCORE*(-62085.41+DCORE*
                                   (288812.02+DCORE*(-642959.03+DCORE*(713974.2-DCORE*304515.75)))))
    GDLIMB = 25.

    if (NPHAS == 1):
        GDYOKE = -0.500*GCORN
    else:
        GDYOKE = -0.667*GCORN

    HYOKE  = 0.94*DCORE+0.025
    YOKAMP = 1.18785-DCORE*(0.403-0.271*DCORE)
    FCONST = 0.735+FREQ*5.3E-3

    ''' "FREQ" = 50 HZ ==> FCONST = 1.0
        "FREQ" = 60 HZ ==> FCONST = 1.053 '''

    ''' Number of cooling ducts '''
    
    BLIM2=BLIMB*UMAXPU
    BLIM   = (2.569-1.514*DCORE)/FCONST
    NCOOLW = 0

    if(BLIM2 > BLIM):
        BLIM   = (2.742-1.514*DCORE)/FCONST
        NCOOLW = 1

        if(BLIM2 > BLIM):
            BLIM   = (2.560-1.001*DCORE)/FCONST
            NCOOLW = 2

            if(BLIM2 > BLIM):
                NCOOLW =3


    if (NCOOLI < 0):
        NCOOLC = NCOOLW
    else:
        NCOOLC = NCOOLI

    ''' Next part rewritten, revision 93-01-26 '''

    ''' Rev 93-05-08  if(DCORE < 0.554) THEN '''
    
    if(round(DCORE*1000.) < 554):
        ''' GLUED CORE '''
        BBGLCO = True
        CORBND = 'GLUED   '
        KBAND  = 0
    else:
        ''' BANDAGED CORE '''
        BBGLCO=False
        CORBND='STEEL   '
        KBAND = 2

    Z=float(NCOOLC)

    if(NCOOLC == 0  and BBGLCO):

        ''' Glued core without cooling ducts '''

        if(STKFAC < 0.1):
            FILLF  = 0.01042*DCORE+0.8677-0.011*math.exp(-8.03*(DCORE-0.22))
        else:
            FILLF  = STKFAC

        ''' Use nominal diameter for calculation of core area '''

        DC = DCORE

    else:

        ''' All cores with cooling ducts '''

        if(STKFAC < 0.1):
            FILLF = (0.09833*DCORE+0.8114-0.0068*(Z-2.)*(Z-3.)*Z/2.+
                     0.0175*(Z-1.)*(Z-3.)*Z/2.-0.0259*(Z-1.)*(Z-2.)*Z/6.)
        else:
            FILLF = STKFAC

	  
        FILLF=FILLF/0.95*SPFADJ

        ''' Use nominal diameter + 3 mm for calculation of core area
            for glued cores
            Use nominal diameter for bandaged cores. '''

        if(BBGLCO):
            DC = DCORE + 0.003
        else:
            DC = DCORE

    ACORE = PI*DC*DC/4.*FILLF

    ''' End of Revision 93-01-26 '''

    GSPYOC=367.

    ''' END OF COPY FROM THE OLD ROUTINE  CORE1 FROM R31009 '''

    ''' FROM ROUTINE CORCAL IN R31009: '''

    U0     = ACORE*2.*PI*FREQ/SQR2
    GSPLIM = ACORE*RAAFEC
    AYOKE  = YOKAMP*ACORE
    GSPYOK = 2.*AYOKE*RAAFEC*(ZLIMB-1.)

    ''' FROM ROUTINE ACTPAR IN R31009: '''

    GLIMBM = ZLIMB*(GSPLIM*HLIMB+GDLIMB)
    GYOKE  = GSPYOK*PLIMB+GDYOKE
    GCORLA = GLIMBM+GYOKE+GCORN

    ''' NEW   : '''

    RLYOKE = (ZLIMB-1.)*PLIMB + DCORE
    ANDEL  = 0.
    BDRAG  = 0.
    TDRAG  = 0.
    RDRAG  = 0.
    GLIMBY = 0.
    TASEC  = 0.
    TCORE  = 0.

    return(ACORE,ANDEL,BDRAG,GCORN,GLIMBM,GLIMBY,GYOKE,HYOKE,NCOOLC,
           RDRAG,RLYOKE,TASEC,TCORE,TDRAG,U0,YOKAMP,CORBND,KBAND,
            NCOOLW)
