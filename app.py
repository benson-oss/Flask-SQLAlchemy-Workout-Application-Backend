from flask import Flask,make_response,request,jsonify
from extensions import db
from flask_migrate import Migrate
from models import *
from schemas import (
    exercise_schema,
    exercises_schema,
    workout_schema,
    workouts_schema,
    workout_exercise_schema
)

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

# =========================
# WORKOUT ROUTES
# =========================

@app.route('/workouts', methods=['GET'])
def get_workouts():
    workouts = Workout.query.all()
    return workouts_schema.dump(workouts), 200


@app.route('/workouts/<int:id>', methods=['GET'])
def get_workout(id):
    workout = Workout.query.get_or_404(id)
    return workout_schema.dump(workout), 200


@app.route('/workouts', methods=['POST'])
def create_workout():

    data = request.get_json()

    workout = Workout(
        date=data["date"],
        duration_minutes=data["duration_minutes"],
        notes=data["notes"]
    )

    db.session.add(workout)
    db.session.commit()

    return workout_schema.dump(workout), 201


@app.route('/workouts/<int:id>', methods=['DELETE'])
def delete_workout(id):

    workout = Workout.query.get_or_404(id)

    db.session.delete(workout)
    db.session.commit()

    return jsonify({
        "message": "Workout deleted successfully"
    }), 200


# =========================
# EXERCISE ROUTES
# =========================

@app.route('/exercises', methods=['GET'])
def get_exercises():

    exercises = Exercise.query.all()

    return exercises_schema.dump(exercises), 200


@app.route('/exercises/<int:id>', methods=['GET'])
def get_exercise(id):

    exercise = Exercise.query.get_or_404(id)

    return exercise_schema.dump(exercise), 200


@app.route('/exercises', methods=['POST'])
def create_exercise():

    data = request.get_json()

    exercise = Exercise(
        name=data["name"],
        category=data["category"],
        equipment_needed=data["equipment_needed"]
    )

    db.session.add(exercise)
    db.session.commit()

    return exercise_schema.dump(exercise), 201


@app.route('/exercises/<int:id>', methods=['DELETE'])
def delete_exercise(id):

    exercise = Exercise.query.get_or_404(id)

    db.session.delete(exercise)
    db.session.commit()

    return jsonify({
        "message": "Exercise deleted successfully"
    }), 200


# =========================
# WORKOUT EXERCISE ROUTES
# =========================

@app.route(
    '/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises',
    methods=['POST']
)
def add_exercise_to_workout(workout_id, exercise_id):

    workout = Workout.query.get_or_404(workout_id)
    exercise = Exercise.query.get_or_404(exercise_id)

    data = request.get_json()

    workout_exercise = WorkoutExercise(
        workout=workout,
        exercise=exercise,
        reps=data["reps"],
        sets=data["sets"],
        duration_seconds=data["duration_seconds"]
    )

    db.session.add(workout_exercise)
    db.session.commit()

    return workout_exercise_schema.dump(workout_exercise), 201




if __name__ == "__main__":
    app.run(debug=True, port=4000)