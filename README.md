# Signup for a Student

url = "http://127.0.0.1:8000/signup/student/"

Payload = {
"full_name": "Abe",
"email": "second@gmail.com",
"password": "2222",
"matric_no": "1902",
"faculty": "Engineering",
"department": "Computer Engineering",
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
