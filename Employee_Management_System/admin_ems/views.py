from django.shortcuts import render
from .models import user_table,user_auth
from .forms import user_table_form,user_auth_forms
# Create your views here.
def user_register(request):
    context = {}

    form = user_table_form(request.POST or None)
    if form.is_valid():
        form.save()
    
    context['form'] =  form
    return render(request,'user_register.html',context)

def user_auth(request):
    context = {}
    form = user_auth_forms(request.POST or None)
    if form.is_valid():
        form.save()
    context['form']= form
    return render(request,'user_auth.html',context)

def  index(request):
    
    return render(request,'index.html')
def list(request):
    context = user_table.objects.all()
    return render(request,'list.html',context)



