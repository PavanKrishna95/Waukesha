def CURDNS():
    import com as C
    
    # Calculate current density and winding voltage
    for IWDG in range(1,1+C.NWILI):
        KTML=C.KGROUP[IWDG-1]
        C.CURRUT[IWDG-1]=C.SRATEP[KTML-1]/C.UN[KTML-1][1-1]/C.FABOOS[IWDG-1]
        if(C.BBAUTO and KTML==C.NPG and not(C.BBRW[IWDG-1] and notC.BBVFR)):
            C.CURRUT[IWDG-1]=C.CURRUT[IWDG-1]-C.SRATEP[KTML-1]/C.UN[C.NSG-1][0]/C.FABOOS[IWDG-1]
        C.VOLTUT[IWDG-1]=C.ZWINDW[IWDG-1]*C.UDIM[0]*C.FABOOS[IWDG-1]/1.E+3

