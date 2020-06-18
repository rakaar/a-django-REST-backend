# Documentation of endpoints related to authentication

#### POST  `/chat/group/`
Data to be sent in this format
```
{
  "name": "string",
  "flag": 0,
  "active": 1
}
```
Responses
- { "message": "success", "gid": gid, "name": name } if group created successfully
- { "message": "failure", "status": 400 } if failed to create groups

#### GET `/chat/group/`
Returns all  email of users of the group
GET request to be sent in this format
```
{
    "gid": integer
}
```
Response
- { "users": ["string1@string1.com", "string2@string2.com" ]} if fetch is succcessful
- { "message" : "not found" } if wrong group id is mentioned

#### POST `/chat/user/`
Data to be sent in this format
```
{
  "gid": integer,
  "m" : "string@string.com"
}
```
Responses
- { "message": "success" } if user added to group successfully
- { "message": "failure", "status": 400 } otherwise

#### PUT `/chat/user/`
Data to be sent in this format
```
{
  "gid": integer,
  "m" : "string@string.com"
}
```
Responses
- { "message": "success" } if user added to group successfully
- { "message": "failure", "status": 400 } otherwise

#### GET `/chat/user/`
Returns all  groups of the user
GET request to be sent with this body
```
{
    "email": "string@string.com"
}
```
Response
- { "groups": [[gid1, active_status_1], [integer, bool], [675, true]]} if fetch is succcessful
- { "message" : "not found" } if wrong user email is recieved 

#### POST  `/chat/complaint/`
Data to be sent in this format
```
{
  "complaint_by": "string@string.string",
  "complaint_on": "string@string.string",
  "gid": integer
}
```
Responses
- { "message": "success", "status": 200} if complaint emailed successfully
- { "message": "invalid email", "status": 400 } if either failed to find users with the given emails
- { "message": "failed to send mail", "status": 400 } if it fails to send mail due to SMTP or an unknown error
- { "message": "invalid group", "status": 400 } if failed to find group with the given gid

#### POST  `/chat/refer/`
Data to be sent in this format
```
{
  "refered_msg": integer,
  "refered_by": integer,
  "gid": integer
}
```
Responses
- { "message": "success", "status": 200} if reference recorded successfully
- { "message": "failure", "status": 500 } if request failed due to unknown reason

#### GET `/chat/refer/`
Returns all  groups of the user
GET request to be sent with this body
```
{
    "gid": integer
}
```
Response
- { "data": [ {integer: ["string"]} ] } if fetch is succcessful
- { "message" : "invalid gid" } if wrong gid is sent

