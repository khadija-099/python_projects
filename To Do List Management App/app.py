from flask import Flask, request, redirect, render_template_string
import json

app = Flask(__name__)
file_name = "todo_list.json"

def load_tasks():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except:
        return {"tasks": []}

def save_tasks(tasks):
    with open(file_name, "w") as file:
        json.dump(tasks, file)

# HTML Template string
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>To-Do List</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { background: #f8f9fa; }
        .container { max-width: 600px; margin-top: 40px; }
        .task-card { padding: 10px; margin-bottom: 10px; border-radius: 10px; }
        .pending { background: #fff3cd; }
        .completed { background: #d4edda; text-decoration: line-through; }
        .btn { border-radius: 20px; }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="text-center mb-4">📝 To-Do List</h1>

        <form action="/add" method="POST" class="d-flex mb-3">
            <input type="text" name="description" class="form-control me-2" placeholder="Enter new task">
            <button type="submit" class="btn btn-primary">➕ Add</button>
        </form>

        {% if tasks %}
            {% for task in tasks %}
                <div class="task-card {% if task.complete %}completed{% else %}pending{% endif %}">
                    <div class="d-flex justify-content-between align-items-center">
                        <span>{{ loop.index }}. {{ task.description }}</span>
                        <div>
                            {% if not task.complete %}
                                <a href="/complete/{{ loop.index0 }}" class="btn btn-success btn-sm">✅ Complete</a>
                            {% endif %}
                            <a href="/delete/{{ loop.index0 }}" class="btn btn-danger btn-sm">🗑 Delete</a>
                        </div>
                    </div>
                </div>
            {% endfor %}
        {% else %}
            <p class="text-muted">No tasks yet! Add one above 👆</p>
        {% endif %}
    </div>
</body>
</html>
"""



@app.route("/")
def index():
    tasks = load_tasks()
    return render_template_string(html_template, tasks=tasks["tasks"])

@app.route("/add", methods=["POST"])
def add_task():
    tasks = load_tasks()
    description = request.form.get("description")
    if description:
        tasks["tasks"].append({"description": description, "complete": False})
        save_tasks(tasks)
    return redirect("/")

@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks["tasks"]):
        tasks["tasks"][task_id]["complete"] = True
        save_tasks(tasks)
    return redirect("/")

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks["tasks"]):
        tasks["tasks"].pop(task_id)
        save_tasks(tasks)
    return redirect("/")

    
if __name__ == "__main__":
    app.run(debug=True)































# import streamlit as st
# import json

# file_name = "todo_list.json"

# def load_tasks():
#     try:
#         with open(file_name, "r") as file:
#             return json.load(file)
#     except:
#         return {"tasks": []}

# def save_tasks(tasks):
#     with open(file_name, "w") as file:
#         json.dump(tasks, file)

# # Load tasks
# tasks = load_tasks()

# st.title("📝 To-Do List App")

# # Add new task
# new_task = st.text_input("Enter a new task:")
# if st.button("➕ Add Task"):
#     if new_task.strip():
#         tasks["tasks"].append({"description": new_task, "complete": False})
#         save_tasks(tasks)
#         st.success("Task added successfully!")
#         st.rerun()
#     else:
#         st.warning("Task description cannot be empty.")

# # Show tasks
# st.subheader("Your Tasks")
# if len(tasks["tasks"]) == 0:
#     st.write("No tasks yet!")
# else:
#     for idx, task in enumerate(tasks["tasks"]):
#         col1, col2 = st.columns([4, 1])
#         with col1:
#             status = "✅" if task["complete"] else "❌"
#             st.write(f"{idx+1}. {task['description']} {status}")
#         with col2:
#             if not task["complete"]:
#                 if st.button("Mark Complete", key=idx):
#                     tasks["tasks"][idx]["complete"] = True
#                     save_tasks(tasks)
#                     st.rerun()
