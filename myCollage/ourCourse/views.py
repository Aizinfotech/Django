from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, welcome to our course!")


def about(request):
    return HttpResponse("This is the about page of our course.")

def blog(request):
    return HttpResponse("This is the blog page of our course.")

def blog_detail(request, **kwargs):
    return HttpResponse(f"this blog year is {kwargs.get('blog_year')}: and this blog month is {kwargs.get('blog_month')}.")