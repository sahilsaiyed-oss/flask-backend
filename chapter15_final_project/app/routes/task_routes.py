from flask import Blueprint, request, jsonify
from app.models import Task
from app import db

task_bp = Blueprint(
    "task",
    __name__,
    url_prefix="/tasks"
)


@task_bp.route("/", methods=["GET"])
def get_tasks():

    tasks = Task.query.all()

    return jsonify([
        {
            "id": task.id,
            "title": task.title,
            "completed": task.completed
        }
        for task in tasks
    ])


@task_bp.route("/", methods=["POST"])
def create_task():

    data = request.get_json()

    task = Task(
        title=data["title"]
    )

    db.session.add(task)
    db.session.commit()

    return jsonify({
        "message": "Task created"
    })


@task_bp.route("/<int:task_id>", methods=["PUT"])
def update_task(task_id):

    task = Task.query.get_or_404(task_id)

    data = request.get_json()

    task.completed = data["completed"]

    db.session.commit()

    return jsonify({
        "message": "Task updated"
    })


@task_bp.route("/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):

    task = Task.query.get_or_404(task_id)

    db.session.delete(task)
    db.session.commit()

    return jsonify({
        "message": "Task deleted"
    })