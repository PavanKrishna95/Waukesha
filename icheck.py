
''' Title:  Checks certain limitations for each UDB '''

def ICHECK(Y,JFC):

    TEXT=['Self-cooled 3-phase power exceeds licence limit ' ,
          'Rated 3-phase power exceeds licence limit       ' ,
          'Winding current exceeds licence limit           ' ,
          'Rated voltage exceeds licence limit             ' ,
          'BIL-value exceeds licence limit                 ' ,
          'Licence does not allow use of oil-guiding rings ' ,
          'Licence does not allow use of small-MVA windings' ,
          'Rated 3-phase power is too small                ' ,
          'Rated 1-phase power exceeds limit               ' ,
          'Rated 1-phase power,self-cooled, exceeds limit  ' ,
          'Licence does not allow use of winding supports  ' ,
          'Licence does not allow use of side limbs        ' ,
          'Licence does not allow use of HI-B core-steel   ' ,
          'Licence does not allow use of ASECOND bandage   ' ,
          '                                                ' ,
          '                                                ' ,
          '                                                ' ,
          '                                                ' ,
          '                                                ' ,
          '                                                ' ]

    NUSER,NLIM,MAXC =[20,14,10]

    USER=['ZK','WZA','UAN','UAI','UAW','UAB','UAL']+13*[' ']

    ICLASS=[20 ,  20 ,   1 ,   4 ,   5 ,   6 ,  7  ]+13*[0]

    X=[[1000.,1000.,1.E+8,450.,1550.,4.,2.,-2.5,500.,500.,4.,4.,4.,4.],
       [1000.,1000.,1.E+8,450.,1550.,4.,2.,-2.5,500.,500.,4.,4.,4.,4.],
       [800., 800.,1.E+8,450.,1550.,4.,4.,-2.5,300.,300.,4.,4.,4.,4.],
       [9999.,9999.,1.E+8,800.,2050.,4.,2.,-2.5,9999.,9999.,4.,4.,4.,4.],
       [188., 188.,1.E+8,275.,1050.,4.,2.,-2.5,100.,100.,4.,2.,4.,4.],
       [1000.,1000.,1.E+8,800.,2050.,4.,2.,-2.5,600.,600.,4.,4.,4.,4.],
       [1100.,1100.,1.E+8,550.,1800.,4.,4.,-2.5,1100.,1100.,4.,4.,4.,4.]]
    temp=[[0. for i in range(13)] for j in range(20)]
    X=X+temp
    ''' Determine the user code. '''

    IUSER='ZK'

    BBSTOP=False
    IU=0
    BBHACK=True

    ''' Find the correct user. '''

    for I in range(1,NUSER+1):

        ''' Carry out the checks '''

        ''' For correct user '''

        if(IUSER == USER[I-1]):
            IU=I
            BBHACK=False
            IC=ICLASS[IU-1]

        ''' Check in sequence '''

        ''' If room left in list '''

        if(IC<=MAXC):
            
            ''' For each test '''

            for ITEST in range(1,NLIM+1):

                ''' Check '''

                ''' If limit exceeded '''

                if(Y[ITEST-1]>X[IC-1][ITEST-1]):

                    ''' Print text '''
                    ''' If Y[ITEST]!= 0 '''

                    if(abs(Y[ITEST-1])>1.E-16):
                        BBSTOP=True
                        ''' WRITE (*,802) TEXT(ITEST),Y(ITEST),X(IC,ITEST)
                        WRITE (JFC,802) TEXT(ITEST),Y(ITEST),X(IC,ITEST) '''

    ''' Print warning '''

    ''' If not registered. '''

    if (BBHACK):
        BBSTOP=True
        ''' WRITE(*,800) '*** You are not a registered user *** '
        WRITE(JFC,800) '*** You are not a registered user *** ' '''

    if(BBSTOP): '''' WRITE (*,801) '''

    return BBSTOP

    ''' 800  FORMAT('0',A)
    801  FORMAT(' ',35(/))
    802  FORMAT(' ',A48,/' ','Value = ',F12.1,'  Limit = ',F12.1,/) '''
