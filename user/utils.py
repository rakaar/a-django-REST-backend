import jwt
from datetime import datetime
SECRET_KEY_FOR_JWT = 'SECRET_KEY'

MESIBO_APP_ID = "8117"
MESIBO_APPTOKEN = 'q6qk2jt17bu19y0nbscbl7l51g9jfo3gufuoxizctlfhh0fs2ggqolzlr10uf5dh'
YOUTUBE_API_ACCESS_KEY = 'AIzaSyBGq_zgNyrZRMAGq300lxKyUTCmcQRm9iw'

def check_token(email, token):
    '''
    Utility function to verify email with email encoded in token
    Args:
        email(str): email of the user
        token(str): token received after login
    Returns:
        True, if verification is successful afer decoding the token, False otherwise
    '''
    decode_obj = jwt.decode(token, SECRET_KEY_FOR_JWT, algorithms=['HS256'])
    return decode_obj['email'] == email


def is_token_valid(token, mins):
    '''
    Utility function to check if token is  expired or not
    Args:
        token(str): token from frontend
    Returns:
        True, if token is valid. False otherwise
    '''

    decode_obj = jwt.decode(token, SECRET_KEY_FOR_JWT, algorithms=['HS256'])
    token_time = decode_obj['random']
    token_time = token_time.split('.')[0]
    current_time =  str(datetime.now()).split('.')[0]
    
    fmt = '%Y-%m-%d %H:%M:%S'
    token_time = datetime.strptime(token_time, fmt)
    current_time = datetime.strptime(current_time, fmt)
    
    time_difference = current_time - token_time
    time_difference_in_mins = time_difference.total_seconds()/60
    return time_difference_in_mins < mins




    