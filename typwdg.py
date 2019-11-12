
'''' Title:  Convert the winding types
         for the winding layout routines
         KWITYP --->  C.KWIND '''

def TYPWDG():
    import com as C
    NCOL =['A','B','C','D','E','F','G','H','I']

    ''' Winding data '''

    for IWDG in range(1,C.NWILI+1):
        if( (C.TARR[30+IWDG-1] == 'S') or
             (C.TARR[30+IWDG-1] == 'S1')) : 
            C.KWIND[IWDG-1]=1
        elif (C.TARR[30+IWDG-1] == 'S2') : 
            C.KWIND[IWDG-1]=2
        elif (C.TARR[30+IWDG-1] == 'S3') : 
            C.KWIND[IWDG-1]=3
        elif (C.TARR[30+IWDG-1] == 'S4') : 
            C.KWIND[IWDG-1]=4
        elif (C.TARR[30+IWDG-1] == 'S5') : 
            C.KWIND[IWDG-1]=5
        elif (C.TARR[30+IWDG-1] == 'S6') : 
            C.KWIND[IWDG-1]=6
        elif (C.TARR[30+IWDG-1] == 'S7') : 
            C.KWIND[IWDG-1]=6
        elif (C.TARR[30+IWDG-1] == 'S8') : 
            C.KWIND[IWDG-1]=6
        elif (C.TARR[30+IWDG-1] == 'S9') : 
            C.KWIND[IWDG-1]=6
        elif (C.TARR[30+IWDG-1] == 'S10') : 
            C.KWIND[IWDG-1]=6
        elif (C.TARR[30+IWDG-1] == 'S11') : 
            C.KWIND[IWDG-1]=6
        elif (C.TARR[30+IWDG-1] == 'S12') : 
            C.KWIND[IWDG-1]=6
        elif (C.TARR[30+IWDG-1] == 'L') : 
            C.KWIND[IWDG-1]=11
        elif (C.TARR[30+IWDG-1] == 'L1') : 
            C.KWIND[IWDG-1]=12
        elif (C.TARR[30+IWDG-1] == 'L2') : 
            C.KWIND[IWDG-1]=13
        elif (C.TARR[30+IWDG-1] == 'L3') : 
            C.KWIND[IWDG-1]=14
        elif (C.TARR[30+IWDG-1] == 'CD') : 
            C.KWIND[IWDG-1]=0
        elif (C.TARR[30+IWDG-1] == 'SD') : 
            C.KWIND[IWDG-1]=100
        elif (C.TARR[30+IWDG-1] == 'D2') : 
            C.KWIND[IWDG-1]=100
        elif (C.TARR[30+IWDG-1] == 'SLS') : 
            C.KWIND[IWDG-1]=11
        elif (C.TARR[30+IWDG-1] == 'SLS1') : 
            C.KWIND[IWDG-1]=11
        elif (C.TARR[30+IWDG-1] == 'SLS2') : 
            C.KWIND[IWDG-1]=12
        elif (C.TARR[30+IWDG-1] == 'SLS3') : 
            C.KWIND[IWDG-1]=13
        elif (C.TARR[30+IWDG-1] == 'SLS4') : 
            C.KWIND[IWDG-1]=14
        elif (C.TARR[30+IWDG-1] == 'SLS5') : 
            C.KWIND[IWDG-1]=15
        elif (C.TARR[30+IWDG-1] == 'SLS6') : 
            C.KWIND[IWDG-1]=16
        elif (C.TARR[30+IWDG-1] == 'SLL') : 
            C.KWIND[IWDG-1]=7
        elif (C.TARR[30+IWDG-1] == 'SLL1') : 
            C.KWIND[IWDG-1]=7
        elif (C.TARR[30+IWDG-1] == 'SLL2') : 
            C.KWIND[IWDG-1]=10

    return
