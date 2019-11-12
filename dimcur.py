def DIMCUR():
    print("start of DIMCUR")
    import com as C

    for KTML in range(1,1+C.NG):
        C.RIDIMW[KTML-1]=C.SRATEP[KTML-1]/C.UN[KTML-1][0]
        C.RIDIRW[KTML-1]=C.RIDIMW[KTML-1]

    if(C.BBAUTO):
        C.RIDIMW[C.NPG-1]=C.RIDIMW[C.NPG-1]-C.RIDIMW[C.NSG-1]
        AUTO=1-C.UDIM[C.NPG-1]/C.UDIM[C.NSG-1]
        if(C.BBVFR):
            C.RIDIRW[C.NPG-1]=C.RIDIMW[C.NPG-1]

# NOT BBAUTO
    else:
        AUTO=1

#Calculate equivalent 2-winding rating
    I1=1
    I2=1
    I3=0
    if(C.NG>=3): I3=1
    I4=0
    if(C.NG>=4): I4=1
    C.SEQU2W=(AUTO*(C.SRATEP[0]*I1+C.SRATEP[1]*I2)+C.SRATEP[2]*I3+C.SRATEP[3]*I4)/2

    print("end of DIMCUR")
