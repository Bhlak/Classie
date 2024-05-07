from django.shortcuts import render
from django.contrib import messages
from models import Lecturer
# Create your views here.

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        faculty = request.POST['faculty']
        department = request.POST['department']
        course_title = request.POST['course_title']
        course_code = request.POST['course_code']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if Lecturer.objects.filter(email=email).exists():
                messages.info(request='email exists')
            else:
                user = Lecturer.objects()