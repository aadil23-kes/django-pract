from django.http import HttpResponse
from django.shortcuts import render

from website2.models import Department, Employee, Role




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


def add_emp(request):
   if request.method == 'POST':
        print('post')
        first_name = request.POST['first_name']
        print(first_name)
        last_name = request.POST['last_name']
        salary = request.POST['salary']
        bonus = request.POST['bonus']
        phone = request.POST['phone']
        hire_date = request.POST['hire_date']
        print(last_name,salary,bonus,phone,hire_date)
        dept = request.POST['dept']
        role = request.POST['role']
        
        dept = Department.objects.get(id=dept)
        role = Role.objects.get(id=role)

        print(dept,role)


 


   else:
        print('get')

   return render(request,'add_emp.html')
