from django.shortcuts import render

# Create your views here.


def aiml_student(request):
    return render(request, 'student/aiml.html')