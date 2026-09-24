from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


def home(request):
    return HttpResponse("Hello, welcome to our course!")


def about(request):
    return HttpResponse("This is the about page of our course.")

def blog(request):
    return HttpResponse("This is the blog page of our course.")

# def blog_detail(request, **kwargs):
#     return HttpResponse(f"this blog year is {kwargs.get('blog_year')}: and this blog month is {kwargs.get('blog_month')}.")

def course_list(request):
    return render(request, 'course/courselist.html')


class Course:
    def __init__(self, name, description):
        self.name = name
        self.description = description

def course_detail(request):
    context = {
        'course': "AIML Programming",
        'Description': "This course covers the fundamentals of Artificial Intelligence ",
        'duration': "6 Months",
        'start_date': datetime(2024, 7, 1, 13, 15, 30),
        "Total_sessions": 124.2345,
        "course_topics": [ "Python Basics", "Machine Learning", "Deep Learning" ],
        "course_details": {
            "course": "AIML Development",
            "Description": "This is the syllabus for the AIML Programming course."
        }
    }
    
    return render(request, 'course/course_detail.html', context)