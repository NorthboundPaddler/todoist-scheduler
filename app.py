#app.py
from logging import exception
from config import Config
import requests, os
from flask import Flask, abort, jsonify, session

app = Flask(__name__)


@app.route("/")
def index():
    #simple check to make sure the app spun up OK
    #TODO This can be changed to the main interface (i.e. week view)
    #once it has been built.
    return "todoist-scheduler"

@app.route("/tasks/get/<filter>", methods=['POST'])
def getTasksByFilter(filter):
    return None

@app.before_first_request
def checkSessionForKey():
    if "api_key" not in session.keys():
        #TODO Redirect the user to settings page with key input
        raise Exception("No Todoist API key set - do this now!")

@app.errorhandler(500)
def internalServerError(e):
    #FIXME This does not send the exception to the user
    return jsonify(str(e))

@app.before_first_request
def setSecretKey():
    app.config.SECRET_KEY = os.getenv("todoistschedulersk")
    if app.config.SECRET_KEY is None:
        raise Exception("You must set a SECRET_KEY env variable - do this now!")

if __name__=="__main__":
    app.config.from_object(Config)
    app.run()