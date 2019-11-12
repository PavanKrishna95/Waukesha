#Title: Calculation of short-circuit impedance

import math
def UKX(UK):
    print("start of ukx")
    import com as C

    UK=0.
    #Calculate for each winding ( except the outermost )
    for IWDG in range(1,C.NWILI):
        #calculate

        if(C.FACT[IWDG-1]!=0):
            D1=C.DWIND[IWDG-1]
            T1=C.RRWDG[IWDG-1]

    #Calculate for next winding
            for JWDG in range(IWDG+1,1+C.NWILI):
                #CALCULATE
                if(C.FACT[JWDG-1]!=0):
                    D2=C.DWIND[JWDG-1]
                    T0=C.RRWDG[JWDG-1]+T1
                    T=(D2-D1+T0)/2
                    X1=C.PI*C.HWINDM/T
                    HLP=0
                    
                    if(abs(X1)<60): HLP = math.exp(-X1)
                    UK=UK-(T-0.66666667*T0)*(D1+D2)*C.FWIND[IWDG-1]*C.FWIND[JWDG-1]*(1-(1-HLP)/X1)                 

    #Calculate UK
    UK=UK*2*C.PI**3/10*(C.FREQ/50)/C.SNOML/C.HWINDM/1.E+4
    print("UK=",UK)
    print("C.FREQ={0} C.SNOML={1} C.HWINDM={2}".format(C.FREQ,C.SNOML,C.HWINDM))
    #End if uk block
    print("end of ukx")

    return UK
