Classie : A Class Management System

This project is a class management system built using Django and Django REST Framework. The system provides a backend API for managing various aspects of a class environment, including announcements, assignments, class creation, student and lecturer management, course list creation, and department creation.

Features

1) Announcements: Lecturer and Course Representatives create announcement. Manage announcements for classes, visible to both students and lecturers.
2) Assignments: Create and manage assignments for students.
3) Class Creation: API for managing classes.
4) Student Signup/Login: API endpoints for student registration and authentication.
5) Lecturer Signup/Login: API endpoints for lecturer registration and authentication.
6) Course List Creation: Manage the creation and listing of courses for each department.
7) Department Creation: API for managing departments.

Technology Stack

- Backend: Django, Django REST Framework
- Database: SQLite (default) or other supported databases (MySQL, PostgreSQL, etc.)

Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Bhlak/Classie.git
   cd Classie
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  & On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Run database migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

Configuration

. Database: Configure the database in `settings.py` as needed.
. Authentication: Customize authentication classes as required.



url = "http://127.0.0.1:8000/signup/student/"

Payload = {
"full_name": "Abe",
"email": "second@gmail.com",
"password": "2222",
"matric_no": "22/SENG02",
"faculty": "Faculty of Computing and Engineering Sciences",
"department": "Software Engineering",
"year": 2,
"type": "student"
}

Response: {
User entity returned
}

# Signup for a Lecture

url = "http://127.0.0.1:8000/signup/student/"

Payload = {
"full_name": "Asbe",
"email": "hasasa@gmail.com",
"password": "1122",
"type": "lecturer",
"lecID": "2311211123",
"title": "Professor"
}

Response: {
User entity returned
}

# Login for a User

url = "http://127.0.0.1:8000/auth/login"

Payload = {
"email": "first@gmail.com"
"password": "1111"
}

Response: {
Returns token to be passed in further requests
}
