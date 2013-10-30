from flask import Flask, render_template
import json
app = Flask(__name__)

user_tasks = [{"title":"a task", "description":"A test task", "id":0, "complete": False}]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/1")
def example():
    return render_template("example.html")

@app.route("/2")
def example2():
    return render_template("example2.html")

@app.route("/slides/jquery")
def jquery():
    return render_template("jquery_slides.html")

@app.route("/slides/ajax")
def ajax():
    return render_template("ajax_slides.html")

@app.route("/tasks/add")
def add_task():
    task = {"title" : request.form.get("title", "Untitled Task"),
    "description" : request.form.get("description", ""),
    "id": len(user_tasks),
    "complete": False}
    user_tasks.append(task)
    return json.dumps(task)


@app.route("/tasks/delete/<task_id>")
def del_task(task_id):
    for i in range(0,len(user_tasks)):
        if user_tasks[i]["id"] == task_id:
            del user_tasks[i]
            return "success"
    return "error - task not found"


@app.route("/tasks")
def tasks():
    return json.dumps(user_tasks)


if __name__ == "__main__":
    app.run(debug=True)