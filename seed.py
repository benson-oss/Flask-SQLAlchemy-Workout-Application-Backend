from datetime import date
from models import Exercise, Workout, WorkoutExercise
from app import app
from extensions import db


def seed_data():
    with app.app_context():

        # Clear existing data
        WorkoutExercise.query.delete()
        Workout.query.delete()
        Exercise.query.delete()

        # Exercises
        pushup = Exercise(
            name="Push Up",
            category="Chest",
            equipment_needed=False
        )

        squat = Exercise(
            name="Squat",
            category="Legs",
            equipment_needed=False
        )

        # Workout
        workout1 = Workout(
            date=date.today(),
            duration_minutes=45,
            notes="Morning workout"
        )

        db.session.add_all([
            pushup,
            squat,
            workout1
        ])

        db.session.commit()

        # Join records
        workout_exercise1 = WorkoutExercise(
            workout=workout1,
            exercise=pushup,
            reps=15,
            sets=3,
            duration_seconds=60
        )

        workout_exercise2 = WorkoutExercise(
            workout=workout1,
            exercise=squat,
            reps=12,
            sets=4,
            duration_seconds=90
        )

        db.session.add_all([
            workout_exercise1,
            workout_exercise2
        ])

        db.session.commit()

        print("Database seeded successfully!")


if __name__ == "__main__":
    seed_data()