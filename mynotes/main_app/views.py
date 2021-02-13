from django.shortcuts import render,redirect
from main_app.forms import RegisterForm
from django.contrib.auth import login,authenticate,logout
# Create your views here.
def home_page(request):
    return render(request,'base.html')

def register_account(request):
    context={}
    user=request.user
    form=RegisterForm()
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            context['form']=form
    else:
        form=RegisterForm()
    return render(request,'register.html',context)

def login_account(request):
    user=request.user
    context={}
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(email=email,password=password)
        if user:
            login(request,user)
            return redirect('notes:mynotes')
        else:
            context['error']='Invalid password or email'
    return render(request,'login.html',context)

def logout_account(request):
    logout(request)
    return redirect('home')