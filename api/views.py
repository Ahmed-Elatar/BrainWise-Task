from django.shortcuts import render ,redirect ,get_object_or_404
from django.http.response import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User, Group
from django.utils.timezone import datetime

from .forms import *
from .models import *
from .serializers import *
# Create your views here.


def index(request):
    items=Company.objects.all().order_by('name')
    companies=CompanySerializer(items,many=True).data
    items=Employee.objects.all().order_by('company','department')
    employees=EmployeeSerializer(items,many=True).data



    return render(request,"index.html",{"user":request.user.username,"companies":companies,"employees":employees})



def if_admin(request):



    if request.user.groups.filter(name='Managers').exists():
        return True

    else:
        return False





def adding_company(request):
    message=""
    form = AddComapnyForm()
    if request.method == 'POST':
        if if_admin(request):
        
            form = AddComapnyForm(request.POST)
            if form.is_valid():
                ser=CompanySerializer(data=form.cleaned_data)
                if ser.is_valid():
                    ser.save()
                return redirect('index')
    

        else:
            message="not_admin"

    return render(request, 'adding_company.html', {'form': form,"user":request.user.username,"message":message})
    
    

def adding_department(request):
    message=""
    form = AddDepatmentForm()
    if request.method == 'POST':
        if  if_admin(request):
            form = AddDepatmentForm(request.POST)
            if form.is_valid():
                form.save()
                x=Company.objects.get(name = form.cleaned_data['company'])
                x.number_of_departments+=1
                x.save()
                print(x.number_of_departments)
            
                return redirect('index')
        else:
            message="not_admin"
    
        
    return render(request, 'adding_department.html', {'form': form,"user":request.user.username,"message":message})
    

def adding_employee(request):
    
        message=""
        form = AddEmployeeForm()
        if request.method == 'POST':
            if if_admin(request):
                form = AddEmployeeForm(request.POST)
                
                if form.is_valid():
                    xd=Department.objects.get(name = form.cleaned_data['department'] )
                    xc=Company.objects.get(name = form.cleaned_data['company'] )
                    if xc ==xd.company :
                        
                    #for counting employee
                        x=Company.objects.get(name = form.cleaned_data['company'])
                        x.number_of_employees+=1
                        x.save()
                        form.save()
                    else:
                        message ="erorr"
                        return render(request, 'adding_employee.html', {'form': form,"user":request.user.username,"message":message})

                    return redirect('index')
            else:
                    message="not_admin"    
                
        
            
    
        return render(request, 'adding_employee.html', {'form': form,"user":request.user.username,"message":message})
    



# @api_view(["GET","POST"])
def list_comapnies(request):

    items=Company.objects.all().order_by('name')

    ser=CompanySerializer(items,many=True)
    
    paginator = Paginator(ser.data,3)
    page_number = request.GET.get('page', 1)
    companies=paginator.page(page_number)
    

    return render (request,"list_company.html",{'companies':companies,"user":request.user.username})




def company_details(request,id):

    company=get_object_or_404(Company,id=id)
    items=Employee.objects.filter(company  =id)
    ser=EmployeeSerializer(items,many=True)
    employees=ser.data

    dep=Department.objects.filter(company =id)
    dep_ser=DepartmentSerializer(dep,many=True)
    department=dep_ser.data

    return render (request,"details.html",{'company':company,"user":request.user.username,"employees":employees,"department":department})



def list_employees(request):

    items=Employee.objects.all().order_by('company','department')

    employees=EmployeeSerializer(items,many=True).data

    
    

    return render (request,"list_employees.html",{'employees':employees,"user":request.user.username})





def employee_details(request,id):

    message=""
    items=get_object_or_404(Employee,id=id)
    form=EditEmployeeForm()
    ser=EmployeeSerializer(items)
    employee=ser.data

    # calculate work days
    now=datetime.now().date()  
    date_object = datetime.strptime(employee['hired_on'], '%Y-%m-%d').date()
    hired_days = abs(date_object - now)
    employee['hired_days']=hired_days.days
    #-----------------------------------
    if if_admin(request):
        
        if request.method =='POST':
            
            form=EditEmployeeForm(request.POST)
            if form.is_valid():
                if form.cleaned_data['name'] !="":
                    items.name = form.cleaned_data['name']
                    
                if form.cleaned_data['email'] !="":
                    items.name = form.cleaned_data['email']
                    
                if form.cleaned_data['mobile_number'] !="":
                    items.name = form.cleaned_data['mobile_number']
                    
                if form.cleaned_data['address'] !="":
                    items.name = form.cleaned_data['address']
                
                items.save()
                return redirect('employee_details',id)

    else:
        message="not_admin"                



    return render (request,"employee_details.html",{"form":form,"employee":employee,"user":request.user.username,"message":message})





















####################################################################################################
##################                  Authentication

#sign-up 
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form,"user":request.user.username})



# login
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form,"user":request.user.username})


# logout page
def user_logout(request):
    logout(request)
    return redirect('login')




