def FUNKFR(XA,ACOND,BBCURD,BBDLI,BBFLU,BBHLI,NWILI,BLIMB,DCORE,HLIMB):
    print("START OF FUNKFR")
# Start of the declarations block.    
    
#End of the declarations block.
    
# Adjust DCORE, HLIMB and BLIMB as required.

# Start of the adjustment block.
    if(BBDLI): DCORE=abs(XA[0])
    if(BBHLI): HLIMB=abs(XA[1])
    if(BBFLU): BLIMB=abs(XA[2])

# End of the adjustment block.

# BLTOPM = Maximum allowed flux density for HI-B & over-magnetisation
# With this function  BLIMB < BLTOPM.

#Allocate values to ACOND for each winding

    for IWDG in range(1,1+NWILI):
        if(BBCURD[IWDG-1]): ACOND[IWDG-1]=abs(XA[3+IWDG-1])
    print("END OF FUNKFR")    
    return (BLIMB,DCORE,HLIMB,ACOND)
