
''' Title:  Calculate number of cooling ducts in TAB cores. '''

def CDTBA(DK,TOPOIL,B,FREKV,BBZDKH,BBSTLA,BBPLJT):

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
                if(B > F(495.,725.,PDK)):   NC=1
                if(B > F(655.,935.,PDK)):   NC=2
                if(B > F(815.,1165.,PDK)):  NC=3
                if(B > F(980.,1415.,PDK)):  NC=4
            else:

                ''' NO STEPLAP, 50 Hz, ZDKH '''

                NC=0
                if(B > F(475.,700.,PDK)):   NC=1
                if(B > F(625.,905.,PDK)):   NC=2
                if(B > F(785.,1135.,PDK)):  NC=3
                if(B > F(940.,1380.,PDK)):  NC=4
    
        else:

            ''' STEP-LAP, 60 Hz,  ZDKH '''

            if (BBSTLA):
                NC=0
                if(B > F(430.,635.,PDK)):   NC=1
                if(B > F(570.,820.,PDK)):   NC=2
                if(B > F(705.,1015.,PDK)):  NC=3
                if(B > F(840.,1235.,PDK)):  NC=4
                if(B > F(955.,1445.,PDK)):  NC=5

            else:

                ''' NO STEPLAP, 60 HZ, ZDKH '''

                NC=0
                if(B > F(410.,610.,PDK)):   NC=1
                if(B > F(540.,795.,PDK)):   NC=2
                if(B > F(675.,985.,PDK)):   NC=3
                if(B > F(805.,1190.,PDK)):  NC=4
                if(B > F(915.,1400.,PDK)):  NC=5

                ''' M5  core plate quality '''

    else:

        ''' 50 HZ '''

        if(FREKV < 55.):

            ''' STEP-LAP, 50 Hz, M5 '''

            if (BBSTLA):
                NC=0
                if(B > F(375.,600.,PDK)):   NC=1
                if(B > F(510.,790.,PDK)):   NC=2
                if(B > F(630.,980.,PDK)):   NC=3
                if(B > F(750.,1190.,PDK)):  NC=4
                if(B > F(845.,1385.,PDK)):  NC=5
            else:

                ''' NO STEPLAP, 50 Hz, M5 '''

                NC=0
                if(B > F(350.,580.,PDK)):   NC=1
                if(B > F(475.,760.,PDK)):   NC=2
                if(B > F(585.,950.,PDK)):   NC=3
                if(B > F(700.,1150.,PDK)):  NC=4
                if(B > F(785.,1335.,PDK)):  NC=5

        else:

            ''' 60 HZ '''

            ''' STEP-LAP, 60 Hz,  M5 '''

            if (BBSTLA):
                NC=0
                if(B > F(315.,525.,PDK)):   NC=1
                if(B > F(430.,690.,PDK)):   NC=2
                if(B > F(540.,860.,PDK)):   NC=3
                if(B > F(630.,1030.,PDK)):  NC=4
                if(B > F(695.,1200.,PDK)):  NC=5

            else:

                ''' NO STEPLAP, 60 HZ, M5 '''

                NC=0
                if(B > F(295.,505.,PDK)):   NC=1
                if(B > F(410.,665.,PDK)):   NC=2
                if(B > F(510.,825.,PDK)):   NC=3
                if(B > F(595.,995.,PDK)):   NC=4
                if(B > F(655.,1150.,PDK)):  NC=5

    CDTBA=NC

    return CDTBA

def F(X1,X2,PDK):

    ''' Evaluation of straight line between B = 1,5 T  and B = 1,95 T
        end point values are X1, AND X2. '''

    return 1.95 - 0.45*(PDK-X1)/(X2-X1)

    
