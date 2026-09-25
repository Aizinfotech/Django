from django.shortcuts import render

# Create your views here.


def aiml_student(request):
    return render(request, 'student/aiml.html')


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')