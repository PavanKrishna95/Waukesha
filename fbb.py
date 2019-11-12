from fprint import FPRINT
def FBB(SUB,BBERR,TEXT):
    import com as C

    ICODE=0
    if(TEXT[0]=='Y'): ICODE=1
    if(TEXT[0]=='N'): ICODE=2

    if(ICODE==0):
            C.JFC,C.BBERR=FPRINT(2,BBERR,"{0} (FBB):Y,Yes,N or No is required".format(SUB))

    if(ICODE==1):
        return True
    else:
        return False            
