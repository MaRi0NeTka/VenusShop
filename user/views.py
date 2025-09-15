from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse
from .forms import CustomUserUpdateForm, CustomUserLoginForm, CustomUserCreationForm
from django.template.response import TemplateResponse
from .models import CustomUser
from main.models import Product


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, 'Registration successful.')
            return redirect('main:index')
        else:
            form = CustomUserCreationForm()
        return render(request, 'user/register.html', {'form': form})
    

def login_view(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('main:index')
        else:
            form = CustomUserLoginForm()
        return render(request, 'user/login.html', {'form': form})
    

@login_required(login_url='/user/login/')
def profile_view(request):
    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            if request.headers.get('HX-Request'):
                return HttpResponse(headers={'HX-Redirect': reverse('user:profile')})
            return redirect('user:profile')
    else:
        form = CustomUserUpdateForm(instance=request.user)
    recommended_products = Product.objects.all().order_by('id')[:3]
    return TemplateResponse(request,'user/profile.html',
                            {'form': form,
                            'recommended_products': recommended_products
                            })

@login_required(login_url='/user/login/')
def account_details(request):
    user = CustomUser.objects.get(id=request.user.id)
    return TemplateResponse(request, 'user/partials/account_details.html', {'user': user})


@login_required(login_url='/user/login/')
def edit_account_details(request):
    form = CustomUserUpdateForm(instance=request.user)
    return TemplateResponse(request, 'user/partials/account_details.html', {'user': request.user, 'form': form})

@login_required(login_url='/user/login/')
def update_account_details(request):
    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.clean()
            user.save()
            updated_user = CustomUser.objects.get(id=user.id)
            request.user = updated_user
            if request.headers.get('HX-Request'):
                return TemplateResponse(request, 'user/partials/account_details.html', {'user': updated_user})
            return TemplateResponse(request, 'user/partials/account_details.html', {'user': updated_user})
        else:
            return TemplateResponse(request, 'user/partials/edit_account_details.html', {'user': request.user, 'form': form})
    if request.headers.get('HX-Request'):
        return TemplateResponse(headers={'HX-Redirect': reverse('user:profile')})
    
@login_required(login_url='/user/login/')
def logout_view(request):
    logout(request)
    if request.headers.get('HX-Request'):
        return TemplateResponse(headers={'HX-Redirect': reverse('main:index')})
    return redirect('main:index')

