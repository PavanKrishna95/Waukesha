from cost import COST
def CACTP(BBPRNT,JFC,GS41,GS42,GS45,GS46,GS47,GS48,
    NLIMB,DCORE,GS24,GG49,RCONN ,ACONDA ,EFKV , NG, BBREAC):
    from cost import COST
    SP1='       '
    SP='          '

    if(BBPRNT):
        #WRITE(JFC,*) '===== INPUT DATA TO CAPTP                    ====='
        #WRITE(JFC,*) SP1,'GS41 ',SP,'GS42 ',SP,'GS45 ',SP,'GS46 '
        #WRITE(JFC,*) GS41 ,GS42 ,GS45 ,GS46
        #WRITE(JFC,*) SP1,'GS47 ',SP,'GS48 ',SP,'NLIMB ',SP,'DCORE '
        #WRITE(JFC,*) GS47 ,GS48 ,NLIMB ,DCORE
        #WRITE(JFC,*) SP1,'GS24 ',SP,'GG49  ',SP,'RCONN ',SP,'ACONDA'
        #WRITE(JFC,*) GS24 ,GG49  ,RCONN ,ACONDA
        #WRITE(JFC,*) SP1,'EFKV  ',SP,'NG    ',SP,'BBREAC'
        #WRITE(JFC,*) EFKV  ,NG    ,BBREAC
        pass

    # INSULATION DETAILS

    #****    MAIN DUCT    ****
    COST(4,77,180,GS41,1.,1.,0.,1.,GS41,1.,1.,1.)
    #****  OUTS.OUT.WIND  ****
    COST(4,78,181,GS42,1.,1.,0.,1.,GS42,1.,1.,1.)
    #****  OUT CORE LIMB  ****
    COST(4,81,182,GS45,1.,1.,0.,1.,GS45,1.,1.,1.)
    XLIMB=NLIMB
    COST(4,82,183,GS46,DCORE,1.,0.,1.,XLIMB,GS46/XLIMB,1.,1.)
    COST(3,0,184,0.,1.,1.,0.,1.,1.,1.,1.,1.)

    #ASSEMBLY WINDINGS
    COST(3,79,185,0.,1.,1.,0.,1.,GS41+GS42,1.,1.,1.)

    #WINDING SUPPORT
    if(not(int(GS47)==0)):
        COST(3,83,188,GS47,1.,1.,0.,1.,GS47,1.,1.,1.)
    #ASSEMBLING ACTIVE PART
    if(not BBREAC):
        COST(3,85,190,0.,1.,1.,GG49,1.,GS24,1.,1.,1.)
    else:
        COST(3,86,190,0.,1.,1.,GG49,1.,GS24,1.,1.,1.)

    if(GS48 > 1.E-3):
        COST(3,84,189,GS48,1.,1.,0.,1.,GS48,1.,1.,1.)

    for I in range(1,1+NG):
        if(not(EFKV[I-1]>50)):
            ACM3=1
            COST(4,87,190+I,0.,1.,1.,0.,1.,RCONN[I-1],ACONDA[I-1],ACM3,1.)
            continue
        ACM3=EFKV[I-1]/50
        COST(4,87,190+I,0.,1.,1.,0.,1.,RCONN[I-1],ACONDA[I-1],ACM3,1.)

    COST (3,0,195,0.,1.,1.,0.,1.,1.,1.,1.,1.)
    COST (2,0,196,0.,1.,1.,0.,1.,1.,1.,1.,1.)

