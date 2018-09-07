def string_clean(x):
    '''
    Cleans location strings and converts names into a standard format.
    Input TwtLoc variable.
    '''
    x = x.replace('AT ','')
    x = x.replace(' AS OF','')
    x = x.replace('TIRE ', '')
    x = x.replace('F/O','FLYOVER')
    x = x.replace(' FO ',' FLYOVER ')
    x = x.replace('AVE ','AVE. ')
    x = x.replace('AVE,','AVE.')
    x = x.replace(' AVENUE ','AVE.')
    x = x.replace('BLVD','BLVD.')
    x = x.replace(' BOULEVARD ',' BLVD. ')
    x = x.replace(' SCT ',' SCT. ')
    x = x.replace('COR','')
    x = x.replace('..','.')
    x = x.replace('COR.','')
    x = x.replace('OLD BALARA','MATANDANG BALARA')
    x = x.replace('SGT.ESGUERRA','SGT. ESGUERRA')
    x = x.replace('SVC.','SERVICE')
    x = x.replace(' SVC ',' SERVICE ')
    x = x.replace('P.TUAZON','P. TUAZON')
    x = x.replace('B.SERRANO','B. SERRANO')
    x = x.replace('MC ARTHUR','MCARTHUR')
    x = x.replace('P TUAZON','P. TUAZON')
    x = x.replace('C.P','C.P.')
    x = x.replace(' CP ',' C.P. ')
    x = x.replace('HI-WAY','HIGHWAY')
    x = x.replace('ROBINSON','ROBINSONS')
    return x
