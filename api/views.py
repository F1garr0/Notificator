from django.core.handlers.wsgi import WSGIRequest
from django.http.request import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse
#from .models import AnkeyUser, Organization
from .models import User

# Create your views here.
def get_users(request: WSGIRequest):
#    req = request.read()
#    AnkeyUser.objects.create(firstName="alan")
#    org = Organization.objects
#    users = AnkeyUser.objects.all()
#    user : AnkeyUser= users.get(id=4)
#    return HttpResponse(user.firstName)
    return HttpResponse(User.objects.all().values_list())
#    return HttpResponse("{\"result\":\"ok\"}")

def create_user(request: WSGIRequest):
    request.body
    return HttpResponse("rorre")
