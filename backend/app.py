from flask import Flask, request, jsonify
from flask_cors import CORS
import time
from threading import Lock

app = Flask(__name__)
CORS(app)

queue = []
lock = Lock()

class DelayedTask:
    def __init__(self, task, delay):
        self.task = task
        self.delay = delay
        self.timestamp = time.time() + delay

    def to_dict(self):
        return {'task': self.task, 'delay': self.delay, 'timestamp': self.timestamp}

@app.route('/')
def home_page():
    return"<h1>The Backend System is UP. </h1>"

#function to add the task in the queue List
@app.route('/add_task', methods=['POST'])
def add_task():
    data = request.get_json()
    task = data['task']
    delay = int(data['delay'])
    delayed_task = DelayedTask(task, delay)

    with lock:
        queue.append(delayed_task)
        queue.sort(key=lambda x: x.delay)

    return jsonify({"status": "Task added", "task": delayed_task.to_dict()}), 200

#function to retrive the poped tasks
@app.route('/get_tasks', methods=['GET'])
def get_tasks():
    current_time = time.time()
    tasks_to_return = []

    with lock:
        while queue and queue[0].timestamp <= current_time:
            tasks_to_return.append(queue.pop(0).task)

    return jsonify({"tasks": tasks_to_return}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
