# Online-Lecture-Scheduling

Description:

This project is a Flask-based web application designed to facilitate lecture scheduling for educational institutions. It allows administrators to add courses, assign instructors to lectures without scheduling conflicts, and manage multiple batches for each course. The system ensures that no two lectures clash with each other in an instructor's schedule. Instructors can view their assigned lectures, including dates and course names, through a dedicated instructor panel.


Features:

Admin Panel: Administrators can manage instructors, add courses with details (name, level, description, image), and assign lectures to instructors on specific dates. The system prevents scheduling conflicts by ensuring an instructor cannot be assigned to multiple lectures on the same date.

Instructor Panel: Instructors can view a list of all lectures assigned to them, complete with course names and dates.


Technologies Used:

Flask (Python web framework)
SQLAlchemy (SQL toolkit and ORM for Python)
SQLite (Database)
HTML/CSS (Frontend)
Bootstrap (Styling)


How to Set Up and Run:

Prerequisites
Python 3
pip


Installation:

Clone the repository:
git clone <repository-url>

Navigate to the project directory:
cd lecture-scheduling-system

Initialize the database:
flask db upgrade

Run the application:
flask run

The application should now be accessible at http://127.0.0.1:5000/.

Contributing:

Contributions to the Lecture Scheduling System are welcome. Please fork the repository and submit a pull request with your enhancements. For major changes, please open an issue first to discuss what you would like to change.
