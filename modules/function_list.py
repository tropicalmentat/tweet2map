def location_string_clean(twt_location):
    twt_location = twt_location.replace(' AT ', '')
    twt_location = twt_location.replace(' IN FRONT OF ', ' ')
    twt_location = twt_location.replace(' TOWARDS ', ' ')
    twt_location = twt_location.replace(' GOING ', ' ')
    twt_location = twt_location.replace(' COMMONWEALTH, ', ' COMMONWEALTH ')
    twt_location = twt_location.replace(' COMMO ', ' COMMONWEALTH ')
    twt_location = twt_location.replace(' AFTER ', ' ')
    twt_location = twt_location.replace(' AS OF', '')
    twt_location = twt_location.replace('TIRE ', '')
    twt_location = twt_location.replace('F/O', 'FLYOVER')
    twt_location = twt_location.replace(' FO ', ' FLYOVER ')
    twt_location = twt_location.replace(' AVE ', ' AVE. ')
    twt_location = twt_location.replace('AVE,', 'AVE.')
    twt_location = twt_location.replace(' AVENUE ', ' AVE. ')
    twt_location = twt_location.replace('BLVD', 'BLVD.')
    twt_location = twt_location.replace(' BOULEVARD ', ' BLVD. ')
    twt_location = twt_location.replace(' SCT ', ' SCT. ')
    twt_location = twt_location.replace(', ', ' ')
    twt_location = twt_location.replace(',', '')
    twt_location = twt_location.replace(' OLD BALARA ', ' MATANDANG BALARA ')
    twt_location = twt_location.replace('SGT.ESGUERRA', 'SGT. ESGUERRA')
    twt_location = twt_location.replace('SVC.', 'SERVICE')
    twt_location = twt_location.replace(' SVC ', ' SERVICE ')
    twt_location = twt_location.replace('P.TUAZON', 'P. TUAZON')
    twt_location = twt_location.replace(' A BONI ', ' A BONIFACIO ')
    twt_location = twt_location.replace(' A.BONIFACIO ', ' A BONIFACIO ')
    twt_location = twt_location.replace(' A. BONI ', ' A BONIFACIO ')
    twt_location = twt_location.replace('P.OCAMPO', 'P. OCAMPO')
    twt_location = twt_location.replace('B.SERRANO', 'B. SERRANO')
    twt_location = twt_location.replace('BONI SERRANO', 'B. SERRANO')
    twt_location = twt_location.replace('BONNI SERRANO', 'B. SERRANO')
    twt_location = twt_location.replace(' T.SORA ', ' TANDANG SORA ')
    twt_location = twt_location.replace(' T. SORA ', ' TANDANG SORA ')
    twt_location = twt_location.replace('MC ARTHUR', 'MCARTHUR')
    twt_location = twt_location.replace(' MHW ', ' MARCOS HIGHWAY ')
    twt_location = twt_location.replace(' RMB ', ' RAMON MAGSAYSAY BLVD ')
    twt_location = twt_location.replace('P TUAZON', 'P. TUAZON')
    twt_location = twt_location.replace(' C-5 ', ' C5 ')
    twt_location = twt_location.replace(' C-3 ', ' C3 ')
    twt_location = twt_location.replace('C.P ', 'C.P. ')
    twt_location = twt_location.replace(' CP ', ' C.P. ')
    twt_location = twt_location.replace(' CP. ', ' C.P. ')
    twt_location = twt_location.replace('HI-WAY ', 'HIGHWAY ')
    twt_location = twt_location.replace('ROBINSON ', 'ROBINSONS ')
    twt_location = twt_location.replace(' CORNER ', ' ')
    twt_location = twt_location.replace(' COR ', ' ')
    twt_location = twt_location.replace(' COR. ', ' ')
    twt_location = twt_location.replace(' FRONTING ', ' ')
    twt_location = twt_location.replace(' INFRONT OF ', ' ')
    twt_location = twt_location.replace(' INFRONT ', ' ')
    twt_location = twt_location.replace(' IN FRONT OF ', ' ')
    twt_location = twt_location.replace(' FRONT OF ', ' ')
    twt_location = twt_location.replace(' BEFORE ', ' ')
    twt_location = twt_location.replace(' AFTER ', ' ')
    twt_location = twt_location.replace('AFTER ', '')
    twt_location = twt_location.replace(' GOING ', ' ')
    twt_location = twt_location.replace(' SPLIT ', ' ')
    twt_location = twt_location.replace(' INTERSECTION ', ' ')
    twt_location = twt_location.replace(' INTERSECTION', ' ')
    twt_location = twt_location.replace(' INT. ', ' ')
    twt_location = twt_location.replace(' INT ', ' ')
    twt_location = twt_location.replace(' INT', ' ')
    twt_location = twt_location.replace(' APPROACHING ', ' ')
    twt_location = twt_location.replace('  ', ' ')
    twt_location = twt_location.replace('..', '.')
    twt_location = twt_location.replace(' U-TURN SLOT ', ' UTS ')
    twt_location = twt_location.replace(' U-TURN ', ' UTS ')
    twt_location = twt_location.replace(' U-TURN', ' UTS')
    twt_location = twt_location.replace(' SVC ', ' SVC. ')
    twt_location = twt_location.replace(' RD. ', ' ROAD ')
    twt_location = twt_location.replace(' SERVICE ROAD ', ' ')
    twt_location = twt_location.replace(' SVC. ROAD ', ' ')
    twt_location = twt_location.replace('\n', ' ')
    twt_location = twt_location.replace('. ', ' ')
    twt_location = twt_location.replace('.', '')
    twt_location = twt_location.replace('  ', ' ')
    return twt_location


def tweepy_tokens(file, consumer_key, consumer_secret, access_token, access_secret):

    from configparser import ConfigParser

    parser = ConfigParser()
    parser.read(file)
    parser.sections()
    consumer_key = parser.get('tweepy', 'consumer_key')
    consumer_secret = parser.get('tweepy', 'consumer_secret')
    access_token = parser.get('tweepy', 'access_token')
    access_secret = parser.get('tweepy', 'access_secret')
    return consumer_key, consumer_secret, access_token, access_secret