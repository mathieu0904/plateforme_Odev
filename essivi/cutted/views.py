from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def Signup(request):
    if request.method == 'GET':
        # <view logic>
        return render (request, 'signup.html')
        return HttpResponse('result')