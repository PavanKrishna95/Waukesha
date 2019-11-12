
def SSEARC(ARG, ARRAY ,MAX ,IND,FOUND):
    
    FOUND=False
    MAX=0
    IND=0
    I=0

    while ((not FOUND) and I<=MAX):
        if(ARG == ARRAY[I-1]):
            IND=I
            FOUND=True
        else:
            I=I+1

    return(ARG,ARRAY,MAX,IND,FOUND)
