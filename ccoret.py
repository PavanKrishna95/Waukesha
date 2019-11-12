from cost import COST
def CCORET(BBPRNT,JFC,NCOR,NLAM,NCLA,GS211,GS212,\
    GG21,GS241,GS242,GG24,GS25,DCORE):
    
    if(BBPRNT):
        #WRITE(JFC,*) '===== INPUT DATA TO CCORET                   ====='
        #WRITE(JFC,*) SP1,'NCOR  ',SP,'NLAM  ',SP,'NCLA  ',SP,'GS211'
        #WRITE(JFC,*) NCOR,NLAM,NCLA,GS211
        #WRITE(JFC,*) SP1,'GS212',SP,'GG21  ',SP,'GS241',SP,'GS242'
        #WRITE(JFC,*) GS212,GG21,GS241,GS242
        #WRITE(JFC,*) SP1,'GG24  ',SP,'GS25 ',SP,'DCORE '
        #WRITE(JFC,*) GG24,GS25,DCORE
        pass

    IX=29+NCLA
    COST (4,IX,153,GS211,1.,1.,0.,1.,GS211,1.,1.,1.)

    IX=33+NCLA
    COST (4,IX,154,GS212,1.,1.,0.,1.,GS212,1.,1.,1.)

    IX=37+NCLA
    COST (3,IX,155,0.,1.,1.,GG21,GG21,1.,1.,1.,1.)

    if(NLAM==1):
        COST (4,46,160,GS241,1.,1.,0.,1.,1.,1.,1.,1.)
        COST (4,47,161,GS242,1.,1.,0.,1.,1.,1.,1.,1.)

    elif(NLAM==2):    
        COST (4,48,162,GS241,1.,1.,0.,1.,1.,1.,1.,1.)
        COST (4,49,163,GS242,1.,1.,0.,1.,1.,1.,1.,1.)

    elif(NLAM==3):
        COST (4,104,162,GS241,1.,1.,0.,1.,1.,1.,1.,1.)
        COST (4,106,163,GS242,1.,1.,0.,1.,1.,1.,1.,1.)    

    elif(NLAM==4):
        COST (4,76,162,GS241,1.,1.,0.,1.,1.,1.,1.,1.)
        COST (4,76,163,GS242,1.,1.,0.,1.,1.,1.,1.,1.)

    if(NCOR==1): IX=50
    if(NCOR==3): IX=51
    if(NCOR>=7): IX=45+NCOR

    if(NLAM==3 or NLAM==4):
        COST (4,IX,164,0.999,DCORE,1.,GG24,1.,DCORE,1.3,1.,1.)
    else:
        COST (4,IX,164,0.999,DCORE,1.,GG24,1.,DCORE,1.,1.,1.)
    COST (3,0,165,0.,1.,1.,0.,1.,1.,1.,1.,1.)
    if(not(int(GS25)==0)):
        COST (3,63,166,GS25,1.,1.,0.,1.,GS25,1.,1.,1.)

    COST (2,0,167,0.,1.,1.,0.,1.,1.,1.,1.,1.)
    
    return
