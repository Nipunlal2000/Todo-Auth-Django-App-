from django.shortcuts import render,redirect
from .models import TODO
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        fname = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('pwd')
        print(fname,email,password)
        
        my_user = User.objects.create_user(fname,email,password)
        my_user.save() 
        
        return redirect('/login')       
    return render (request,'signup.html')

def Login(request):
    if request.method == 'POST':
        fname = request.POST.get('username')
        pwd = request.POST.get('pwd')
        print(fname,pwd)
        
        userr = authenticate(request,username = fname,password =pwd)
        if userr is not None:
            login(request,userr)
            return redirect('/todo')
        else:
            return redirect('/login')
    return render(request,'login.html')

@login_required(login_url = '/login')    
def TodoPage(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        print(title)
        #todo (title) and its related user (user) we create obj
        obj = TODO(title = title,user = request.user)
        obj.save()
        
        #after saving the todo created by that user in date order should show
        result = TODO.objects.filter(user = request.user).order_by('-date')
        
        # in this page the todo data will be displayed with this context
        return redirect('/todo',{'result': result})
        
    result = TODO.objects.filter(user = request.user).order_by('-date')
    return render (request,'todo.html',{'result': result})

@login_required(login_url = '/login')    
def Update(request,srno):
    obj = TODO.objects.get(srno = srno)
    if request.method == 'POST':
        title = request.POST.get('title')
        print(title)
        #here we get/fetch the previous og data 
        obj.title = title
        obj.save()
        
        return redirect('/todo')
    return render (request,'update_todo.html',{'obj': obj})

@login_required(login_url = '/login')    
def Delete(request,srno):
    obj = TODO.objects.get(srno = srno)
    obj.delete()
    return redirect('/todo')

def Signout(request):
    logout(request)
    return redirect('/login')