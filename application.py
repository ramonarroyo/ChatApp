import pusher
from flask import Flask, render_template, request, jsonify
from settings import APP_ID, APP_KEY, SECRET

app = Flask(__name__)

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

