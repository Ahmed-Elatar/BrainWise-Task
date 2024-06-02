from django.urls import path,include
from .views import *


urlpatterns = [

    path('login/',user_login,name="login"),
    path('singup/',user_signup,name="signup"),
    path('logout/',user_logout,name="logout"),

    path('',index,name="index"),


    path('companies/', list_comapnies,name="list_comanies"),
    path('employees/', list_employees,name="list_employees"),
    path('company/<int:id>/',company_details,name="company_details"),
    path('employee/<int:id>/',employee_details,name="employee_details"),



    path('adding-company/',adding_company,name="adding_company"),
    path('adding-department/',adding_department,name="adding_department"),
    path('adding-employee/',adding_employee,name="adding_employee"),



]
