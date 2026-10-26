from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import validates, ValidationError
from models import Exercise, Workout, WorkoutExercise


class ExerciseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Exercise
        load_instance = True
    @validates("name")
    def validate_name(self, value):
        if len(value) < 3:
            raise ValidationError(
                "Exercise name must be at least 3 characters."
            )

class WorkoutSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Workout
        load_instance = True
    @validates("duration_minutes")
    def validate_duration(self, value):
        if value <= 0:
            raise ValidationError(
                "Duration must be greater than 0."
            )

class WorkoutExerciseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = WorkoutExercise
        load_instance = True


exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)

workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)

workout_exercise_schema = WorkoutExerciseSchema()
workout_exercises_schema = WorkoutExerciseSchema(many=True)