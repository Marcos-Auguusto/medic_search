from django.shortcuts import render, redirect, get_object_or_404
from medicSearch.models import Profile
from django.core.paginator import Paginator
from medicSearch.forms.UserProfileForm import UserProfileForm, UserForm
from django.contrib import messages

def list_profile_view(request, id=None):
    profile = None   

    if id is None and request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user).first()

    elif id is not None:
        profile = Profile.objects.filter(user__id=id).first()

    elif not  request.user.is_authenticated:
        return redirect(to='/')
    
    favorites = profile.show_favorites()

    if len(favorites) > 0:
        paginator = Paginator(favorites, 8)
        page = request.GET.get('page')
        favorites = paginator.get_page(page)
    
    ratings = profile.show_ratings()

    if len(ratings) > 0:
        paginator = Paginator(ratings, 8)
        page = request.GET.get('page')
        ratings = paginator.get_page(page)

    context = {
        'profile': profile,
        'favorites': favorites,
        'ratings': ratings,
    }

    return render(request, template_name='profile.html', context=context, status=200)

def edit_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    emailUnused = True

    if request.method == 'POST':
        profileForm = UserProfileForm(request.POST, request.FILES, instance=profile)
        userForm = UserForm(request.POST, instance=request.user)
        if request.POST['email']:
            verifyEmail = Profile.objects.filter(user__email=request.POST['email']) \
                .exclude(user__id=request.user.id).first()
            emailUnused = verifyEmail is None
        else:
            emailUnused = True

    else:
        profileForm = UserProfileForm(instance=profile)
        userForm = UserForm(instance=request.user)
    
    if request.POST.get('email') is not None:
        if profileForm.is_valid() and userForm.is_valid() and emailUnused:
            profileForm.save()
            userForm.save()
            messages.success(request, 'Dados atualizados com sucesso')
        else:
            if request.method == 'POST':
                if emailUnused:
                    messages.error(request, 'Dados inválidos')
                else:
                    messages.error(request, 'E-mail já usado por outro usuário')
    else:
        if profileForm.is_valid() and userForm.is_valid():
            profileForm.save()
            userForm.save()
            messages.success(request, 'Dados atualizados com sucesso')
            
            if request.method == 'POST':
                messages.error(request, 'Dados inválidos')

    context = {
        'profileForm': profileForm,
        'userForm': userForm,
    }

    return render(request, template_name='user/profile.html', context=context, status=200)