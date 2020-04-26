# restful-stock-api
A RESTful Stock API that is deployed to Heroku.
The Procfile has one line "web gunicorn app:app" which starts the gunicorn server on Heroku.

## Database

This API is using SQLAlchemy with MySQL in order to save JSON strings for queries. This functionality was added in order to save a lot of
data to use for Machine Learning. The pooling recycle rate is set to 20 because of MySQL host limitations (if your host has a different wait_timeout setting you can modify the pooling recycle value to be just below it). In order to find out the timeout of your MySQL host run: 

```
SHOW SESSION VARIABLES LIKE 'wait_timeout';
```

## Available Scripts

cd to the root directory to be able to run the following scrips:

### `python app.py`

Run the server locally for testing purposes. You should use heroku local over this.

### `source venv/bin/activate`

Activate the python virtual environment.

### `git push heroku master`

Push the code to Heroku directly. This can also be performed on Heroku by deploying the Github master branch on the website.

### `heroku config:set API_KEY=<value>`

Set config vars like api keys by using this command

You can then get the config values in the code like this:

```
import os

api_key = os.environ.get('API_KEY', None)
```

### `heroku local`

Loads the .env and server locally so you can test your config vars. This is the default way to test the API locally.
This starts a server at http://127.0.0.1:5000/ by default.









