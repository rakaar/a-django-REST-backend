# Documentation of endpoints related to authentication

#### POST  `/chat/group`
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

#### GET `/chat/group`
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

#### POST `/chat/user`
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

#### PUT `/chat/user`
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

#### GET `/chat/user`
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
