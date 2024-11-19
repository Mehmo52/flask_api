from flask import Flask, jsonify, request

app = Flask(__name__)

# Beispiel-Daten
tasks = [
    {"id": 1, "title": "Einkaufen gehen", "completed": False},
    {"id": 2, "title": "Python lernen", "completed": False}
]

# GET: Alle Aufgaben abrufen
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# POST: Neue Aufgabe hinzufügen
@app.route('/tasks', methods=['POST'])
def create_task():
    new_task = request.get_json()
    new_task["id"] = len(tasks) + 1
    tasks.append(new_task)
    return jsonify(new_task), 201

# PUT: Aufgabe aktualisieren
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task:
        updates = request.get_json()
        task.update(updates)
        return jsonify(task)
    return {"error": "Task not found"}, 404

# DELETE: Aufgabe löschen
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return {"message": "Task deleted successfully"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
