#Title:  Calculation of penalty costs for the
#        optimisation routine

def PENLTY():
    import com as C
    print("\n")
    print("start of PENLTY")

    G=[0 for i in range(50)]

    #Allocate values to the G-vector
    # Start of the first G-block
    G[0]=C.URC[0][0][0]*C.ZWOULI -C.PLOADM
    G[1]=C.P00[0] -C.PNOLOM
    G[2]=(C.DCORE-C.DCOMAX)*(C.DCORE-C.DCOMIN)/(C.DCOMAX-C.DCOMIN)
    G[3]=C.VALUEO  -C.VALUEM
    G[4]=C.HTANK  -C.HTANKM
    G[5]=(C.HLIMB-C.HLMBMA)*(C.HLIMB-C.HLMBMI)/(C.HLMBMA-C.HLMBMI)
    G[6]=C.BTANK -C.BTANKM
    G[7]=C.RLTANK -C.RLTNKM
    G[8]=C.GTRP -C.GTRPM
    G[9]=C.SOUND0[1]-C.SOUNDM
    G[10]=C.UXC[0][0][0]-C.USHORE

    #BLMIN is the minimum flux density practicable.
    BLMIN=0.8

    G[11]=(C.BLIMB-C.BLTOPM)*(C.BLIMB-BLMIN)/(C.BLTOPM-BLMIN)

    #End of the first G-block

    #Allocate values to the G-vector for each winding

    #C.PRESSM values are negative

    for IWDG in range(1,1+C.NWILI):
        G[13+3*(IWDG-1)-1]=C.CURDEN[IWDG-1]-C.CURDM[IWDG-1]
        G[14+3*(IWDG-1)-1]=C.PRESSM[IWDG-1]-C.STRWMM[IWDG-1]
        G[15+3*(IWDG-1)-1]=C.STRWMP[IWDG-1]-C.TENSM[IWDG-1]
    print("end of PENLTY")
    return G    










