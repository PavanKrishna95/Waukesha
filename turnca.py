
''' Title: Calculate the relative turn-numbers (NTAL) for
           each winding. Winding 1 turn-number gives the
           primary limb-voltage. '''

from relnta import RELNTA
def TURNCA():
    import com as C
    ''' Start values (C.NLOOP,C.NLOOPG,C.ZERPOS,C.PLSPOS,C.RMIPOS,C.ZTALWG) '''

    ''' Start of the start values block. '''

    ''' Set C.EXTPOS = 0 for each terminal. '''
    ''' For ITML= 1 to 3 '''
    
    C.EXTPOS=[0. for i in range(3)]
    
    ''' Set tap positions,etc = 0 for each terminal '''
    ''' For ITML = 1 to 4'''
    
    C.NLOOPG=[1 for i in range(4)]
    C.ZERPOS=[0. for i in range(4)]
    C.PLSPOS=[0. for i in range(4)]
    C.RMIPOS=[0. for i in range(4)]

    ''' Set turns = 0 for each tap '''
    ''' For KTAP =1 to 3 ITML =1 to 4'''

    C.ZTALWG=[[0. for i in range(4)] for j in range(3)]

    ''' Set loops = 1 for each winding '''
    ''' For IWDG = 1 to C.NWILI '''

    for i in range(1,C.NWILI+1):
        C.NLOOP[i-1]=1

    ''' End of the start values block. '''

    ''' Select FULL or AUTO transformer '''
    
    ''' FULL trfr '''

    if ( not C.BBAUTO) :

        ''' VFR type voltage regulation '''

        if (C.BBVFR) :
            C.NPSTEP[0]=C.NMSTEP[1]
            X1=float(C.NMSTEP[1])
            C.NMSTEP[0]=C.NPSTEP[1]
            X2=float(C.NPSTEP[1])
            C.PUSTEP[0]=1./(X2-X1+1./C.PUSTEP[1])
            C.KTYPRW[0]=C.KTYPRW[1]
            C.ZTALWG[0][1]=1.
            ITML=1

            ''' Calculate relative turns '''
            C.NLOOPG,C.PLSPOS,C.RMIPOS,C.ZERPOS,C.ZTALWG,C.EXTPOS =RELNTA(ITML,C.KTYPRW,C.NLOOPG,
                    C.NMSTEP,C.NPSTEP,C.NXSTEP,
                    C.PLSPOS,C.PUSTEP,C.RMIPOS,
                    C.ZERPOS,C.ZTALWG,C.EXTPOS)
            X1=(1.-X2*X1*C.PUSTEP[1]*C.PUSTEP[0])*C.UDIM[1]/C.UDIM[0]

            ''' CFR '''

        else:

            ''' For terminals 1 & 2 '''

            for ITML in range(1,3):

                ITML1=ITML
                ''' Calculate relative turns '''

                if (C.BBVR[ITML-1]):
                    C.NLOOPG,C.PLSPOS,C.RMIPOS,C.ZERPOS,C.ZTALWG,C.EXTPOS =RELNTA(ITML1,C.KTYPRW,C.NLOOPG,
                                 C.NMSTEP,C.NPSTEP,C.NXSTEP,
                                 C.PLSPOS,C.PUSTEP,C.RMIPOS,
                                 C.ZERPOS,C.ZTALWG,C.EXTPOS)

                if (not C.BBVR[ITML-1]): C.ZTALWG[0][ITML-1]=1.
            X1=C.UDIM[1]/C.UDIM[0]


        ''' For tap postions 1 to 3 '''
    
        for ITAP in range(1,4):
            C.ZTALWG[ITAP-1][1]=X1*C.ZTALWG[ITAP-1][1]

        ''' PART 2, Auto-connected transformers '''

    else:

        ''' Auto-connected transformers '''

        ''' Voltage regulation type CFR '''

        if (not C.BBVFR) :

            ''' Auto-connected transformers, voltage regulation type CFR '''
            ''' For terminals 1 & 2 '''
            
            for ITML in range(1,3):

                ITML1=ITML
                ''' Calculate relative turns '''

                if (C.BBVR[ITML-1]):
                    C.NLOOPG,C.PLSPOS,C.RMIPOS,C.ZERPOS,C.ZTALWG,C.EXTPOS =RELNTA(ITML1,C.KTYPRW,C.NLOOPG,
                                 C.NMSTEP,C.NPSTEP,C.NXSTEP,
                                 C.PLSPOS,C.PUSTEP,C.RMIPOS,
                                 C.ZERPOS,C.ZTALWG,C.EXTPOS)

                if (not C.BBVR[ITML-1]): C.ZTALWG[0][ITML-1]=1.
            X1=C.UDIM[1]/C.UDIM[0]

            ''' For tap postions 1 to 3 '''
    
            for ITAP in range(1,4):
                C.ZTALWG[ITAP-1][1]=X1*C.ZTALWG[ITAP-1][1]

            if (C.BBUPTR): C.ZTALWG[0][1]-=C.ZTALWG[0][0]
            if (not C.BBUPTR): C.ZTALWG[0][0]-=C.ZTALWG[0][1]

            ''' Voltage regulation type VFR '''

        else:

            ''' Calculate as required '''

            ''' For step-up transformer '''

            if (C.BBUPTR) :
                X1=C.UDIM[0]/C.UDIM[1]
                X3=1./(1.+float(C.NPSTEP[1]-C.NMSTEP[1])*C.PUSTEP[1]-X1)
                C.ZTALWG[0][1]=X3*(1.-float(C.NMSTEP[1])*C.PUSTEP[1]-X1)*((1.+float(C.NPSTEP[1])*C.PUSTEP[1])/X1-1.)
                C.NPSTEP[0]=C.NMSTEP[1]
                X2=float(C.NMSTEP[1])
                C.NMSTEP[0]=C.NPSTEP[1]
                X1=float(C.NPSTEP[1])
                C.PUSTEP[0]=C.PUSTEP[1]*X3
                C.KTYPRW[0]=C.KTYPRW[1]
                ITML2=1

                ''' Calculate relative turns '''

                C.NLOOPG,C.PLSPOS,C.RMIPOS,C.ZERPOS,C.ZTALWG,C.EXTPOS =RELNTA(ITML2,C.KTYPRW,C.NLOOPG,
                            C.NMSTEP,C.NPSTEP,C.NXSTEP,
                            C.PLSPOS,C.PUSTEP,C.RMIPOS,
                            C.ZERPOS,C.ZTALWG,C.EXTPOS)
                
                ''' For NON step-up transformer '''
                
            else:
                X=C.UDIM[1]/C.UDIM[0]
                X1=float(C.NPSTEP[1])*C.PUSTEP[1]
                X2=float(C.NMSTEP[1])*C.PUSTEP[1]
                X3=1./(1.+(X1*X2+X2-X1-1.)*X)
                C.PUSTEP[1]=C.PUSTEP[1]*X3
                ITML3=2

                ''' Calculate relative turns '''

                C.NLOOPG,C.PLSPOS,C.RMIPOS,C.ZERPOS,C.ZTALWG,C.EXTPOS =RELNTA(ITML3,C.KTYPRW,C.NLOOPG,
                            C.NMSTEP,C.NPSTEP,C.NXSTEP,
                            C.PLSPOS,C.PUSTEP,C.RMIPOS,
                            C.ZERPOS,C.ZTALWG,C.EXTPOS)
                C.PUSTEP[1]=C.PUSTEP[1]/X3
                X=1./(1./X-X1*X2*X3)

                ''' For tap postions 1 to 3 '''

                for KTAP in range(1,4):
                    C.ZTALWG[KTAP-1][1]=X1*C.ZTALWG[KTAP-1][1]
                if (C.ZERPOS[1]>1.5): X1=C.ZERPOS[1]-2.
                if (C.ZERPOS[1]>1.5): X2=1.
                if (C.ZERPOS[1]<=1.5): X1=C.ZERPOS[1]
                if (C.ZERPOS[1]<=1.5): X2=0.
                C.ZTALWG[0][0]=1.-C.ZTALWG[0][1]-C.ZTALWG[1][1]*X1-C.ZTALWG[2][1]*X2


    ''' NTAL for tertiary and extra windings '''
    ''' If more than 2 terminals '''

    if (C.NG>=3) :

        ''' For terminals 3 and 4 '''

        for ITML in range(3,C.NG+1):
            ITML11=ITML

            ''' Calculate relative turns '''

            if (C.BBVR[ITML-1]):
                C.NLOOPG,C.PLSPOS,C.RMIPOS,C.ZERPOS,C.ZTALWG,C.EXTPOS =RELNTA(ITML11,C.KTYPRW,C.NLOOPG,
                       C.NMSTEP,C.NPSTEP,C.NXSTEP,
                       C.PLSPOS,C.PUSTEP,C.RMIPOS,
                       C.ZERPOS,C.ZTALWG,C.EXTPOS)
            if (not C.BBVR[ITML-1]): C.ZTALWG[0][ITML-1]=1.
            X1=C.UDIM[ITML-1]/C.UDIM[0]

            ''' For tap postions 1 to 3 '''

            for KTAP in range(1,4):
                C.ZTALWG[KTAP-1][ITML-1]=X1*C.ZTALWG[KTAP-1][ITML-1]

    ''' Transfer NTAL for each group
        to a sequential order from the core
        as they appear in the transformer '''

    for IWDG in range(1,C.NWILI+1):
        JTML=C.KGROUP[IWDG-1]
        C.ZTALMW[IWDG-1]=0.
        C.ZTALRW[IWDG-1]=0.
        C.NLOOP[IWDG-1]=1

        ''' Set tap postion variables '''

        ''' If C.KCODE[IWDG] = 1 '''
        
        if (C.KCODE[IWDG-1] == 1) :
            print('C.KODE==1')
            C.FRZPOS[IWDG-1]=1.
            C.FRPPOS[IWDG-1]=1.
            C.FRMPOS[IWDG-1]=1.
            C.FRXPOS[IWDG-1]=1.
            C.ZTALMW[IWDG-1]=C.ZTALWG[0][JTML-1]
            print(C.ZTALWG[0])

            ''' If C.KCODE[IWDG-1] != 1 '''

        else:

            ''' Set C.ZTALRW '''

            ''' If C.KCODE[IWDG-1] != 2 and != 4 '''

            if (C.KCODE[IWDG-1]!=2 and C.KCODE[IWDG-1] != 4) :
                C.ZTALRW[IWDG-1]=C.ZTALWG[2][JTML-1]

                ''' If C.KCODE[IWDG] = 2 or 4 '''

            else:
                C.ZTALRW[IWDG-1]=C.ZTALWG[1][JTML-1]
                C.NLOOP[IWDG-1]=C.NLOOPG[JTML-1]

            ''' Set tap position variables '''

            ''' If C.KTYPRW[JTML-1] = 3 '''

            if(C.KTYPRW[JTML-1]==3) :

                ''' Set tap position variables '''

                ''' If C.KCODE[IWDG-1] = 2 '''

                if (C.KCODE[IWDG-1]==2) :
                    C.FRMPOS[IWDG-1]=C.RMIPOS[JTML-1]
                    C.FRZPOS[IWDG-1]=C.ZERPOS[JTML-1]
                    if (C.ZERPOS[JTML-1]>1.5): C.FRZPOS[IWDG-1]=C.ZERPOS[JTML-1]-2.
                    C.FRPPOS[IWDG-1]=C.PLSPOS[JTML-1]-2.
                    C.FRXPOS[IWDG-1]=C.EXTPOS[JTML-1]
                    if (C.EXTPOS[JTML-1]>1.5): C.FRXPOS[IWDG-1]=C.EXTPOS[JTML-1]-2.

                    ''' If C.KCODE[IWDG-1] != 2 '''

                else:
                    C.FRMPOS[IWDG-1]=0.
                    C.FRZPOS[IWDG-1]=0.
                    if (C.ZERPOS[JTML-1]>1.5): C.FRZPOS[IWDG-1]=1.
                    C.FRPPOS[IWDG-1]=1.
                    C.FRXPOS[IWDG-1]=0.
                    if (C.EXTPOS[JTML-1]>1.5): C.FRXPOS[IWDG-1]=1.

                    ''' If C.KTYPRW[JTML-1] != 3 '''

            else:
                C.FRZPOS[IWDG-1]=C.ZERPOS[JTML-1]
                C.FRPPOS[IWDG-1]=C.PLSPOS[JTML-1]
                C.FRMPOS[IWDG-1]=C.RMIPOS[JTML-1]
                C.FRXPOS[IWDG-1]=C.EXTPOS[JTML-1]

            if(C.KCODE[IWDG-1]==4): C.ZTALMW[IWDG-1]=C.ZTALWG[0][JTML-1]

        ''' Set tap position variables '''

        ''' If VFR and terminal 1 '''

        if (C.BBVFR and JTML == 1) :
            X1=C.FRPPOS[IWDG-1]
            C.FRPPOS[IWDG-1]=C.FRMPOS[IWDG-1]
            C.FRMPOS[IWDG-1]=X1
 
    ''' For each winding '''

    for IWDG in range(1,C.NWILI+1):
        C.POSIT[IWDG-1][0]=C.FRZPOS[IWDG-1]
        C.POSIT[IWDG-1][1]=C.FRPPOS[IWDG-1]
        C.POSIT[IWDG-1][2]=C.FRMPOS[IWDG-1]
        C.POSIT[IWDG-1][3]=C.FRXPOS[IWDG-1]
    
    return
