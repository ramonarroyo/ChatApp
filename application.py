import os
import pusher
from flask import Flask, render_template, request, jsonify
# from config import APP_ID, APP_KEY, SECRET

app = Flask(__name__)

# Get from environment when hosting on Heroku
APP_ID = os.environ.get('APP_ID')
APP_KEY = os.environ.get('APP_KEY')
SECRET = os.environ.get('SECRET')

pusher_client = pusher.Pusher(
  app_id=APP_ID,
  key=APP_KEY,
  secret=SECRET,
  cluster='us2',
  ssl=True
)


@app.route("/")
def index():
    return render_template("index.html", key=APP_KEY)


@app.route("/message", methods=["POST"])
def message():

    try:
        username = request.form.get("username")
        message = request.form.get("message")

        pusher_client.trigger('chat-channel', 'new-message', {'username': username, 'message': message})

        return jsonify({'result' : 'success'})

    except:
        return jsonify({'result': 'failure'})

