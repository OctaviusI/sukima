### Using the app

0. Navigate to the apps `/docs` endpoint (usually found at http://0.0.0.0:8000/docs). Alternatively, if for some reason that is not possible, you can send curl requests to the app.
1. Register an user. Make sure to set the ``permission_level`` to a value greater than 0 and give it a username/password combination.
2. Generate a token. Input the username/password but leave all other fields blank.
3. Log into the app by using the `Authorize` button, using your username/password.
4. Load you first model. For the purposes of debugging you may want to use a smaller model like `hakurei/gpt-j-random-tinier` (for testing only) or `iokru/c1-1.3B` (one of the smallest 'coherent' models).
5. After the model's loading has been completed, use the `Get model list` function to check if your model is in the database and flagged as `ready`.
6. Use the `generate` function to test the model. Make sure to set the correct values for the `model` you have loaded, as well as add some text that you want the bot to reply to in the `prompt` value.