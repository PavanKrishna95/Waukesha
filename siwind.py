''' Title:  Convert winding indata to SI-units and
            transfer them to internal variables.
            Relevant indata checks are performed.
            The following variables are assigned values :

            C.KWITYP,C.BBRR,C.BBRW,C.SIGM,C.RAACON. 

          Reduction of max current density based on rated power=
          self cooled power  (C.FONAN > 1.)

          Check for BOOSTER turns ratio transferred to C.FABOOS[IWDG]
          Logical C.BBOOSW is specified for each winding.
          Variable C.SIGMA-Cu depending on temperature is included. '''

from fprint import FPRINT
def SIWIND():
    import com as C
    NCOL=['A','B','C','D','E','F','G','H','I']

    ''' Calculation of reduction factor for current density if
        C.FONAN > 1 (rated power = self cooled power) '''

    UPGRED = 1.
    C.FONAN  = C.AARR[153]
    if (C.FONAN >  3.):C.FONAN = C.FONAN/100.
    if (C.FONAN >  1.):UPGRED= 1./C.FONAN

    ''' For each winding '''
    
    for IWDG in range(1,C.NWILI+1):
        C.KGROUP[IWDG-1]=C.IARR[20+IWDG-1]

        ''' Illegal reference to terminal '''

        if (C.KGROUP[IWDG-1] <=  0 or C.KGROUP[IWDG-1] >  C.NG):
            C.JFC,C.BBERR=FPRINT(2,C.BBERR,
                        'SIWIND: Winding '//NCOL[IWDG-1]//' has an invalid terminal node')

        ''' Determine the winding type. '''

        C.KWITYP[IWDG-1]=0
        if (C.TARR[30+IWDG-1] == 'S'
            or C.TARR[30+IWDG-1] == 'S1'
            or C.TARR[30+IWDG-1] == 'S2'
            or C.TARR[30+IWDG-1] == 'S3'
            or C.TARR[30+IWDG-1] == 'S4'
            or C.TARR[30+IWDG-1] == 'S5'
            or C.TARR[30+IWDG-1] == 'S6'
            or C.TARR[30+IWDG-1] == 'S7'
            or C.TARR[30+IWDG-1] == 'S8'
            or C.TARR[30+IWDG-1] == 'S9'
            or C.TARR[30+IWDG-1] == 'S10'
            or C.TARR[30+IWDG-1] == 'S11'
            or C.TARR[30+IWDG-1] == 'S12'):C.KWITYP[IWDG-1]=1

        if (C.TARR[30+IWDG-1] == 'L'
            or C.TARR[30+IWDG-1] == 'L1'
            or C.TARR[30+IWDG-1] == 'L2'
            or C.TARR[30+IWDG-1] == 'L3'):C.KWITYP[IWDG-1]=2

        if (C.TARR[30+IWDG-1] == 'CD'):C.KWITYP[IWDG-1]=3

        if (C.TARR[30+IWDG-1] == 'SD'):C.KWITYP[IWDG-1]=4

        if (C.TARR[30+IWDG-1] == 'D2'):C.KWITYP[IWDG-1]=5

        if (C.TARR[30+IWDG-1] == 'SLS'
            or C.TARR[30+IWDG-1] == 'SLS1'
            or C.TARR[30+IWDG-1] == 'SLS2'
            or C.TARR[30+IWDG-1] == 'SLS3'
            or C.TARR[30+IWDG-1] == 'SLS4'
            or C.TARR[30+IWDG-1] == 'SLS5'
            or C.TARR[30+IWDG-1] == 'SLS6'):C.KWITYP[IWDG-1]=6

        if (C.TARR[30+IWDG-1] == 'SLL'
            or C.TARR[30+IWDG-1] == 'SLL1'
            or C.TARR[30+IWDG-1] == 'SLL2'):C.KWITYP[IWDG-1]=7

        ''' Winding type illegally stated '''

        if (C.KWITYP[IWDG-1] == 0):
            C.JFC,C.BBERR=FPRINT(2,C.BBERR,
                        'SIWIND: Winding '+NCOL[IWDG-1]+' has an invalid winding type')

        ''' Determine the number of strands in radial direction '''

        C.ZRR[IWDG-1]=1
        C.ZPART[IWDG-1]=0
        if (C.TARR[30+IWDG-1] == 'S'
            or C.TARR[30+IWDG-1] == 'S1'):C.ZPART[IWDG-1]=1
        if (C.TARR[30+IWDG-1] == 'S2'): C.ZPART[IWDG-1]=2
        if (C.TARR[30+IWDG-1] == 'S3'): C.ZPART[IWDG-1]=3
        if (C.TARR[30+IWDG-1] == 'S4'): C.ZPART[IWDG-1]=4
        if (C.TARR[30+IWDG-1] == 'S5'): C.ZPART[IWDG-1]=5
        if (C.TARR[30+IWDG-1] == 'S6'): C.ZPART[IWDG-1]=6
        if (C.TARR[30+IWDG-1] == 'S7'): C.ZPART[IWDG-1]=7
        if (C.TARR[30+IWDG-1] == 'S8'): C.ZPART[IWDG-1]=8
        if (C.TARR[30+IWDG-1] == 'S9'): C.ZPART[IWDG-1]=9
        if (C.TARR[30+IWDG-1] == 'S10'): C.ZPART[IWDG-1]=10
        if (C.TARR[30+IWDG-1] == 'S11'): C.ZPART[IWDG-1]=11
        if (C.TARR[30+IWDG-1] == 'S12'): C.ZPART[IWDG-1]=12

        if (C.TARR[30+IWDG-1] == 'L'
            or C.TARR[30+IWDG-1] == 'L1'): C.ZPART[IWDG-1]=1
        if (C.TARR[30+IWDG-1] == 'L2'): C.ZPART[IWDG-1]=2
        if (C.TARR[30+IWDG-1] == 'L3'): C.ZPART[IWDG-1]=3

        if (C.TARR[30+IWDG-1] == 'CD'): C.ZPART[IWDG-1]=1

        if (C.TARR[30+IWDG-1] == 'SD'): C.ZPART[IWDG-1]=1

        if (C.TARR[30+IWDG-1] == 'D2'): C.ZPART[IWDG-1]=1

        if (C.TARR[30+IWDG-1] == 'SLS'
            or C.TARR[30+IWDG-1] == 'SLS1'): C.ZPART[IWDG-1]=1
        if (C.TARR[30+IWDG-1] == 'SLS2'): C.ZPART[IWDG-1]=2
        if (C.TARR[30+IWDG-1] == 'SLS3'): C.ZPART[IWDG-1]=3
        if (C.TARR[30+IWDG-1] == 'SLS4'): C.ZPART[IWDG-1]=4
        if (C.TARR[30+IWDG-1] == 'SLS5'): C.ZPART[IWDG-1]=5
        if (C.TARR[30+IWDG-1] == 'SLS6'): C.ZPART[IWDG-1]=6

        if (C.TARR[30+IWDG-1] == 'SLL'
            or C.TARR[30+IWDG-1] == 'SLL1'):C.ZPART[IWDG-1]=1
        if (C.TARR[30+IWDG-1] == 'SLL2'):C.ZPART[IWDG-1]=2

        ''' Number of strands in the redial direction not given '''

        if (C.ZPART[IWDG-1] == 0):
            C.JFC,C.BBERR=FPRINT(2,C.BBERR,
                'SIWIND: Number of radial strands not given'+' for winding '+NCOL[IWDG-1])

        C.IPISOL[IWDG-1]=0
        if (C.TARR[60+IWDG-1] == 'SP'): C.IPISOL[IWDG-1]=1
        if (C.TARR[60+IWDG-1] == 'OR'): C.IPISOL[IWDG-1]=2
        if (C.TARR[60+IWDG-1] == 'LR'): C.IPISOL[IWDG-1]=3
        if (C.TARR[60+IWDG-1] == 'TC'): C.IPISOL[IWDG-1]=1

        ''' Cable type illegally stated '''

        if (C.IPISOL[IWDG-1] == 0):
            C.JFC,C.BBERR=FPRINT(2,C.BBERR,
                        'SIWIND: Winding '+NCOL[IWDG-1]+' has an invalid cable type')

        ''' Function code (1=Main,2=Reg.,3=Coarse step reg w , 4=Tapped main) '''

        C.KCODE[IWDG-1]=C.IARR[30+IWDG-1]

        ''' Illegal function code '''

        if (C.KCODE[IWDG-1] <=  0 or C.KCODE[IWDG-1] >  4):
            C.JFC,C.BBERR=FPRINT(2,C.BBERR,
                        'SIWIND: Winding '+NCOL[IWDG-1]+' has an invalid function code')

        C.BBRW[IWDG-1]=False
        if (C.KCODE[IWDG-1] == 2 or C.KCODE[IWDG-1] == 3):
            C.BBRW[IWDG-1]=True

        C.FRACT[IWDG-1]=C.AARR[40+IWDG-1]
        C.NGROUP[IWDG-1]=C.IARR[40+IWDG-1]
        C.CURDM[IWDG-1]=4.5E+6 * UPGRED
        if (C.AARR[50+IWDG-1] <  0.):
            C.CURDM[IWDG-1]=1.E+6*abs(C.AARR[50+IWDG-1]) * UPGRED

        ''' ACOND is calculated in 'PREP1'  after 'VOLTAGE' '''

        ''' Start of calculation block '''

        C.BDUCT[IWDG-1]=C.AARR[70+IWDG-1]/1.E+3
        C.FILLF[IWDG-1]=C.AARR[80+IWDG-1]
        if (C.AARR[90+IWDG-1] >  0.):C.BBRR[IWDG-1]=True

        ''' End of calculation block '''

        ''' Space factor not given '''

        if (C.AARR[80+IWDG-1] <  1.E-6 and C.AARR[90+IWDG-1] <  1.E-6):
            C.JFC,C.BBERR=FPRINT(2,C.BBERR,
                        'SIWIND: Winding '+NCOL[IWDG-1]+' has no space factor given')

        C.RRWDG[IWDG-1]=C.AARR[90+IWDG-1]/1.E+3
        C.DYOKE[IWDG-1]=C.AARR[100+IWDG-1]/1.E+3
        C.BPART[IWDG-1]=C.AARR[110+IWDG-1]/1.E+3
        C.EXTRAR[IWDG-1]=C.DARR[40+IWDG-1]/1.E+3
        C.HCLAC[IWDG-1]=C.DARR[50+IWDG-1]/1.E+3

        ''' Conductor material parameters '''

        ''' Aluminium conductors '''

        if (C.TARR[40+IWDG-1][0] == 'A'):
            C.SIGM[IWDG-1]=C.SIGMAL * (235. + 75.) / (235. + C.TELOSS)
            C.RAACON[IWDG-1]=C.RAAAL
            ''' Copper conductors '''

        elif (C.TARR[40+IWDG-1][0] == 'C'):
            C.SIGM[IWDG-1]=C.SIGMCU * (235. + 75.) / (235. + C.TELOSS)
            C.RAACON[IWDG-1]=C.RAACU
            ''' Conductor material not recognised '''

        else:
            pass
            C.JFC,C.BBERR=FPRINT(2,C.BBERR,
                        'SIWIND: Winding '+NCOL[IWDG]+' conductor material is invalid')

        ''' Auxiliary constant for calculation of additional losses '''
        print(C.SIGM)
        C.TENSM[IWDG-1]=1.E+6*C.AARR[120+IWDG-1]
        C.PRESSM[IWDG-1]=-1.E+6*C.AARR[130+IWDG-1]

        ''' Default values for conductor height and paper covering '''

        ''' Winding type 1 '''

        if (C.KWITYP[IWDG-1] == 1):
            C.HPART[IWDG-1]=0.0075
            C.TSPIN[IWDG-1]=0.0005

            ''' Winding type 2 '''

        elif (C.KWITYP[IWDG-1] == 2):
            C.HPART[IWDG-1]=0.0075
            C.TSPIN[IWDG-1]=0.001

            ''' Winding type 3 or 5 '''

        elif ((C.KWITYP[IWDG-1] == 3) or (C.KWITYP[IWDG-1] == 5)):
            C.HPART[IWDG-1]=0.011
            C.TSPIN[IWDG-1]=max((C.USURG[C.KGROUP[IWDG-1]-1]/1000.)**0.7/60000.,0.0005)

            ''' Winding type 4 '''

        elif (C.KWITYP[IWDG-1] == 4):
            C.HPART[IWDG-1]=0.011
            C.TSPIN[IWDG-1]=max((C.USURG[C.KGROUP[IWDG-1]-1]/1000.)**0.7/90000.,0.0005)

            ''' Winding type 6 '''

        elif (C.KWITYP[IWDG-1] == 6):
            C.HPART[IWDG-1]=0.015
            C.TSPIN[IWDG-1]=0.0018

            ''' Winding type 7 '''

        elif (C.KWITYP[IWDG-1] == 7):
            C.HPART[IWDG-1]=0.015
            C.TSPIN[IWDG-1]=0.004

        if (C.BARR[10+IWDG-1] >  0.1):
            C.HPART[IWDG-1]=C.BARR[10+IWDG-1]/1.E+3
        C.BARR[10+IWDG-1]=1.E+3*C.HPART[IWDG-1]

        if (C.BARR[20+IWDG-1] >=  0.):
            C.TSPIN[IWDG-1]=C.BARR[20+IWDG-1]/1.E+3

        if(C.IPISOL[IWDG-1] == 2):
            PSPIN=0.15E-3

        elif(C.IPISOL[IWDG-1] == 3):
            PSPIN=0.18E-3

        else:PSPIN=0.5E-3

        C.TCOV1[IWDG-1]=PSPIN
        if (C.DARR[30+IWDG-1] >=  0.):C.TCOV1[IWDG-1]=C.DARR[30+IWDG-1]/1.E+3

        if(C.IPISOL[IWDG-1] == 2 or C.IPISOL[IWDG-1] == 3):C.TCOV1[IWDG-1]=PSPIN

        C.TCOV2[IWDG-1]=C.TSPIN[IWDG-1]-C.TCOV1[IWDG-1]
        if(C.IPISOL[IWDG-1] == 2 or C.IPISOL[IWDG-1] == 3):
            C.TCOV2[IWDG-1]=C.TSPIN[IWDG-1]

        ''' Make covering non-negative '''

        if(C.TCOV1[IWDG-1] <  0.): C.TCOV1[IWDG-1]=0.
        if(C.TCOV2[IWDG-1] <  0.): C.TCOV2[IWDG-1]=0.

        ''' Booster check '''
        if(C.WDGFUN[IWDG-1]  == 'RB'  or C.WDGFUN[IWDG-1]  == 'RCB'     ):
            C.FABOOS[IWDG-1] = C.TRBOOS
        else:
            C.FABOOS[IWDG-1] = 1.

        ''' Booster losses are added to the regulating winding with
            C.BBOOSW=.T. . Only one winding shall have that addition.
            This is the reason why not 'RCB'-winding shall have
            C.BBOOS=.T. '''
        if(C.WDGFUN[IWDG-1]  == 'RB'):
            C.BBOOSW[IWDG-1] = True
        else:
            C.BBOOSW[IWDG-1] = False

    return
