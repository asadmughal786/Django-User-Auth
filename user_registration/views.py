from django.shortcuts import redirect, render,HttpResponseRedirect
from .forms import SignUpForm,EditUserProfileForm,EditAdminProfileForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages

# Create your views here.
#---------------------------------------------------------- singup form buildin

def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"user registered successfully!")
    else:
        form = SignUpForm()
    return render(request,'signup.html',{'form':form})

# ----------------------------------------------------------Login Function buildin
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request= request,data = request.POST)
        if form.is_valid():
            u_name = form.cleaned_data['username']
            u_pass = form.cleaned_data['password']
            user  = authenticate(username = u_name,password= u_pass)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/profile/')
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form':form})

#-------------------------------------------------------------Profile function 

def user_profile(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            if request.user.is_superuser == True:
                form = EditAdminProfileForm(request.POST, instance = request.user)
            else:
                form = EditUserProfileForm(request.POST,instance=request.user)
            if form.is_valid():
                messages.success(request,'User Updated Successfully!')
                form.save()
        else:
            if request.user.is_superuser == True:
                form = EditAdminProfileForm(instance = request.user)
            else:
                form = EditUserProfileForm(instance = request.user)
        return render(request,'profile.html',{'name':request.user,'form':form})
    else:
        messages.error(request,'You are not authorized to access this page!')
        return HttpResponseRedirect('/login/')
# ------------------------------------------------------------Logout

def user_logout(request):
        logout(request)   
        messages.info(request,"Logout successfully!")
        return HttpResponseRedirect('/login/')

def changepass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PasswordChangeForm(user=request.user , data = request.POST)
            if form.is_valid():
                form.save()
                #This function is user to maintain the session for the user.
                update_session_auth_hash(request,form.user)
                messages.info(request,'Password Saved Successfully!')
                return HttpResponseRedirect('/profile/',)
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request,'changepass.html',{"form": form})
    else:
        messages.error(request,'You have no rights to access this page!')
        return HttpResponseRedirect('/login/')


#----------------------------------- method 2 Change Password without entering the old password----------------------------------------
def changepass1 (request):
    if request.user.is_authenticated:
        if request.method =="POST":
            form = SetPasswordForm(user= request.user,data=request.POST)
            if form.is_valid():
                form.save()
                #This function is user to maintain the session for the user.
                update_session_auth_hash(request,form.user)
                messages.info(request,'Password Saved Successfully!')
                return HttpResponseRedirect('/profile/',)
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request,'changepass.html',{"form": form})
    else:
        messages.error(request,'You have no rights to access this page!')
        return HttpResponseRedirect('/login/')
