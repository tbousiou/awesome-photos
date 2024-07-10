from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import ProfileForm
from django.contrib.auth.models import User
from django.http import Http404
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def profile_view(request, username=None):
    if username:
        profile = get_object_or_404(User, username=username).profile
    else:
        try:
            profile = request.user.profile
        except:
            raise Http404()
    
    posts = profile.user.posts.all()

    context = {
        'profile' : profile,
        'posts': posts,
    }
    
    return render(request, 'profile.html', context)

@login_required
def profile_edit_view(request):
    form = ProfileForm(instance=request.user.profile)

    # If the form is submitted
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')

    # If the user is onboarding after signup   
    if request.path == reverse('profile-onboarding'):
        template = 'profile_onboarding.html'
    # Or if the user is editing their profile
    else:
        template = 'profile_edit.html'

    return render(request, template, {'form': form})

@login_required
def profile_delete_view(request):
    user = request.user
    if request.method == 'POST':
        logout(request)
        user.delete()
        messages.success(request, 'Your account has been deleted.')
        
        return redirect('home-page')

    return render(request, 'profile_delete.html')