
''' Title:  Print an error message relating to
            the automatic winding layout
            The message will appear only twice '''

def WMESS(JFC,TEXT,NWARN):

    CTIMES =['First ','Second']

    NWARN=NWARN+1
    if(NWARN <= 2) :
        ''' WRITE (*,2) CTIMES(NWARN),TEXT '''
        ''' WRITE (JFC,2) CTIMES(NWARN),TEXT '''
    elif(NWARN == 2):
        ''' WRITE (*,3) '''
        ''' WRITE (JFC,3) '''
    
    return
