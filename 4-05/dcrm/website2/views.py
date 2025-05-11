from django.http import HttpResponse
from django.shortcuts import render

from website2.models import Employee




def index(request):
    #return HttpResponse("Hello from the blog!")
    return render(request,'index.html')



def all_emp(request):
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    print(context)
    return render(request,'all_emp.html',context)