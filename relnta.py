
''' Title:  Calculation of relative turn numbers for :
         1. Linear      regulation
         2. Plus-minus  regulation
         3. Coarse-fine regulation
      In accordance with the tapchangers in TI 5492 0450
      "ZTALWG" gives the relation between the voltage in
      one winding and the voltage of the corresponding
      winding group.
      "PLSPOS","ZERPOS" and "RMIPOS" give the part of the
      regulating winding that is connected in circuit. '''

def RELNTA(ITML,KTYPRW,NLOOPG,NMSTEP,NPSTEP,NXSTEP,
           PLSPOS,PUSTEP,RMIPOS,ZERPOS,ZTALWG,EXTPOS):

    X1=float(NPSTEP[ITML-1]+NMSTEP[ITML-1])
    ''' Reg Type? '''

    ''' Linear '''

    if (KTYPRW[ITML-1] == 1) :
        NLOOPG[ITML-1]=NPSTEP[ITML-1]+NMSTEP[ITML-1]
        ZERPOS[ITML-1]=float(NMSTEP[ITML-1])/X1
        PLSPOS[ITML-1]=1.
        RMIPOS[ITML-1]=0.
        EXTPOS[ITML-1]=float(NXSTEP[ITML-1])/X1
        ZTALWG[1][ITML-1]=X1*PUSTEP[ITML-1]
        ZTALWG[0][ITML-1]=1.-ZERPOS[ITML-1]*ZTALWG[1][ITML-1]
        ZTALWG[2][ITML-1]=0.

        ''' Plus-minus '''

    elif(KTYPRW[ITML-1] == 2) :
        NLOOPG[ITML-1]=2*int((X1+3.1)/4.)
        if (X1<=16.5): NLOOPG[ITML-1]=int((X1+1.1)/2.)
        X1=float(NLOOPG[ITML-1])

        BBL=False
        if ((2.*X1-float(NPSTEP[ITML-1]+NMSTEP[ITML-1]))>1.5):BBL=True
        if (BBL) :
            PLSPOS[ITML-1]=1.-1./X1
        else:
            PLSPOS[ITML-1]=1.
        
        ZERPOS[ITML-1]=PLSPOS[ITML-1]-float(NPSTEP[ITML-1])/X1
    
        RMIPOS[ITML-1]=ZERPOS[ITML-1]-float(NMSTEP[ITML-1])/X1
        EXTPOS[ITML-1]=PLSPOS[ITML-1]-float(NPSTEP[ITML-1]+NMSTEP[ITML-1]-NXSTEP[ITML-1])/X1
        ZTALWG[1][ITML-1]=X1*PUSTEP[ITML-1]
    
        ZTALWG[0][ITML-1]=1.-(ZERPOS[ITML-1])*ZTALWG[1][ITML-1]

        ZTALWG[2][ITML-1]=0.
        ''' Coarse-fine '''

    elif (KTYPRW[ITML-1] == 3) :
        NLOOPG[ITML-1]=int((X1+1.1)/2.)
        X1=float(NLOOPG[ITML-1])
        ZTALWG[1][ITML-1]=X1*PUSTEP[ITML-1]

        if (X1<8.5) :
            X2=1.+X1

        else:
            X2=2.*int((X1+1.1)/2.)
        
        PLSPOS[ITML-1]=1.+float(NMSTEP[ITML-1]+NPSTEP[ITML-1])/X1
        ZTALWG[2][ITML-1]=X2*PUSTEP[ITML-1]
        BBL=False
        if ((X2-X1)>0.5): BBL=True

        ''' Set RMIPOS[ITML] '''

        if (BBL) :
            RMIPOS[ITML-1]=1./X1

        else:
            RMIPOS[ITML-1]=0.

        if (float(NMSTEP[ITML-1])>(X1-0.5)) :
            ZERPOS[ITML-1]=1.+float(NMSTEP[ITML-1])/X1
            ZTALWG[0][ITML-1]=1.-ZTALWG[2][ITML-1]-ZTALWG[1][ITML-1]*(ZERPOS[ITML-1]-2.)

        else:
            ZERPOS[ITML-1]=RMIPOS[ITML-1]+float(NMSTEP[ITML-1])/X1
            ZTALWG[0][ITML-1]=1.-ZERPOS[ITML-1]*ZTALWG[1][ITML-1]

        if (float(NXSTEP[ITML-1])>(X2-0.5)) :
            EXTPOS[ITML-1]=1.+float(NXSTEP[ITML-1])/X1

        else:
            EXTPOS[ITML-1]=RMIPOS[ITML-1]+float(NXSTEP[ITML-1])/X1
    print('relnta ztalwg=',ZTALWG)
    return (NLOOPG,PLSPOS,RMIPOS,ZERPOS,ZTALWG,EXTPOS)
