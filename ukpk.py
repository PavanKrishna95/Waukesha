import numpy

def UKPK(U1,U2,U3,UX12,UX13,UX23,UR12,UR13,UR23):
    ##### Declarations #####
    import com as C
    
    UCONV=[[0. for i in range(4)]for j in range(4)]
    
    ##### End of Declarations #####

    ##### Calculate values for each terminal #####
    for JTML in range(1,C.NG+1):

        CCON=C.UNLINE[JTML-1]/C.UDIM[JTML-1]
        UCONV[0][JTML-1]=C.UN[JTML-1][0]*CCON
        if (C.BBVR[JTML-1]):UCONV[1][JTML-1]=C.UN[JTML-1][1]*CCON
        if (C.BBVR[JTML-1]):UCONV[2][JTML-1]=C.UN[JTML-1][2]*CCON
        if (C.BBVR[JTML-1]):UCONV[3][JTML-1]=C.UN[JTML-1][3]*CCON
  
    N2=2
    if (C.BBVR[0] and not C.BBVR[1]):N2=1
    BB1=False
    if (C.BBVR[0] or C.BBVR[1]):BB1=True

    ##### Calculate values for each terminal #####

    for JTML in range(1,5):
        U1[JTML-1]=UCONV[0][JTML-1]/1.E+3
        U2[JTML-1]=UCONV[1][JTML-1]/1.E+3
        U3[JTML-1]=UCONV[2][JTML-1]/1.E+3
        #U4[JTML-1]=UCONV[3][JTML-1]/1.E+3

        if (not C.BBVR[1]):UX12[JTML-1]=C.UXC[JTML-1][0][0]*100.
        if (C.BBVR[1]):UX12[JTML-1]=C.UXC[0][JTML-1][0]*100.

        if (not C.BBVR[1]):UR12[JTML-1]=C.URC[JTML-1][0][0]*C.NWOULI/1.E+3
        if (C.BBVR[1]):UR12[JTML-1]=C.URC[0][JTML-1][0]*C.NWOULI/1.E+3

    UX13[0]=C.UXC[0][0][1]*100.
    UX23[0]=C.UXC[0][0][2]*100.

    UR13[0]=C.URC[0][0][1]*C.NWOULI/1.E+3
    UR23[0]=C.URC[0][0][2]*C.NWOULI/1.E+3

    return (U1,U2,U3,UX12,UX13,UX23,UR12,UR13,UR23)
