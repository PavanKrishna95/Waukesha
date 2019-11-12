def PRUX():
    import com as C

    CTAP=['Prc.  tap : ',
          'Max.  tap : ',
          'Min.  tap : ',
          'Spec. tap : ']

    NGMAX=min(3,C.NG)

     #WRITE(JFC,80) C.SRATE(1)/1.E+6
    #Calculate No. of taps to be used
    for JTML in range(1,NGMAX):
        #Adjust the No. of taps
        # If a 'special' tap is given
        NTAPS=1
        if(C.BBVR[JTML-1]):
            NTAPS=4
            if((C.NXSTEP[JTML-1]==C.NPSTEP[JTML-1]) or (C.NXSTEP[JTML-1]==C.NMSTEP[JTML-1]) or (C.NXSTEP[JTML-1]==0)):
                NTAPS=3

        C2=1.E-3
        if(C.KCON[JTML-1]==1 or C.KCON[JTML-1] ==11 ): C2=C.SQR3/1.E+3

        #Adjust the heading for each tap
        for ITML in range(JTML+1, 1+NGMAX):
            LTML=ITML+JTML-2
            IN=1
            if(C.BBVR[ITML-1]or C.BBVFR): IN=3
            C1=1.E-3
            if(C.KCON[ITML-1]==1 or C.KCON[ITML-1]==11): C1=C.SQR3/1.E+3
            #WRITE(JFC,81) ('U',ITML,C.UN(ITML,KTAP)*C1,KTAP=1,IN)

          #Adjust the heading for each tap
            for KTAP in range(1,1+NTAPS):
                #djust the heading
#*
#C,,, If regulated terminal or VFR
                if(C.BBVR[ITML-1] or C.BBVFR):
                    ROWHED='     '
    # If NON-regulated terminal or CFR

                else:
                    ROWHED=CTAP[KTAP-1]                

    return
