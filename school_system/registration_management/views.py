# from django.shortcuts import render
# from django.http import HttpResponseRedirect,HttpResponse
from django.http import JsonResponse



def index(request):
    # return render(request,'basic_app/index.html')
    # return HttpResponse("You are in registration page, Nice")
    return JsonResponse({'register':False})
