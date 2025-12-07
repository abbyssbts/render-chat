from flask import Flask, render_template, request
from flask_socketio import SocketIO, send

app = Flask(__name__)
# allow cross-origin so clients can connect
socketio = SocketIO(app, async_mode='eventlet', cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

# simple broadcast handler
@socketio.on('message')
def on_message(msg):
    # optional: attach sender ip/username if you add that feature
    print("Received message:", msg)
    send(msg, broadcast=True)

if __name__ == '__main__':
    # Local debug only. Render/production will use gunicorn + eventlet.
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
