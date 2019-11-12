from cost import COST
def CTANK(BBPRNT,JFC,NTANK,ACOV,TANKDI,KODRAD,NRAD,RSEK,\
               NCEQ,GS51,GS52,GS53,GS61,GS71,GS72,GG151,GG152,\
                      GG51,GG52,GG54,GG55,GG61,GG63,GG71,GG72,GG74):
    
    SP1='       '
    SP='          '
    if(BBPRNT):
        #WRITE(JFC,*) '===== INPUT DATA TO CTANK                    ====='
        #WRITE(JFC,*) SP1,'NTANK ',SP,'ACOV  ',SP,'TANKDI',SP,'KODRAD'
        #WRITE(JFC,*) NTANK,ACOV,TANKDI,KODRAD
        #WRITE(JFC,*) SP1,'NRAD  ',SP,'RSEK  ',SP,'NCEQ  ',SP,'GS51 '
        #WRITE(JFC,*) NRAD,RSEK,NCEQ,GS51
        #WRITE(JFC,*) SP1,'GS52 ',SP,'GS53 ',SP,'GS61 ',SP,'GS71 '
        #WRITE(JFC,*) GS52,GS53,GS61,GS71
        #WRITE(JFC,*) SP1,'GS72 ',SP,'GG151 ',SP,'GG152 ',SP,'GG51  '
        #WRITE(JFC,*) GS72,GG151,GG152,GG51
        #WRITE(JFC,*) SP1,'GG52  ',SP,'GG54  ',SP,'GG55  ',SP,'GG61  '
        #WRITE(JFC,*) GG52,GG54,GG55,GG61
        #WRITE(JFC,*) SP1,'GG63  ',SP,'GG71  ',SP,'GG72  ',SP,'GG74  '
        #WRITE(JFC,*) GG63,GG71,GG72,GG74
        pass
    IX=87+NTANK

    COST (4,IX,197,GS51,ACOV,1.,GG51,1.,TANKDI,1.,1.,1.)

    COST (4,96,198,GS52,1.,1.,GG52,1.,GS52+GG52,1.,1.,1.)

    COST (4,97,199,0.,1.,1.,0.,1.,GS51+GG51+GS52+GG52,1.,1.,1.)
    BBHELP = (GS53 > 0.1)

    if(not BBHELP):
        COST(3,0,200,0.,1.,1.,0.,1.,1.,1.,1.,1.)
    else:
        COST(3,124,200,GS53,1.,1.,0.,1.,GS53,1.,1.,1.)

    IX = 97 + KODRAD    
    COST (3,IX,201,0.,1.,1.,GG54,RSEK,1.,1.,1.,1.)
    COST (4,103,202,0.,1.,1.,GG55,1.,\
        GS51+GG51+GS52+GG52+GG54+GG55, 1.,1.,1.)
    if(NCEQ==4):
        COST (4,119,202,0.,1.,1.,0.,1.,GG151+GG152,1.,1.,1.)
    COST (3,0,202,0.,1.,1.,0.,1.,1.,1.,1.,1.)
    COST (2,0,203,0.,1.,1.,0.,1.,1.,1.,1.,1.)

    #COVER COSTS
    if(NTANK>=3 and NTANK<=6): IX=110
    if(NTANK<=2 or NTANK ==7):IX=111
    if(NTANK==8): IX=112

    COST (4,IX,208,GS71,1.,1.,GG71,1.,GS71+GG71,1.,1.,1.)
    COST (4,113,209,GS72,1.,1.,GG72,1.,GS72+GG72,1.,1.,1.)
    COST (4,114,210,0.,1.,1.,0.,1.,GS71+GG71+GS72+GG72,\
            1., 1., 1.)
    COST (3,0,211,0.,1.,1.,0.,1.,1.,1.,1.,1.)
    COST (3,115,212,0.,1.,1.,GG74,1.,GS71+GG71+GS72+GG72+GG74,\
               1.,1.,1.)
    COST (2,0,213,0.,1.,1.,0.,1.,1.,1.,1.,1.)

    #COSTS  COOLING EQUIPMENT

    if((NCEQ==3 or NCEQ==5)):
        IX=102+NCEQ
        COST (3,IX,204,GS61,1.,1.,GG61,1.,GS61+GG61+GG63,1.,1.,1.)
        COST (3,108,205,0.,1.,1.,0.,1.,GS61+GG61+GG63,1.,1.,1.)
        COST (3,109,206,0.,1.,1.,GG63,1.,GS61+GG61+GG63,1.,1.,1.)
        COST (2,0,207,0.,1.,1.,0.,1.,1.,1.,1.,1.)
    COST (2,0,207,0.,1.,1.,0.,1.,1.,1.,1.,1.)    

