**Workout Tracking Application API**

A RESTful Flask API for managing workouts and exercises. Users can create workouts, manage exercises, and track workout-specific metrics such as sets, reps, and duration through a many-to-many relationship.

# Features
Create, view, and delete workouts
Create, view, and delete exercises
Associate exercises with workouts
Track:
    Reps
    Sets
    Duration (seconds)
    SQLAlchemy ORM relationships
    Marshmallow serialization
    Model validations
    Schema validations
    Database seed file
    RESTful API design

# Technologies Used
    Python 3
    Flask
    Flask-SQLAlchemy
    Flask-Migrate
    Marshmallow
    SQLite
    SQLAlchemy
**Project Structure**
Plain Text

workout-tracking-application/
│
├── app.py
├── models.py
├── schemas.py
├── seed.py
├── config.py
├── extensions.py
├── requirements.txt
├── README.md
│
├── instance/
│ └── app.db
│
└── migrations/

Database Models

**Exercise**
Field	        
Typeid	        |Integer
name	        |String
category        |String
equipment_needed|Boolean

**Workout**

Field	
Typeid	Integer
date	Date
duration_minutes	Integer
notes	Text
WorkoutExercise

Join table connecting Workouts and Exercises.

Field	
Typeid	            Integer
workout_id	        Foreign Key
exercise_id	        Foreign Key
reps	            Integer
sets	            Integer
duration_seconds	Integer

Relationships
Plain Text
Workout
|
| 1 - *
|
WorkoutExercise
|
| * - 1
|
Exercise

 A Workout has many WorkoutExercises
An Exercise has many WorkoutExercises
A WorkoutExercise belongs to a Workout
A WorkoutExercise belongs to an Exercise 

**Installation**

    Clone Repository
    Shell
    git clone <repository-url>
    Shell
    cd workout-tracking-application
    Create Virtual Environment
    Shell
    pipenv install

Activate shell:

    Shell
    pipenv shell
    Install Dependencies
    Shell
    pip install -r requirements.txt
    Database Setup

Initialize migrations:

    Shell
    flask db init

    Create migration:

    Shell
    flask db migrate -m "initial migration"

Apply migration:

    Shell
    flask db upgrade
    Seed Database

Populate the database with sample data:

    Shell
    python seed.py

Example seeded data:

    Push Up
    Squat
    Morning Workout
    WorkoutExercise associations
    Running the Application
    Shell
    flask run

Application runs at:

Plain Text
http://127.0.0.1:5000
API Endpoints
Workouts
Get All Workouts
HTTP
GET /workouts
Get Workout By ID
HTTP
GET /workouts/<id>
Create Workout
HTTP
POST /workouts

Body:

    JSON
    {
    "date": "2026-10-24",
    "duration_minutes": 45,
    "notes": "Morning workout"
    }
Delete Workout
HTTP
DELETE /workouts/<id>
Exercises
Get All Exercises
HTTP
GET /exercises
 
Get Exercise By ID
HTTP
GET /exercises/<id>
Create Exercise
HTTP
POST /exercises
 

Body:

    JSON
    {
    "name": "Push Up",
    "category": "Chest",
    "equipment_needed": false
    }
Delete Exercise
HTTP
DELETE /exercises/<id>
Workout Exercise

Associate an exercise with a workout.

HTTP
    POST /workouts/<workout_id>/exercises/<exercise_id>/workout_exercises

Body:

    JSON
    {
    "reps": 15,
    "sets": 3,
    "duration_seconds": 60
    }
    Validations
    Table Constraints

Examples:

    Python
    nullable=False
    Python
    db.CheckConstraint("duration_minutes > 0")
    Model Validations

Examples:

    Exercise name must contain at least 3 characters.
    Duration must be greater than 0.
    Reps and sets cannot be negative.
    Schema Validations

Implemented using Marshmallow:

    Exercise name validation
    Category validation
    Duration validation
    Reps validation
    Testing

Run the application:

    Shell
    flask run

Use:

    Postman
    Insomnia
    Thunder Client

to test all API endpoints.

    Future Improvements
    User authentication
    Workout categories
    Update endpoints (PUT/PATCH)
    Workout statistics dashboard
    React frontend integration

Author

Benson Maina