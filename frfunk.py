# Title:  Assigns free variables from the object-function
def FRFUNK(XA,ACOND,BBCURD,BBDLI,BBFLU,BBHLI,BLIMB,DCORE,HLIMB,NWILI):
    
    print("\n")
    print("start of FRFUNK")
    
    if(BBDLI): XA[0]=DCORE
    if(BBHLI): XA[1]=HLIMB
    if(BBFLU): XA[2]=BLIMB

    for IWDG in range(1,1+NWILI):
        if(BBCURD[IWDG-1]): XA[3+IWDG-1]=ACOND[IWDG-1]

    print("end of FRFUNK")
    return XA    



