
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product
from .models import Customer

# Create your views here.
def index(request):
    prds=Product.objects.all();# fetch the data in database
    return render(request,'index.html',{'products':prds})

def signup(request):
   if request.method =='POST':
       first_name=request.POST.get('fname')
       last_name=request.POST.get('lname')
       email=request.POST.get('email')
       mobile=request.POST.get('mobile')
       password=request.POST.get('password')
       print(first_name,last_name,email,mobile,password)
       customer=Customer(first_name=first_name,last_name=last_name,email=email,mobile=mobile,
                         password=password)
       customer.register()
       return render(request,'login.html')
   else:
       return render(request,'signup.html')

def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        email=request.POST.get('email')
        password=request.POST.get('password')
        customer=Customer.get_customer_by_email(email)
        error_message=None
        if customer:
            return redirect('homepage')
        else:
            error_message='email is invalid please ragister email'

        return render(request,'login.html',{'error':error_message})

