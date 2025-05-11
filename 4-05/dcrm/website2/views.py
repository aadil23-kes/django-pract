from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

from website2.models import Department, Employee, Role

def index(request):
    #return HttpResponse("Hello from the blog!")
    return render(request,'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request,'all_emp.html',context)


def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = request.POST['salary']
        bonus = request.POST['bonus']
        phone = request.POST['phone']
        hire_date = request.POST['hire_date']
        dept_id = request.POST['dept']
        role_id = request.POST['role']

        # Get related objects from DB
        dept = Department.objects.get(id=dept_id)
        role = Role.objects.get(id=role_id)

        # Save employee
        emp = Employee(
            first_name=first_name,
            last_name=last_name,
            salary=salary,
            bonus=bonus,
            phone=phone,
            hire_date=hire_date,
            dept=dept,
            role=role
        )
        emp.save()

        # After saving, return a response with the updated list of departments and roles
        departments = Department.objects.all()
        roles = Role.objects.all()
        return render(request, 'add_emp.html', {'departments': departments, 'roles': roles, 'message': "Employee added successfully!"})

    elif request.method == 'GET':
        departments = Department.objects.all()
        roles = Role.objects.all()
        return render(request, 'add_emp.html', {'departments': departments, 'roles': roles})
    



def remove_emp(request):
    return render(request,'remove_emp.html')


def filter_emp(request):
    return render(request,'filter_emp.html')
