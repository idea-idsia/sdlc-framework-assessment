from flask import Flask, render_template, request
from socketio import SocketIO, Signal

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    print(f"Received message: {data}")

if __name__ == '__main__':
    socketio.run(app, debug=True)