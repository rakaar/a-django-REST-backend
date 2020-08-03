# Documentation of endpoints related to authentication

#### POST  `/user/signup/`
Data to be sent in this format
```
{
  "name": "string",
  "email": "string@string.com",
  "password_hash": "string",
  "insti_email": "string@string.com"
}
```
Responses
- { "message": "success", "status": 201 } if able to send verification mail
- { "message": "already exists", "status": 409 } if user is registering with an already existing mail
- { "message": "invalid mail", "status": 400 } if unable to send mail due to wrong email providied


#### GET `/user/verify/<hashed_code>/`
On hitting the link in the browser
Responses
- { "message": "success", "status": 201 } if successfully saved in database
- { 'message':'data error', "status": 400 } if wrong URL is hit
- { "message":"mesibo failure", "status": 503 } if Mesibo fails
- { "message": "already exists", "status": 409 } if User already exist
- { "message": 'link expired', "status": 410 } if token/link expired
- { "message": "not subscribed", "status": 201 } if successfully saved in database but not subscribed to NewsLetter

#### POST `/user/login/`
Data to be sent in this format
```
{
  "email": "string@string.com",
  "password": "string"
}
```
Responses
- { "message": "success", "token": TOKEN, "status": 200 } if login successful
- { "message": "invalid creds", "status": 401 } if mail and password do not match


#### GET `/user/group/recent/`
Data to be sent in this format
```
{
  "uid": "string@string.com",
  "gid": integer,
  "mid": integer
}
```
On hitting the endpoint
Response
- { "read_by": ["string@string.com"], "status": 200 } if successful
- { "message": "not found", "status": 400 } if something goes wrong


#### POST `/user/group/recent/`
Data to be sent in this format
```
{
  "uid_reader": "string@string.com",
  "uid": "string@string.com",
  "gid": integer,
  "mid": integer
}
```
On hitting the endpoint
Response
- { "message": "success", "status": 200 } if successful
- { "message": "error", "status": 400 } if something goes wrong

#### POST `/user/forgot/`
Data to be sent in this format
```
{
  "email": "string - empty or string@string.com",
  "password": "string - empty or password",
  "activity": "forgot or update",
  "token": "string - empty or token"
}
```
On hitting the endpoint
Response
- { "message": "success", "status": 200 } if successful
- { "message": "not found", "status": 400 } if user is not registered
- { "message": "invalid email", "status": 400 } if wrong email
- { "message": "token expired", "status": 400 } if token expired
- { "message": "failure", "status": 400 } if failed to update password

#### POST `/user/reset/`
Data to be sent in this format
```
{
  "email": "string - string@string.com",
  "password": "string - empty or password",
  "activity": "token or update",
  "token": "string - token",
  "new_password": "sring - empty or new password"
}
```
On hitting the endpoint
Response
- { "message": "success", "token": "string - token", "status": 200 } if successful
- { "message": "invalid token", "status": 400 } if token is invalid for the given email - for activity = "token"
- { "message": "incorrect password", "status": 401 } if wrong password - for activity = "update"
- { "message": "invalid token", "status": 400 } if token expired/invalid - for activity = "update"
- { "message": "invalid activity", "status": 400 } if activity is neither "update" nor "token"

#### POST `/user/google/`
Data to be sent in this format
```
{
  "code": "string"
}
```
On hitting the endpoint
Response
- { 'token': 'string', 'message': 'string', 'name': 'string', 'email': 'string', "status": 200 } if successful
- { 'message': 'wrong or expired google token', "status": 401 } if token is invalid/expired

#### POST `/user/news_letter/`
Data to be sent in this format
```
{
  "first_name": "string length b/w 3 to 50",
  "email": "string@string.string",
  "custom_fields": {
		"contact": 9111(integer)
	}

}
```
Responses
- { "message": "success", "status": 200 } if successful
- { 'message': 'invalid email', "status": 400 } if mail is invalid
- { 'message': 'bad data', "status": 400 } if user could not be added to subscribers list
- { 'message': 'server error', "status": 500 } if issue with sendgrid
