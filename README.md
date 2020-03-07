# restful-stock-api
A RESTful Stock API that is deployed to Heroku.
The Procfile has one line "web gunicorn app:app" which starts the gunicorn server on Heroku.

## Available Scripts

cd to the root directory to be able to run the following scrips:

### `python app.py`

Run the server locally for testing purposes.

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

Loads the .env and server locally so you can test your config vars.









