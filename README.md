# Getting Started

First create a new account, new database in mongodb altas cloud and get the connection string, use this [video](https://www.youtube.com/watch?v=jzZwarOxNCA) as reference. Add your connection string to `app.config["MONGO_URI"]` in `app.py`

## Step 1

Open up windows powershell as Administrator, navigate to `your\path\to\flask-api-boilerplate`

`cd your\path\to\flask-api-boilerplate`

## Step 2

Execute `python -m venv env` to create a python virtual environment wait until it is created.

Execute `.\env\Scripts\activate` to activate virtual environment (if Powershell gives you an error as `“execution of scripts is disabled on this system.”`, run this command first -> `Set-ExecutionPolicy RemoteSigned`)

Execute `pip install -r .\requirements.txt` to install requirements

## Step 3

Execute `flask run` to start application. (or executing  `python .\app.py` should also work)

While doing this if you run into a error like `"Error: Could not locate flask application. You did not provide the FLASK_APP environment variable"`, execute this command first -> `$env:FLASK_APP = "run.py"`

## Step 4 (Test POST Method)

Open up [postman](https://chrome.google.com/webstore/detail/tabbed-postman-rest-clien/coohjcphdfgbiolnekdpbcijmhambjff?hl=en) and send `POST` request to `http://127.0.0.1:5000/query` with `Json` body as,

```
{
    "queryId": 90030072,
    "field1": "example1",
    "field2": "example2",
    "field3": "example3"
}
```
If everyting is configured properly, you should get a `201` responce,
```
{
    "message": "Query added successfully",
    "query": 90030072
}
```
## Step 5 (Test GET Method)

Now let's retrieve the record we just added. Sent a `GET` request to `http://127.0.0.1:5000/get/90030072`, if everything is configured properly you should get,
```
[
    {
        "field1": "example1",
        "field2": "example2",
        "field3": "example3"
    }
]
```
## Step 6 (Deploy)

Create an account on [Heroku](https://signup.heroku.com/login) and download and install [Hiroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

Execute command `heroku login` and enter credentials to login to Hiroku CLI.

Execute command `heroku create your-app-name` to create a new application. (https://your-app-name.hirokuapp.com will be your URL)



