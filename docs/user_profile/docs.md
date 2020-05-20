# Endpoints for Profile Updation

#### GET `/profile` (To get the complete profile details of a user)
Data to be sent in this format
```
{
  "email": "string@string.com",
  "token": "string"
}
```
Responses
- { profile, "status": 200 } if everything is fine
- { "message": "invalid token", "status": 400 } if token is invalid
- { "message": "invalid user", "status": 401 } if user is not found in database

#### POST `/profile/education` (To update education details in the profile)
Data to be sent in this format
```
{
  "email": "string@string.com",
  "token": "string",
  "education": {
    "colleges": [
      {
      "name": "string",
      "cgpa_range": "string",
      "dept": "string",
      "core_courses": [
        {
          "name": "string"
        },
        {
          "name": "string"
        }
      ],
      "additional_courses": [
        {
          "name": "string"
        },
        {
          "name": "string"
        }
      ],
      "type_of_degree": "string"
    },
    {
      "name": "string",
      "cgpa_range": "string",
      "dept": "string",
      "core_courses": [
        {
          "name": "string"
        },
        {
          "name": "string"
        }
      ],
      "additional_courses": [
        {
          "name": "string"
        },
        {
          "name": "string"
        }
      ],
      "type_of_degree": "string"
    }
    ],
    "school": {
      "name": "string",
      "board": "string",
      "percentage": "string"
    },
    "online_courses": [
      {
        "name": "string",
        "company": "string",
        "partner_insti": "string"
      },
      {
        "name": "string",
        "company": "string",
        "partner_insti": "string"
      }
    ]
  }
}
```
Responses
- { "message": "success", "status": 200 } if everything is fine
- { "message": "invalid token", "status": 400 } if token is not right
- { "message": "invalid user", "status": 401 } if user not found in Database

#### POST `/profile/experience` (To update experience details in the profile)
Data to be sent in this format
```
{
  "email": "string@string.com",
  "token": "string",
  "experience": {
    "prev_interns": [
      {
        "company": "string",
        "job_title": "string",
        "from_date": "string",
        "to_date": "string",
        "nature": "string"
      }
    ],
    "projects": [
      {
        "project_type": "string",
        "title": "string",
        "description": "string",
        "associated_info": "string"
      }
    ],
    "por": [
      {
        "place": "string",
        "positions": [
          {
            "year": "string",
            "description": "string"
          },
          {
            "year": "string",
            "description": "string"
          }
        ]
      }
    ],
    "research_papers": [
      {
        "journal": "string",
        "title": "string",
        "description": "string",
        "num_of_people": 2,
        "is_main": 1,
        "name_of_main": "string"
      }
    ],
    "patents": [
      {
        "title": "string",
        "description": "string",
        "date": "string"
      }
    ]
  }
}
```
Responses
- { "message": "success", "status": 200 } if everything is fine
- { "message": "invalid token", "status": 400 } if token is not right
- { "message": "invalid user", "status": 401 } if user not found in Database

#### POST `profile/achs` (To update personal details in the profile)
Data to be sent in this format
```
{
  "email": "string@string.com",
  "token": "string",
  "achs": {
    "competitions": [
      {
        "title": "string",
        "description": "string",
        "date": "string",
        "issuing_auth": "string"
      }
    ],
    "certifications": [
      {
        "name": "string",
        "description": "string",
        "year": "string",
        "issuing_auth": "string"
      }
    ]
  }
}
```

Responses
- { "message": "success", "status": 200 } if everything is fine
- { "message": "invalid token", "status": 400 } if token is not right
- { "message": "invalid user", "status": 401 } if user not found in Data

#### POST `/profile/personal`
Data to be sent in this format
```
{
  "email": "string@string.com",
  "token": "string",
  "personal": {
    "skills": [
      {
        "name": "string"
      }
    ],
    "location": "string",
    "bio": "string"
  }
}
```
Responses
- { "message": "success", "status": 200 } if everything is fine
- { "message": "invalid token", "status": 400 } if token is not right
- { "message": "invalid user", "status": 401 } if user not found in Data
