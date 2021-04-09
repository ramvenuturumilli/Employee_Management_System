from django.shortcuts import render,redirect
from .models import user_table,user_auth
from .forms import user_table_form,user_auth_forms
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.models import Q


# Create your views here.
def user_register(request):
    context = {}

    form = user_table_form(request.POST or None)
    if form.is_valid():
        form.save()
    
    context['form'] =  form
    return render(request,'user_register.html',context)



def  index(request):
    return render(request,'index.html')

def list_view(request):
    context = {'list':  user_table.objects.all().values()}
    return render(request,'list.html',context)


def logout_request(request):
    logout(request)
    messages.info(request,'logged out successfully')
    return redirect('/')

def login_request(request):
    form = AuthenticationForm()
    return render(request = request,
                  template_name = "user_auth.html",
                  context={"form":form})

def user_auth(request):
    if request.method == "POST":
        form = AuthenticationForm(request ,data=request.POST)
        print(form)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(username = username, password = password)
            print(user)
            if user:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                # messages.info('',user)
                print(user)
                print("--------------------------------")
                return redirect('/sucess')
            else:
                messages.error(request, "Invalid username or password.")
                return render(request,'user_auth.html',context)
    form = AuthenticationForm()
    context = {"form": form}
    return render(request,'user_auth.html',context)