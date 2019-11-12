def PAGE01():
    import com as C
    from curdns import CURDNS

    #Calculation of winding currents, current densities & voltages
    CURDNS()

    #       WRITE(JFC,102)'R A T I N G   P L A T E   D A T A: ',
    #     &   '- - - - - - - - - - - - - - - - - - -'
    NLIMB=C.NWOULI
    if(C.BBSLIM): NLIMB=2+C.NWOULI



