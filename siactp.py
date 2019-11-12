''' Title:  Convert indata to SI-units and
            transfer them to internal variables
            for variables which do NOT refer to
            Tank, Terminals or Windings '''

from fbb import FBB
def SIACTP():
    import com as C
    C.NPHAS=C.IARR[0]
    C.FREQ=C.AARR[1]
    C.UMAXPU=1.+(C.AARR[4]/1.E+2)

    ''' Maximum losses - Loss evaluation '''
    
    ''' SC.BBL Start of the Max. losses block. '''

    C.PNOLOM=0.
    if (C.AARR[5]<0.): C.PNOLOM=-1.E+3*C.AARR[5]
    C.P0LOSS=0.
    if (C.AARR[5]>=0.): C.P0LOSS=C.AARR[5]/1.E+3
    C.PLOADM=0.
    if (C.AARR[6]<0.): C.PLOADM=-1.E+3*C.AARR[6]
    C.PKLOSS=0.
    if (C.AARR[6]>=0.): C.PKLOSS=C.AARR[6]/1.E+3

    ''' End of the Max. losses block. '''

    C.DPHAS=C.AARR[140]/1.E+3
    C.DPHSL=C.AARR[141]/1.E+3
    C.NWOULI=C.IARR[50]
    C.ZWOULI=float(C.NWOULI)
    C.TWSUP=C.BARR[29]/1.E+3
    C.DCORE=C.AARR[142]/1.E+3
    C.BLIMB=C.AARR[145]
    FONAN=C.AARR[153]
    C.QFINAL=1.E+6*C.BARR[30]

    if (abs(C.AARR[3])>100.): C.DARR[19]=C.AARR[3]

    ''' This transfer because HLIMB can be input in two ways.
        In future only C.DARR(20) will be used for this purpose. '''

    C.CORBND=C.TARR[79]
    C.ILACK=C.DARR[29]

    C.KCOOL=-1
    if (C.TARR[55] == 'NO'): C.KCOOL=0
    if (C.TARR[55] == 'ONAN'): C.KCOOL=1
    if (C.TARR[55] == 'ONAF'): C.KCOOL=2
    if (C.TARR[55] == 'OFAF'): C.KCOOL=3
    if (C.TARR[55] == 'ONAN/F'): C.KCOOL=4

    ''' Illegal mixture of cooling type and self cool ratio '''

    if (FONAN > 1.001):
        if (C.KCOOL<=1 or C.KCOOL == 3):
            C.JFC,C.BBERR=FPRINT(2,C.BBERR,
                        'SIACTP: Illegal mixture of self cooling ratio and cooling type')

            ''' Backtracking '''
            if(C.ISTOP ==1 ):return

    if (C.KCOOL==1):
        if (FONAN<=0.99 or FONAN >= 1.01):
            C.JFC,C.BBERR=FPRINT(2,C.BBERR,
                        'SIACTP: Illegal mixture of self cooling ratio and cooling type') 

            ''' Backtracking'''
            if(C.ISTOP==1):return

    ''' Illegal cooling type '''

    if (C.KCOOL<0):
        C.JFC,C.BBERR=FPRINT(2,C.BBERR,
                    'SIACTP:Illegal cooling type')

        ''' Backtracking '''
        if(C.ISTOP==1):return

    ''' Calculation of preliminary cooling variables '''

    ''' Start of the prel cooling block. '''

    C.KCOOL2=C.KCOOL
    if (C.KCOOL>3): C.KCOOL2=2
    if (C.KCOOL==0): C.KCOOL2=1


    C.TWINDM=C.AARR[154]
    C.TTOILM=C.AARR[155]
    C.TTOILC=C.AARR[99]

    ''' Set certain values for C.AARR '''

    #PREACT()

    C.GTRPM=1.E+3*C.AARR[172]
    C.SOUNDM=C.AARR[176]
    C.AFIELD=C.AARR[156]
    C.HLMBMA=C.DARR[9]/1.E+3
    C.HLMBMI=C.DARR[39]/1.E+3

    ''' End of the prel cooling block. '''

    C.BBWISU=False
    if (C.BARR[29]>0.): C.BBWISU=True

    C.BBSLIM=FBB('SIACTP',C.BBERR,C.TARR[50])

    C.EXTCOR=False
    if (C.TARR[0]=='EXT'): C.EXTCOR=True

    C.BB051=FBB('SIACTP',C.BBERR,C.TARR[72])
    C.BB132=FBB('SIACTP',C.BBERR,C.TARR[74])
    C.BBFLDS=FBB('SIACTP',C.BBERR,C.TARR[2])
    C.BBDSHE=FBB('SIACTP',C.BBERR,C.TARR[3])
       
    ''' Reoptimisation '''

    C.CPUIND=C.AARR[160]

    return
