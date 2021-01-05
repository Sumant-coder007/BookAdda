from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import UserRegistrationForm,UserUpdateForm,ProfileUpdateForm
from .models import Book
# Create your views here.




def register(request):
    if request.method == 'POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Your Account Has Been Created!! You Can Log In Now!! as {username}')
            return redirect("login")
    else:
        form=UserRegistrationForm()
    return render(request,'register.html',{'form': form})
def profile(request):
    if request.method == 'POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,
                                 request.FILES,
                                 instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account Has Been UPDAED!!')
            return redirect('profile')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)
    context ={
        'u_form':u_form,
        'p_form': p_form
    }
    return render(request,'profile.html',context)

    
def ecopies(request):
    
    books = Book.objects.all()
    
    
    return render(request,"e-copies.html",{'books': books })





