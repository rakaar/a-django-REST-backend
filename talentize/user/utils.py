import jwt

SECRET_KEY_FOR_JWT = 'SECRET_KEY'


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
