from django.shortcuts import render, redirect

from .models import Student, Contact

from django.http import HttpResponse

# Create your views here.


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student/studentlist.html', {'students': students})

def aiml_student(request):
    return render(request, 'student/aiml.html')

def contact_form(request):
    return render(request, 'student/student_form.html')

def submit_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Create a new Contact instance and save it to the database
        contact = Contact(name=name, email=email, message=message)
        contact.save()

        # return HttpResponse(f"Thank you {name} for your message!")  # You can customize the response as needed
        # return redirect('contact_form')  # Redirect to the contact form after submission
        return render(request, 'student/student_form.html')  # Render the form if not a POST request

    else:
        return HttpResponse("Invalid request method. Please submit the form using POST.")




def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')