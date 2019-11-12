
''' Title:  Determine the corner radius of a conductor '''

def CORN(THICKN):
    if (THICKN < 0.0017): AREA=0.215
    if (THICKN >= 0.0017 and THICKN < 0.0022): AREA=0.36
    if (THICKN >= 0.0022 and THICKN < 0.0037): AREA=0.55
    if (THICKN >= 0.0037): AREA=0.86

    CORN=AREA
    return CORN
