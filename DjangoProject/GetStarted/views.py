from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def createUser(request):
    return render(request,'\ProjShell\Front\index.html')
#    HttpResponse('Henlo')