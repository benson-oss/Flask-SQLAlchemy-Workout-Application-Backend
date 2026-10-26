import requests

BASE_URL = "http://127.0.0.1:4000"


def view_workouts():
    try:
        response = requests.get(f"{BASE_URL}/workouts", timeout=10)

        print("Status:", response.status_code)

        if response.status_code == 200:
            workouts = response.json()

            if not workouts:
                print("No workouts found.")
                return

            for workout in workouts:
                print(
                    f"{workout['id']} | "
                    f"{workout['date']} | "
                    f"{workout['duration_minutes']} mins | "
                    f"{workout.get('notes', '')}"
                )
        else:
            print("Error:", response.text)

    except requests.exceptions.RequestException as error:
        print("Could not connect to the server:", error)


def create_workout():
    try:
        workout_date = input("Date (YYYY-MM-DD): ").strip()
        duration_input = input("Duration (minutes): ").strip()
        notes = input("Notes: ").strip()

        # Validate duration
        try:
            duration = int(duration_input)

            if duration <= 0:
                print("Duration must be greater than zero.")
                return

        except ValueError:
            print("Please enter a valid whole number for duration.")
            return

        # Validate date format
        from datetime import date

        try:
            date.fromisoformat(workout_date)
        except ValueError:
            print("Invalid date. Use YYYY-MM-DD, e.g. 2026-10-25.")
            return

        # Send workout data to Flask
        response = requests.post(
            f"{BASE_URL}/workouts",
            json={
                "date": workout_date,
                "duration_minutes": duration,
                "notes": notes
            },
            timeout=10
        )

        print("Status:", response.status_code)
        print("Response:", response.text)

    except requests.exceptions.RequestException as error:
        print("Could not connect to the server:", error)


def delete_workout():
    try:
        workout_id = input("Workout ID: ").strip()

        if not workout_id.isdigit() or int(workout_id) <= 0:
            print("Please enter a valid workout ID.")
            return

        response = requests.delete(
            f"{BASE_URL}/workouts/{workout_id}",
            timeout=10
        )

        print("Status:", response.status_code)

        if response.status_code in (200, 204):
            if response.text:
                print("Response:", response.text)
            else:
                print("Workout deleted successfully.")
        else:
            print("Error:", response.text)

    except requests.exceptions.RequestException as error:
        print("Could not connect to the server:", error)
def view_exercises():
    try:
        response = requests.get(
            f"{BASE_URL}/exercises",
            timeout=10
        )

        if response.status_code == 200:
            exercises = response.json()

            if not exercises:
                print("No exercises found.")
                return

            for exercise in exercises:
                equipment = (
                    "Required"
                    if exercise["equipment_needed"]
                    else "Not required"
                )

                print(
                    f"{exercise['id']} | "
                    f"{exercise['name']} | "
                    f"{exercise['category']} | "
                    f"Equipment: {equipment}"
                )
        else:
            print("Error:", response.text)

    except requests.exceptions.RequestException as error:
        print("Connection error:", error)


def create_exercise():
    name = input("Exercise name: ").strip()
    category = input("Category: ").strip()
    equipment = input("Equipment needed? (yes/no): ").strip().lower()

    if equipment not in ("yes", "no"):
        print("Enter yes or no for equipment.")
        return

    try:
        response = requests.post(
            f"{BASE_URL}/exercises",
            json={
                "name": name,
                "category": category,
                "equipment_needed": equipment == "yes"
            },
            timeout=10
        )

        print("Status:", response.status_code)
        print("Response:", response.text)

    except requests.exceptions.RequestException as error:
        print("Connection error:", error)


def delete_exercise():
    exercise_id = input("Exercise ID: ").strip()

    if not exercise_id.isdigit() or int(exercise_id) <= 0:
        print("Enter a valid exercise ID.")
        return

    try:
        response = requests.delete(
            f"{BASE_URL}/exercises/{exercise_id}",
            timeout=10
        )

        print("Status:", response.status_code)
        print("Response:", response.text)

    except requests.exceptions.RequestException as error:
        print("Connection error:", error)

def menu():
    while True:
        print("\n===== Workout Tracker =====")
        print("1. View Workouts")
        print("2. Create Workout")
        print("3. Delete Workout")
        print("4. Exit")
        print("5. View Exercises")
        print("6. Create Exercise")
        print("7. Delete Exercise")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            view_workouts()

        elif choice == "2":
            create_workout()

        elif choice == "3":
            delete_workout()

        elif choice == "4":
            print("Exiting Workout Tracker.")
            break

        elif choice == "5":
            view_exercises()

        elif choice == "6":
            create_exercise()

        elif choice == "7":
            delete_exercise()

        else:
            print("Invalid choice. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    menu()