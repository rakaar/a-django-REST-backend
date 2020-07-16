import os
import jwt
from datetime import datetime

SECRET_KEY_FOR_JWT = os.environ.get('SECRET_FOR_JWT')

MESIBO_APP_ID = "8117"
MESIBO_APPTOKEN = os.environ.get('MESIBO_APP_TOKEN')

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
    current_time =  str(datetime.now().timestamp()).split('.')[0]
    
    # fmt = '%Y-%m-%d %H:%M:%S'
    # token_time = datetime.strptime(token_time, fmt)
    # current_time = datetime.strptime(current_time, fmt)
    
    time_difference = int(current_time) - int(token_time)
    time_difference_in_mins = time_difference/60
    return time_difference_in_mins < mins




    
