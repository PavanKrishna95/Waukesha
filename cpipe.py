def CPIPE(BBPRNT,JFC,GS81, GS91, GS92, GS102,
          GG81,GG83,GG91,GG92,GG94,GG101,GG102):
    from cost import COST
    SP1='       '
    SP='          '
    if(BBPRNT):
        #WRITE(JFC,*) '===== INPUT DATA TO CPIPE                    ====='
        #WRITE(JFC,*) SP1,'GS81 ',SP,'GS91 ',SP,'GS92 ',SP,'GS102'
        #WRITE(JFC,*) GS81,GS91,GS92,GS102
        #WRITE(JFC,*) SP1,'GG81  ',SP,'GG83  ',SP,'GG91  ',SP,'GG92  '
        #WRITE(JFC,*) GG81,GG83,GG91,GG92
        #WRITE(JFC,*) SP1,'GG94  ',SP,'GG101 ',SP,'GG102 '
        #WRITE(JFC,*) GG94,GG101,GG102
        pass
    COST(3,116,214,GS81,1.,1.,GG81,1.,GS81+GG81+GG83,1.,1.,1.)
    COST(3,117,215,0.,1.,1.,0.,1.,GS81+GG81+GG83,1.,1.,1.)
    COST(3,118,216,0.,1.,1.,GG83,1.,GS81+GG81+GG83,1.,1.,1.)
    COST(2,0,217,0.,1.,1.,0.,1.,1.,1.,1.,1.)    


    COST(3,120,218,GS91,1.,1.,GG91,1.,GS91+GG91,1.,1.,1.)
    if(not(int(GS92)==0)):
        COST(3,121,219,GS92,1.,1.,GG92,1.,GS92+GG92,1.,1.,1.)

    COST(3,122,220,0.,1.,1.,0.,1.,GS91+GG91+GS92+GG92+GG94,1.,1.,1.)
    COST(3,123,221,0.,1.,1.,GG94,1.,GS91+GG91+GS92+GG92+GG94,1.,1.,1.)
    COST(2,0,222,0.,1.,1.,0.,1.,1.,1.,1.,1.)

    COST(3,125,223,0.,1.,1.,GG101,1.,1.,1.,1.,1.)
    COST(3,127,225,GS102,1.,1.,GG102,1.,GS102,1.,1.,1.)
    COST(2,0,226,0.,1.,1.,0.,1.,1.,1.,1.,1.)
