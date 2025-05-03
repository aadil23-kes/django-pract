from django.http import HttpResponse
from django.shortcuts import render




def index(request):
    #return HttpResponse("Hello from the blog!")
    return render(request,'index.html')



def all_emp(request):
    #return HttpResponse("Hello from the blog!")
    return render(request,'all_emp.html')