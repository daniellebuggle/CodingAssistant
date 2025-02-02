import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

load_dotenv()


def connect_db():
    """
    Connect to SQL Database using environment variables set in the .env file.
    :return: connection to the database or None
    """
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        if connection.is_connected():
            print("Connected to the MySQL database")
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None


def add_student(student_name):
    """
    Add a student to the students table.
    :param student_name: Name of the student.
    :return: Nothing
    """
    connection = connect_db()
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO students (student_name) VALUES (%s)", (student_name,))
                connection.commit()
                print(f"Student '{student_name}' added!")
        except Error as e:
            print(f"Error while adding student: {e}")
        connection.close()


def add_badge(student_id, badge_name):
    """
    Add a badge for a specific student.
    :param student_id: Student ID Number in the students table.
    :param badge_name: Name of the badge to be assigned to student.
    :return: Nothing
    """
    connection = connect_db()
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO badges (student_id, badge_name) VALUES (%s, %s)",
                    (student_id, badge_name)
                )
                connection.commit()
                print(f"Badge '{badge_name}' added for student ID {student_id}!")
        except mysql.connector.IntegrityError:
            print(f"Badge '{badge_name}' already exists for student ID {student_id}.")
        except Error as e:
            print(f"Error while adding badge: {e}")
        connection.close()


def assign_badge_if_tests_passed(student_id, badge_name, test_report, language, ast_check):
    """
    Checks if all tests passed in the test report and assigns a badge if they did.
    :param student_id: Student ID Number in the students table.
    :param badge_name: Name of the badge to be assigned to student.
    :param test_report: Test results output from unit tests.
    :return: Message indicating if the badge was assigned or not.
    """
    if ast_check:
        if "0 tests failed" in test_report and language == "java":
            add_badge(student_id, badge_name)
            return f"All tests passed! Badge '{badge_name}' assigned to student ID {student_id}."
        elif "FAILED" not in test_report and language == "python":
            add_badge(student_id, badge_name)
            return f"All tests passed! Badge '{badge_name}' assigned to student ID {student_id}."
    return "Not all tests passed. Badge not assigned."
