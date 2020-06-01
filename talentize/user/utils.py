import jwt

SECRET_KEY_FOR_JWT = 'SECRET_KEY'

MESIBO_APP_ID = "8117"
MESIBO_APPTOKEN = 'q6qk2jt17bu19y0nbscbl7l51g9jfo3gufuoxizctlfhh0fs2ggqolzlr10uf5dh'


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
