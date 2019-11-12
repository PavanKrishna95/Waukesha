
''' Title:  Calculate number of cooling ducts in TAD and TAA cores. '''

def CDTAD(DK,TOPOIL,B,FREKV,BBZDKH,BBSTLA,BBPLJT):

    ''' DK      Corediameter  (MM)
        TOPOIL  Top oil temperature
        B       max flux density (T)
        FREKV   frequency  (HZ)
        BBZDKH  ZDKH core plate (.T.  OR .N.)
        BBPLJT  PLJT core plate (.T.  OR .N.)
        BBSTLA  step-lap core   (.T.  OR .N.) '''

  
    ''' Top oil paramter PDK.
        A new fictive diameter is calculated which is less than the original one, but with 90 degrees top oil.
        (which will give the same number of cooling ducts) '''

    E=0.1*(TOPOIL-50.)
    P1000=(2.**E-1.)*25.+625.
    PDK = (DK*(P1000*0.01-1.)+1000.-P1000)/9.

    ''' ZDKH or PLJT core plate quality '''

    if(BBZDKH or BBPLJT):

        ''' 50 HZ '''

        if(FREKV < 55.):

            ''' STEP-LAP, 50 Hz, ZDKH '''

            if(BBSTLA):
                NC=0
                if(B > F(425.,605.,PDK)):   NC=1
                if(B > F(610.,855.,PDK)):   NC=2
                if(B > F(790.,1150.,PDK)):  NC=3
            else:

                ''' NO STEPLAP, 50 Hz, ZDKH '''

                NC=0
                if(B > F(410.,585.,PDK)):   NC=1
                if(B > F(585.,825.,PDK)):   NC=2
                if(B > F(755.,1110.,PDK)):  NC=3
    

        else:

            ''' STEP-LAP, 60 Hz,  ZDKH '''

            if (BBSTLA):
                NC=0
                if(B > F(475.,525.,PDK)):   NC=1
                if(B > F(640.,720.,PDK)):   NC=2
                if(B > F(785.,965.,PDK)):   NC=3

            else:

                ''' NO STEPLAP, 60 HZ, ZDKH '''

                NC=0
                if(B > F(460.,510.,PDK)):   NC=1
                if(B > F(620.,695.,PDK)):   NC=2
                if(B > F(765.,930.,PDK)):   NC=3

                ''' M5  core plate quality '''

    else:

        ''' 50 HZ '''

        if(FREKV < 55.):

            ''' STEP-LAP, 50 Hz, M5 '''

            if (BBSTLA):
                NC=0
                if(B > F(340.,510.,PDK)):   NC=1
                if(B > F(500.,725.,PDK)):   NC=2
                if(B > F(625.,955.,PDK)):   NC=3
            else:

                ''' NO STEPLAP, 50 Hz, M5 '''

                NC=0
                if(B > F(320.,475.,PDK)):   NC=1
                if(B > F(475.,700.,PDK)):   NC=2
                if(B > F(575.,920.,PDK)):   NC=3

        else:

            ''' 60 HZ '''

            ''' STEP-LAP, 60 Hz,  M5 '''

            if (BBSTLA):
                NC=0
                if(B > F(300.,445.,PDK)):   NC=1
                if(B > F(445.,620.,PDK)):   NC=2
                if(B > F(540.,815.,PDK)):   NC=3

            else:

                ''' NO STEPLAP, 60 HZ, M5 '''

                NC=0
                if(B > F(280.,425.,PDK)):   NC=1
                if(B > F(425.,600.,PDK)):   NC=2
                if(B > F(510.,785.,PDK)):   NC=3

    CDTAD=NC

    return CDTAD

def F(X1,X2,PDK):

    ''' Evaluation of straight line between B = 1,5 T  and B = 1,95 T
        end point values are X1, AND X2. '''

    return 1.95 - 0.45*(PDK-X1)/(X2-X1)

    
