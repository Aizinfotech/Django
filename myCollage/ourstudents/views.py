from django.shortcuts import render

from .models import Student

from django.http import HttpResponse

# Create your views here.


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student/studentlist.html', {'students': students})

def aiml_student(request):
    return render(request, 'student/aiml.html')


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')