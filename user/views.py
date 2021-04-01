# Django imports

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth import login, authenticate





def auth_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():        
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            form = AuthenticationForm(data=request.POST)
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('/')
            else:
                messages.error(request,"Invalid username or password.")            
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="users/login.html", context={"form":form})        
            
            
            
            
    
    



def auth_logout(request):
    logout(request)
    return redirect('/')
