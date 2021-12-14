### Running in local:

`git clone https://github.com/dashgin/CarParkAPI && cd CarParkAPI`
`python3 -m venv venv`
`source venv/bin/activate`
`pip install -r requirements.txt`
`python manage.py migrate && python manage.py createsuperuser`
`python3 manage.py runserver`
> then visit [localhost:8000/admin/](http://localhost:8000/admin/)

### Deploying to Heroku:

> Prerequisites: <br/>
> python and heroku account(it is free)

+ fork this repo
+ then clone it to your local 
+ create these files in root directory of project
+ `Procfile` with content: `web: python manage.py collectstatic --no-input; gunicorn config.wsgi --log-file - --log-level debug`
+ `runtime.txt` with content: `python=3.9.9`
+ then create new app on heroku 
+ go to settings tab of app and add `python` as a runtime
+ go to `settings` tab of app and add these config vars:
+ `DJANGO_SETTINGS_MODULE=config.settings.production`
+ `SECRET_KEY=<random string>`
+ `ALLOWED_HOSTS=<your_app_name>.herokuapp.com,localhost`
+ `DISABLE_COLLECTSTATIC=1`
+ then go to `deploy` tab of app and select use GitHub
+ then connect your app repo to your forked GitHub repo
+ and finally deploy your repo to Heroku
