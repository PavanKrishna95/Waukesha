#Title: Calculation of actual short-circuit stresses
import numpy
def SCSTRE(I,J,K,BBOUT):
    print("\n")
    print("start of SCSTRE")
    import com as C
    #DECLARATIONS
    UXBR=[0 for i in range(3)]
    RISC=[0 for i in range(3)]

    #END OF DECLARATIONS
    LPERM=[1,2,3,1,2]

    #UK
    #start if abbreviations
    X1=C.UXC[I-1][J-1][0]
    X2=C.UXC[I-1][K-1][1]
    X3=C.UXC[J-1][K-1][2]
    
    # End of Abbreviations
    
    #Total impedance per branch:

    #Start of Tot Imp/branch
    UXBR[0]=(X1+X2-X3)/2+C.XRINT[0]
    UXBR[1]=(X1+X3-X2)/2+C.XRINT[1]
    UXBR[2]=(X2+X3-X1)/2+C.XRINT[2]

    #End of Tot Imp/branch

    # Tap-changer position

    #Start of Tap.chgr position
    C.NPERM[0]=I
    C.NPERM[1]=J
    C.NPERM[2]=K

    #End of Tap.chgr position

    # "C.NPERM" denotes the actual tap-position for each winding group
    MAXTML=min(C.NG,3)
    for JTML in range(1,1+MAXTML):
        #Calculation of short-circuit currents for the terminal
        #branches, "ISC"
        # "ISC(I)" where "JTML" is the short-circuited terminal and
        #              "I" is the terminal with the actual current.
        # p.u.-values are used

        # If C.BBSCL(ITML)
        
        if(C.BBSCL[JTML-1]):
            JTML1=LPERM[JTML]
            JTML2=LPERM[JTML+1]
            X1=UXBR[JTML1-1]+C.EXTX[JTML1-1]
            X2=UXBR[JTML2-1]+C.EXTX[JTML2-1]
            Y=1
            X3=X2
            RISC[JTML-1]=0
            RISC[JTML1-1]=0
            if(C.BBSCR[JTML2-1] and C.BBSCR[JTML1-1]):  Y=X2/(X1+X2)
            if(C.BBSCR[JTML1-1]): X3=X1*Y
            if(C.BBSCR[JTML1-1] or C.BBSCR[JTML2-1]):   RISC[JTML-1]=1./(UXBR[JTML-1]+X3)
            if(C.BBSCR[JTML1-1]): RISC[JTML1-1]=-RISC[JTML-1]*Y
            RISC[JTML2-1]=-RISC[JTML-1]-RISC[JTML1-1]

#By using "RISC" the physical current densities "RIDENS" and
#C... magnetomotoric forces "FW0" will be calculated for the whole
#C... winding arrangement for the actual short-circuiut case starting
#C... with winding "A". When "RIDENS" and "FW0"  are known the inside &
#C... outside stresses will be calculated as "X2" and "X3" respectively.
#C... If now the mean value of "X2" and "X3" exceeds
#C...         "C.STRWMP" if positive
#C...     or  "C.STRWMM" if negative
#C... then new values for "C.STRWMM" and "C.STRWMP" respectively
#C... will be inserted.

            FW0=0

            #For each winding
            for IWDG in range(1,1+C.NWILI):
                N1=C.KGROUP[IWDG-1]

                #Calculations

                #If N1 < 3
                if(N1<=3):
                    N2=C.NPERM[N1-1]
                    I1=N2
                    if(C.BBVFR): I1=J
                    X4=C.POSIT[IWDG-1][I1-1]
                # Rev 94-04-12 Include Booster factor in calculation if Booster winding
                    if(not C.BBOOSW[IWDG-1]):    
                        X=C.SNOML*RISC[N1-1]/C.UN[N1-1][N2-1]
                    else:
                        X=C.SNOML*RISC[N1-1]/C.UN[N1-1][N2-1]/C.TRBOOS
                    #Calculate X
                        
                    #If Auto and N1 <> C.NPG
                    if(C.BBAUTO and N1 ==C.NPG):
                        if(C.BBVFR or not C.BBRW[IWDG-1]):
                            X=X+C.SNOML*RISC[C.NSG-1]/C.UN[C.NSG-1][C.NPERM[C.NSG-1]-1]

                    RIDENS=0
                    if(X4 != 0): RIDENS=X/C.ACOND[IWDG-1]* numpy.sign(X4)
                    X5=RIDENS*C.SCCONS*C.PI/C.HWINDM
                    X1=-FW0*C.DWIND[IWDG-1]*X5
                    FW0=FW0+X*C.ZWIND[IWDG-1]*X4
                    X2=-FW0*C.DWIND[IWDG-1]*X5
                    X3=(X1+X2)/2
                    if(X3<C.STRWMM[IWDG-1]):    C.STRWMM[IWDG-1]=X3
                    if(X3>C.STRWMP[IWDG-1]):    C.STRWMP[IWDG-1]=X3

        #Allocate values to certain variables
        #If BBOUT
                    if(BBOUT):
                        C.X10[IWDG-1]=X1
                        C.X20[IWDG-1]=X2
                        C.X30[IWDG-1]=X3
                        C.SHTCUR[IWDG-1]=X
            #Allocate values to certain variables

            #If BBOUT
            if(BBOUT):
                JTML0=JTML
                #. Print out the values

                if(C.NG<=2):
                    #Print out the table
                    #TABLE1(JTML0,3-JTML0,3)
                    pass
                else:
                    
                    pass
                    #Print out the table
                    #TABLE1(JTML0,JTML1,JTML2)
        
    print("end of SCSTRE")                    

    return
