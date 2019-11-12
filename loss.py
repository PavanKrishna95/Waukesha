#Title:  Calculate the winding losses
#        Calculate the resistive
#        and eddy-current losses for a specified
#        two-winding performance case

from edmult import EDMULT
def LOSS():
    print("start of LOSS")
    import com as C
    #Start of the declarations block.
    TWTHRD=0.6666667

    #end of the declarations block.
    CURMAX=0
    MAXCW=0
    C.FLUXM=0
    FI0=0
    FW2=0
    FW1=0
    C.PCU=0
    C.PED=0
    D0=0
    SCALE=0.5*C.SQR2*C.PI*C.RMY0/C.HWINDM

    #Calculate for each winding

    for IWDG in range(1,1+C.NWILI):
        C.FLUXI[IWDG-1]=0
        C.FLUXO[IWDG-1]=0
        CURR=C.CUR[IWDG-1]

    #Part 1, Eddy current losses

    #NON-current-carrying winding
        if(CURR==0):
            C.PCUW[IWDG-1]=0
            print("LOSS calling EDMULT")
            C.PEDW[IWDG-1]=EDMULT(0.0,FW2,C.EDDCON[IWDG-1])                 #WATCHOUT

        else:
            D1=C.DWIND[IWDG-1]
            B1=C.RRWDG[IWDG-1]
            FW1=C.ZWIND[IWDG-1]*C.FRACTW[IWDG-1]*CURR
            print('ipk2',FW1,C.ZWIND[IWDG-1],C.FRACTW[IWDG-1],CURR,(FW1+FW2)*FW2,FW2)    
        #Remember which winding that has highest current and calculate
            if(abs(CURR)>CURMAX):
                CURMAX=abs(CURR)
                MAXCW=IWDG    

        #Calculation of the resistive (I2R) losses in winding "IWDG"

            C.PCUW[IWDG-1]=C.RWIND[IWDG-1]*CURR*CURR*abs(C.FRACTW[IWDG-1])

            if(C.BBOOSW[IWDG-1]): C.PCUW[IWDG-1]=C.PCUW[IWDG-1]+ CURR*CURR*C.REBOOS*C.TRBOOS*C.TRBOOS
            C.PCU=C.PCU+C.PCUW[IWDG-1]

        #Calculation of the eddy-current losses in windings
        #due to the axial leakage flux
            print("LOSS calling EDMULT")
            C.PEDW[IWDG-1]=EDMULT(FW1,FW2,C.EDDCON[IWDG-1])

        #Leakage flux in the duct between windings "MUT(I-1)" and "IWDG"

            D2=D1-B1

            FLUXD=(D2*D2-D0*D0)*FW2/2.

            if(abs(FLUXD*SCALE)>abs(C.FLUXMD[IWDG-1])):
                C.FLUXMD[IWDG-1]=FLUXD*SCALE
            FI0=FLUXD+FI0   
            D0=D1+B1  
        #    Calculate the flux in the winding

    #If the ampere-turn diagram crosses the zero-line in the
    # actual winding "IWDG"

            if(((FW1+FW2)*FW2) < 0):
                print('insideif',FW1,FW2)
                C.FLUXI[IWDG-1]=FI0
                BX=0
                if(FW1!=0): BX=-B1*FW2/FW1
                FLUXW1=BX*(D2+TWTHRD*BX)*FW2
                FI0=FLUXW1+FI0
                if(abs(FI0) > C.FLUXM): C.FLUXM=abs(FI0)
                BX=B1-BX
                FLUXW2=BX*(D0-TWTHRD*BX)*(FW2+FW1)
                if(abs((FLUXW1+FLUXW2)*SCALE) > abs(C.FLUXMW[IWDG-1])):
                    C.FLUXMW[IWDG-1]=(FLUXW1+FLUXW2)*SCALE
                FI0=FLUXW2

                C.FLUXO[IWDG-1]=FI0

    #If the ampere-turn diagram DOES NOT cross the zero-line in the
    #actual winding "IWDG"            
            else:
                C.FLUXI[IWDG-1]=FI0
                FLUXW=B1*(D1*(FW2+FW2+FW1)+B1*FW1/3)
                if(abs(FLUXW*SCALE) > abs(C.FLUXMW[IWDG-1])):
                    C.FLUXMW[IWDG-1]=FLUXW*SCALE
                FI0=FLUXW+FI0
                C.FLUXO[IWDG-1]=FI0
            FW2=FW2+FW1
            
        C.PED=C.PED+C.PEDW[IWDG-1]

        C.FLUXI[IWDG-1]=C.FLUXI[IWDG-1]*SCALE
        C.FLUXO[IWDG-1]=C.FLUXO[IWDG-1]*SCALE

    print('aaaaaaaaaaafluxo',C.FLUXO)
    if(abs(FI0)>C.FLUXM): C.FLUXM=abs(FI0)
    C.FLUXM=C.FLUXM*SCALE

#Decide if we have a D2-winding as outer winding for correction
#of high current transformers. If so we must correct C.BPOED to
#zero as the Other eddy loss already is compensated.

    if((C.KWITYP[C.NWILI-1]==5)and(MAXCW==C.NWILI)):
        C.BPOED=0
       
    C.POED=C.APOED*C.FLUXM**1.46+C.BPOED*CURMAX*CURMAX
    C.POED=C.POED*(C.FREQ/50.)**1.5
    return
