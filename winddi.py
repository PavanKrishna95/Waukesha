from ukx import UKX
from fprint import FPRINT
import math
def WINDDI():
    import com as C
    print("START OF WINDDI")
   
    NCOL=['A','B','C','D','E','F','G','H','I']
    FWIND0=[0 for i in range(9)]
    ZWIND0=[0 for i in range(9)]
    DCORE1=0

    #Calculate mean winding height

    #Start of the mean winding height block
    ABSFW=0
    ABSDFW=0
    DCOR0=0
    TURNR0=0

    #For each winding
    for IWDG in range(1,1+C.NWILI):
        ABSFW=ABSFW+abs(C.FWIND[IWDG-1])    
        ABSDFW=ABSDFW+C.DYOKE[IWDG-1]*abs(C.FWIND[IWDG-1])
    
    DYOKE0=ABSDFW/ABSFW
    C.HWINDM=C.HLIMB-DYOKE0

    #End of the mean winding height block

    #Calculate certain variables for each winding

    #If no limb height or reactance given

    if(not C.BBHLI and not C.BBREA):
        DCOR0=C.DCORE
        TURNR0=C.TURNRA
    
    #Calculate for each winding    

        for IWDG in range(1,1+C.NWILI):
            FWIND0[IWDG-1]=C.FWIND[IWDG-1]
            ZWIND0[IWDG-1]=C.ZWIND[IWDG-1]
    
    BBEND=False

    #Calculate the winding dimensions unless BBEND is true
    while(not BBEND):
        DW1=C.DCORE
        BW1=0
        
    #Calculate for each winding
        for IWDG in range(1,1+C.NWILI):
            C.HWIND[IWDG-1]=C.HLIMB-C.DYOKE[IWDG-1]

            if(not C.BBRR[IWDG-1]): C.RRWDG[IWDG-1]=C.AWIND[IWDG-1]/C.HWIND[IWDG-1]    
            C.DWIND[IWDG-1]=DW1+BW1+2.*C.BDUCT[IWDG-1]+C.RRWDG[IWDG-1]
            
            BW1=C.RRWDG[IWDG-1]
            DW1=C.DWIND[IWDG-1]
            
        C.DOUTW=DW1+BW1
    #Calculate reactance    
    #If 'EXACT' calculation and no reactance specified
        if(C.BBEXAC and (not C.BBREA) ):
            UX=0.
            UX=UKX(UX)                                         #WATCHOUT
        # Calculate certain variables       
        
            if(abs(C.USHORE/UX-1)>=1.E-5):
                print('aaaaaaaaaaaaaaaaaaaaaaaaaa',UX)
        #Calculate certain variables    
        # If no limb height was given
                if(not C.BBHLI):
                    DCORE1=C.DCORE/((C.USHORE/UX)**0.25)
                    HLP=abs(DCORE1-C.DCORE)
                    if(HLP< 0.5E-3):BBEND=True

        #Calculate certain variables   
        # If not the final calculation
                    if(not BBEND):

                        C.DCORE=DCORE1
                        RATDCO=(DCOR0/C.DCORE)*(DCOR0/C.DCORE)
                        C.TURNRA=TURNR0*RATDCO


        #Calculate for each winding
                        for IWDG in range(1,1+C.NWILI):
                            C.FWIND[IWDG-1]=FWIND0[IWDG-1]*RATDCO
                            C.ZWIND[IWDG-1]=ZWIND0[IWDG-1]*RATDCO
                            if(not C.BBRR[IWDG-1]):
                                C.AWIND[IWDG-1]=C.ACOND[IWDG-1]*C.ZWIND[IWDG-1]/C.FILLF[IWDG-1]
        #If limb height was given   
                else:
                    C.HWINDM=C.HWINDM*max(0.5,1.-0.60*(C.USHORE/UX-1.))
                    C.HLIMB=C.HWINDM+DYOKE0
        #If ratio=1         
            else:
                BBEND=True
        else:
            BBEND=True

    #Calculate for each winding
    for IWDG in range(1,1+C.NWILI):
        if(C.BBRR[IWDG-1]):
            C.FILLF[IWDG-1]=C.ACOND[IWDG-1]*C.ZWIND[IWDG-1]/(C.HWIND[IWDG-1]*C.RRWDG[IWDG-1])
            print(C.ACOND[IWDG-1],C.ZWIND[IWDG-1],C.HWIND[IWDG-1],C.RRWDG[IWDG-1])
    #Space factor is greater than 1
        if(C.FILLF[IWDG-1]>=1):
            C.JFC,C.BBERR=FPRINT(2,C.BBERR,'WINDDI:Space factor is missing for winding '+NCOL[IWDG-1]+' IS GREATER THAN 1 ')
            if(C.ISTOP==1):
                return
            
        RLW0=C.PI*C.DWIND[IWDG-1]*C.ZWIND[IWDG-1]
        C.GWINCO[IWDG-1]=RLW0*C.ACOND[IWDG-1]*C.RAACON[IWDG-1]    

        #Electrical properties
       
        #Start of the electrical properties block
        C.RWIND[IWDG-1]=RLW0/(C.SIGM[IWDG-1]*C.ACOND[IWDG-1])
        C.EDDCON[IWDG-1]=C.EDDCO1[IWDG-1]*C.GWINCO[IWDG-1]*(C.BPART[IWDG-1]/C.HWINDM)*(C.BPART[IWDG-1]/C.HWINDM)

    #End of the electrical properties block    
    print("END OF WINDDI")

    return
