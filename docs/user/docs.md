# Documentation of endpoints related to authentication

#### POST  `/user/signup`
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
- { "message": "already exists", "status": 400 } if user is registering with an already existing mail
- { "message": "invalid mail", "status": 400 } if unable to send mail due to wrong email providied


#### GET `/user/verify/<hashed_code>`
On hitting the link in the browser
Responses
- { "message": "success", "status": 201 } if successfully saved in databased
- { "message": ERRORS, "status": 400 } if wrong URL is hit

#### POST `/user/login`
Data to be sent in this format
```
{
  "email": "string@string.com",
  "password": "string"
}
```
Responses
- { "message": "success", "token": TOKEN, "status": 202 } if login successful
- { "message": "invalid creds", "status": 401 } if mail and password do not match

