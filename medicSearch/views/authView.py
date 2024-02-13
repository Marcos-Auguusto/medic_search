from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.models import User
from medicSearch.forms.AuthForm import LoginForm, RegisterForm


def login_patient_view(request):
    loginForm = LoginForm()

    if request.user.is_authenticated:
        return redirect('/home-patient')

    if request.method == 'POST':
        loginForm = LoginForm(request.POST)

        if loginForm.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.profile.role == 3:
                    login(request, user)
                    return redirect('/home-patient')
                elif user.profile.role == 2:
                    messages.error(request, 'Acesso não permitido.')
                    return redirect('/login-patient')
                else:
                    return redirect('/admin/')
            else:
                messages.error(
                    request, 'Usuário ou senha incorretos. Por favor, tente novamente.')
                return redirect('/login-patient')
        else:
            messages.error(
                request, 'Por favor, preencha todos os campos corretamente.')
            return redirect('/login-patient')

        #     if user is not None:
        #         login(request, user)
        #         if user.check_password(password):
        #             messages.error(
        #                 request, 'Senha incorreta. Por favor, tente novamente.')

        #             if user.profile.role == 3:
        #                 return redirect('/home-patient')
        #             else:
        #                 messages.error(request, 'Acesso não permitido.')
        #                 return redirect('/')
        #         else:
        #             messages.error(
        #                 request, 'Senha incorreta. Por favor, tente novamente.')
        #     else:
        #         messages.error(
        #             request, 'Usuário não encontrado. Por favor, verifique suas credenciais.')
        # else:
        #     messages.error(
        #         request, 'Por favor, preencha todos os campos corretamente.')

    context = {
        'form': loginForm,
        'button_text': 'Entrar',
        'link_text': 'Registrar',
        'link_href': '/register'
    }

    return render(request, template_name='auth/login.html', context=context, status=200)


def register_view(request):
    registerForm = RegisterForm()
    message = None

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        registerForm = RegisterForm(request.POST)

        if registerForm.is_valid():
            verifyUsername = User.objects.filter(username=username).first()
            verifyEmail = User.objects.filter(email=email).first()

            if verifyUsername is not None:
                message = {'type': 'danger',
                           'text': 'Já existe um usuário com este username!'}

            elif verifyEmail is not None:
                message = {'type': 'danger',
                           'text': 'Já existe um usuário com este e-mail!'}

            else:
                user = User.objects.create_user(username, email, password)
                if user is not None:
                    message = {'type': 'success',
                               'text': 'Conta criada com sucesso!'}

                else:
                    message = {
                        'type': 'danger', 'text': 'Um erro ocorreu ao tentar criar o usuário.'}

    context = {
        'form': registerForm,
        'message': message,
        'title': 'Registrar',
        'button_text': 'Registrar',
        # 'link_text': 'Login',
        'link_href': '/login-patient/'
    }
    return render(request, template_name='auth/register.html', context=context, status=200)


def logout_view(request):
    logout(request)
    return redirect('/')
