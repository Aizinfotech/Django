from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def set_session(request):
    request.session['username'] = 'Zaid'
    request.session['course'] = '   '
    return HttpResponse("Session Data saved successfully")


def get_session(request):
    username = request.session.get('username', 'Guest')
    course = request.session.get('course', 'Not entrolled')
    return HttpResponse(f"Welcome {username},  you are learning {course}")


def delete_session(request):
    # 1
    # try:
    #     del request.session['username']
    #     del request.session['course']
    # except KeyError:
    #     pass
    # return HttpResponse("Session data deleted successfully.")

    # 2
    request.session.flush() # this will delet all session data
    return HttpResponse("Session data deleted successfully.")