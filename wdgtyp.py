
''' Title:  Convert the winding types
            to the same classification of windings as in T31146
            from the winding layout routines
            C.KWIND  --->  C.KWITYP '''

def WDGTYP():

    import com as C

    ''' Translation to the same classification of windings as in T31146 '''

    for IWDG in range(1,C.NWILI+1):
        if  (C.KWIND[IWDG-1] == 1  ) :
            C.TARR[30+IWDG-1]='S1'
            C.KWITYP[IWDG-1]=1
        elif (C.KWIND[IWDG-1] == 2  ) :
            C.TARR[30+IWDG-1]='S2'
            C.KWITYP[IWDG-1]=1
        elif (C.KWIND[IWDG-1] == 3  ) :
            C.TARR[30+IWDG-1]='S3'
            C.KWITYP[IWDG-1]=1
        elif (C.KWIND[IWDG-1] == 4  ) :
            C.TARR[30+IWDG-1]='S4'
            C.KWITYP[IWDG-1]=1
        elif (C.KWIND[IWDG-1] == 5  ) :
            C.TARR[30+IWDG-1]='S5'
            C.KWITYP[IWDG-1]=1
        elif (C.KWIND[IWDG-1] == 6  ) :
            C.TARR[30+IWDG-1]='S6'
            C.KWITYP[IWDG-1]=1
        elif (C.KWIND[IWDG-1] == 11 ) :
            C.TARR[30+IWDG-1]='L'
        elif (C.KWIND[IWDG-1] == 12 ) :
            C.TARR[30+IWDG-1]='L1'
        elif (C.KWIND[IWDG-1] == 13 ) :
            C.TARR[30+IWDG-1]='L2'
        elif (C.KWIND[IWDG-1] == 14 ) :
            C.TARR[30+IWDG-1]='L3'
        elif (C.KWIND[IWDG-1] == 11 ) :
            C.TARR[30+IWDG-1]='SLS1'
        elif (C.KWIND[IWDG-1] == 12 ) :
            C.TARR[30+IWDG-1]='SLS2'
        elif (C.KWIND[IWDG-1] == 13 ) :
            C.TARR[30+IWDG-1]='SLS3'
        elif (C.KWIND[IWDG-1] == 14 ) :
            C.TARR[30+IWDG-1]='SLS4'
        elif (C.KWIND[IWDG-1] == 15 ) :
            C.TARR[30+IWDG-1]='SLS5'
        elif (C.KWIND[IWDG-1] == 16 ) :
            C.TARR[30+IWDG-1]='SLS6'
        elif (C.KWIND[IWDG-1] == 7  ) :
            C.TARR[30+IWDG-1]='SLL1'
            C.KWITYP[IWDG-1]=7
        elif (C.KWIND[IWDG-1] == 10 ) :
            C.TARR[30+IWDG-1]='SLL2'
            C.KWITYP[IWDG-1]=7
        elif (C.KWIND[IWDG-1] == 100 ) :
            C.TARR[30+IWDG-1]='SD'
            C.KWITYP[IWDG-1]=4
        elif (C.KWIND[IWDG-1] == 0 ) :
            C.TARR[30+IWDG-1]='CD'
            C.KWITYP[IWDG-1]=3
 
    ''' for IWDG in range(1,C.NWILI+1):
        if (C.KWIND[IWDG-1] == 11 or C.KWIND[IWDG-1] == 12) :
            C.ZCOIAR[IWDG-1]=float(C.KWIND[IWDG-1]-10)
            C.KWITYP[IWDG-1]=9
        elif (C.KWIND[IWDG-1] == 13 or C.KWIND[IWDG-1] == 14) :
            C.ZCOIAR[IWDG-1]=float(C.KWIND[IWDG-1]-12)
            C.KWITYP[IWDG-1]=9
        elif (C.KWIND[IWDG-1] == 15 or C.KWIND[IWDG-1] == 16) :
            C.ZCOIAR[IWDG-1]=float(C.KWIND[IWDG-1]-14)
            C.KWITYP[IWDG-1]=9
        elif (C.KWIND[IWDG-1] >= 21 and C.KWIND[IWDG-1] <= 29) :
            C.ZCOIAR[IWDG-1]=float(C.KWIND[IWDG-1]-20)
            C.KWITYP[IWDG-1]=9
        elif (C.KWIND[IWDG-1] >= 30 and C.KWIND[IWDG-1] <= 39) :
            C.ZCOIAR[IWDG-1]=float(C.KWIND[IWDG-1]-30)
            C.KWITYP[IWDG-1]=8 '''

    return
