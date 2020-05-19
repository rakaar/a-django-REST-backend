import jwt

SECRET_KEY_FOR_JWT = 'SECRET_KEY'


def check_token(email, token):
    '''
    utility function to verify 
        email with email encoded in token
    '''
    decode_obj = jwt.decode(token, SECRET_KEY_FOR_JWT, algorithms=['HS256'])
    return decode_obj['email'] == email
