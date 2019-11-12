''' Title:  Check whether 99% and/or 100% limits exceeded.
            Called from CONSTR.
            Critical parameters are saved in SAVE1.
            NCONST stores the No. of critical parameters.
            Printout of SAVE1 via PAGE01 '''

def LIMCHK(VALUE,TEXT1,TEXT2,NCONST,SAVE1):

    ''' Check which limit has been exceeded. '''

    if(VALUE > 1.001 and  TEXT2 !='       '):
        NCONST=NCONST+1
        SAVE1[NCONST-1]=TEXT2

    elif(VALUE > 0.990 and TEXT1 !='       ') :
        NCONST=NCONST+1
        SAVE1[NCONST-1]=TEXT1

    elif(VALUE < 0. and TEXT1 != '       '):

        ''' Total up '''
        if(abs(VALUE) > 1.E-3):
            NCONST=NCONST+1
            SAVE1[NCONST-1]=TEXT1

    return NCONST,SAVE1
