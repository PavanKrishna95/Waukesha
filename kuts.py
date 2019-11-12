''' Printing of the costmatrix. '''

def KUTS(JFC,NLIND,IDENT,DATE,IPAGE,RUB,BBFINE,CONVAR,TCEPOX):
    import common as CM
    
    IRAD=99
    for I in range(1,NLIND+1):
        if(CONVAR[I-1] == 'YES'):
            CM.LTEXT[0]=' Cond. Copper Varnish   3'
        else:
            CM.LTEXT[0]=' Conductor Copper       3'
    
        if(TCEPOX[I-1] == 'YES'):
            CM.LTEXT[2]=' Cond. Transp. Epoxy    3'
        else:
            CM.LTEXT[2]=' Conductor Transposed   3'

        for J in range(1,19):
            K=J+(I-1)*19
            ''' RPRINT(JFC,IDENT,DATE,IPAGE,IRAD,RUB,BBFINE,
                   CM.LTEXT[J-1],CM.RES1[K-1],CM.RES2[K-1],CM.RES3[K-1],CM.RES4[K-1],CM.RES5[K-1],
                   CM.RES6[K-1])'''

        K=K+1
        ''' RPRINT(JFC,IDENT,DATE,IPAGE,IRAD,RUB,BBFINE,
               CM.LTEXT[18+I-1],CM.RES1[K-1],CM.RES2[K-1],CM.RES3[K-1],CM.RES4[K-1],CM.RES5[K-1],CM.RES6[K-1]) '''

    for K in range(27,116):
        K126= K+126
        '''RPRINT(JFC,IDENT,DATE,IPAGE,IRAD,RUB,BBFINE,
               CM.LTEXT[K-1],CM.RES1[K126-1],CM.RES2[K126-1],CM.RES3[K126-1],
               CM.RES4(K126),CM.RES5(K126),CM.RES6(K126-1])'''
 
    return
