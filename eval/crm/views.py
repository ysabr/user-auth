from django.shortcuts import render, redirect
from .forms import CreateUserForm
# Create your views here.

def homepage(req):
    print("hello world alah ykon dkhal")
    return render(req, 'crm/homepage.html')




def register(req):
    print("dkhal l register asat wlh hta dkhal")
    form = CreateUserForm()
    print("test test test test")
    if req.method == "POST":
        form = CreateUserForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    print("dkhal l register asat wlh hta dkhal222222222222")
    context = {'registerform':form}
    return render(req, 'crm/register.html', context=context)
    
  
def my_Login(req):
    return render(req, 'crm/login.html')

def dashboard(req):
    return render(req, 'crm/dashboard.html')
