
''' Title:  Determines whether the core is
            fully or partly varnished or not at all
            According to LT-TA 4610-117 '''

def CORVAR(TYP,DCOR,BPL):

    '''cTYP = Core Type ( D  =  1,
                          T  =  3,
                          EY =  7,
                          DY =  8,
                          TY 1-PHASE =  9,
                          TY 3-PHASE = 10) '''

    ''' If the whole core is to be varnished then TYP=0
        DCOR   = Nominal core diameter
        BPL  = Core plate width in mm '''

    CORVAR = False

    ''' Whole core varnished '''

    if(round(TYP)< 1):
        CORVAR=True

        ''' Part of core varnished '''

    elif(round(TYP)<7):

        ''' Undivided cores '''

        if(DCOR >=750. and BPL >= 500.): CORVAR=True

    else:

        ''' Divided cores '''

        if((round(TYP) <= 9 and DCOR >= 750. and BPL >=350.) or
           (round(TYP) == 10 and DCOR >= 600. and BPL >=250.)):CORVAR= True

    return CORVAR
