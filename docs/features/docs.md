# Documentation of endpoints related to features(app)

### GET `/features/learnlists/`
To fetch all the learn lists metadata(excluding resources)
```
[
	{
	 "id": number,
        "person": {
            "name": "string",
            "fb": "string",
			"linkedin": "string",
			"numouno": "string",
            "pic": "string"
        },
        "category": "string",
        "podcast": "string",
        "experiences": [
            "string",
            "string"
        ]
	}
]
```

### GET `/features/learnlist/<id>`
To get complete data of a single learn list
```
{
	 "id": number,
        "person": {
            "name": "string",
            "fb": "string",
			"linkedin": "string",
			"numouno": "string",
            "pic": "string"
        },
        "category": "string",
        "podcast": "string",
        "experiences": [
            "string",
            "string"
        ],
        "resources": [
        	{
	            "title": "string",
	            "link": "string",
	            "level": "string",
	            "tags": "string, string",
	            "description": "string",
	            "cover": "string"
        	}
        ]
	}
```