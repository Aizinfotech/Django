from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.core.mail import send_mail



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




def set_cookie(request):
    response = HttpResponse("Cookie Set Successfully")
    response.set_cookie('username','Moin', max_age=60*60*24*5)
    response.set_cookie('course','Python Full Course', max_age=60*60*24*5)
    return response


def get_cookie(request):
    username = request.COOKIES.get('username', 'Guest')
    course = request.COOKIES.get('course', 'Not entrolled')
    return HttpResponse(f"Welcome {username},  you are learning {course}")
    # if username in request.COOKIES:
    #     return HttpResponse(f"Welcome {username},  you are learning {course}")
    # else:
    #     return HttpResponse("No Cookies found")




def delete_cookie(request):
    response = HttpResponse('Cookie Delete Successfully')
    response.delete_cookie('username')
    response.delete_cookie('course')
    return response



# def send_test_mail(request):
#     subject = 'Welcome to AIZ infotechs'
#     message = "Welcome to AIZ infotechs, where you can learn Python Full Course."
#     from_mail = "moinuddinbavan@gmail.com"
#     recipient_list = ["aizinfotech@gmail.com", "aizinfotechs@gmail.com"]
#     send_mail(subject, message, from_mail, recipient_list)
#     return HttpResponse("Mail sent successfully")