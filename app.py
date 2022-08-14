#app.py
from logging import exception
from config import Config
import requests, os
from flask import Flask, abort, jsonify, session, render_template, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    #simple check to make sure the app spun up OK
    #TODO This can be changed to the main interface (i.e. week view)
    #once it has been built.
    return render_template("index.html")

@app.route("/settings")
def settings():
    return render_template("settings.html")

@app.route("/tasks/get/<filter>", methods=['POST'])
def getTasksByFilter(filter):
    return None

@app.before_first_request
def checkSessionForKey():
    # Check for the secret key
    TSSK = os.getenv("TSSK")
    app.config.SECRET_KEY = TSSK
    if TSSK is None:
        raise Exception("You must set a SECRET_KEY env variable - do this now!")
    
    # Send the user to settings if they dont have their API key entered yet. 
    if "api_key" not in session.keys():
        #FIXME This does not detect a blank key in my initial tests
        return redirect(url_for("settings"))

@app.errorhandler(500)
def internalServerError(e):
    #FIXME This does not send the exception to the user, just the 500 err message
    return jsonify(str(e))


if __name__=="__main__":
    app.config.from_object(Config)
    app.run()