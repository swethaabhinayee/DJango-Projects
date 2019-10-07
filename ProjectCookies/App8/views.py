from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def setcookie(request):
    response=HttpResponse("Cookie Set")
    response.set_cookie("user_location",'india')
    return response

def getcookie(request):
    # return HttpResponse(request.get('user_location'))
    location=request.COOKIES['user_location']
    return HttpResponse('iam from:'+location)