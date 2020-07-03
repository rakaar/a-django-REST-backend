#### Deployed at https://api.numouno.tech/

### Installation and setup
- Create a virtual environment using venv
`python3 -m venv env`
- Activate it
`source env/bin/activate`
- Install packages
`pip install -r requirements.txt`
- Move to the directory containing manage.py and start server
`python manage.py runserver`

### DB Migrations
After change in models(adding, updating), migration should be performed
- Run *makemigrations* and a new file is generated inside Migrations folder
`python manage.py makemigrations APP_NAME`
- Apply those and get OK repsonse on terminal
`python manage.py migrate`
