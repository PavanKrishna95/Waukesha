def FPRINT(IND,BBERR,TEXT2):

    TEXT1=['Note','Error']
    
    
    JFC=TEXT1[IND-1]+':'+TEXT2
    print("{0}:{1}".format(TEXT1[IND-1],TEXT2))
    
    if(IND!=1):
        BBERR=True
        exit()
    return (JFC,BBERR)    

