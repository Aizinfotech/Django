import datetime
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class SimpleLogMiddleware(MiddlewareMixin):

    def process_request(self, request):
        print(f" [{datetime.datetime.now()}] Request Url: {request.path}")

   
    def process_response(self, request, response):
        print(f" [{datetime.datetime.now()}] response status code: {response.status_code}")
        return response



class BlockIPMiddleware(MiddlewareMixin):
    BLOCKED_IPS = ['127.0.0.3']  

    def process_request(self, request):
        ip = request.META.get('REMOTE_ADDR')
        if ip in self.BLOCKED_IPS:
            return HttpResponse("Your Ip is Blocked", status=403)




# request.META -> is a dictionary-like object containing information about the request and server environment
# can contain things like
#     REMOTE_ADDR
#     REQUEST_METHOD
#     HTTP_USER_AGENT
#     SERVER_NAME
#     SERVER_PORT
#     HTTP_HOST