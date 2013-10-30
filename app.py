from flask import Flask, g
import json
app = Flask(__name__)

g.tasks = []

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/tasks/add")
def add_task():
    task = {"title" : request.form.get("title", "Untitled Task"),
    "description" : request.form.get("description", ""),
    id: len(g.tasks)}
    g.tasks.append(task)
    return json.dumps(task)


@app.route("/tasks/delete/<task_id>")
def del_task(task_id):
    for i in range(0,len(g.tasks)):
        if g.tasks[i]["id"] == task_id:
            del g.tasks[i]
            return "success"
    return "error - task not found"


@app.route("/tasks")
def tasks():
    return json.dumps(g.tasks)


if __name__ == "__main__":
    app.run()