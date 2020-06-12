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


#### GET `/user/group/recent`
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


#### POST `/user/group/recent`
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

#### POST `/user/forgot`
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
