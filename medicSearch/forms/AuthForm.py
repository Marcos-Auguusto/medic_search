from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Usuário:', required=True,
                               widget=forms.TextInput(attrs={'class': 'w-full h-11 border border-neutral-300 rounded-md outline-none px-4 hover:border-blue-500 hover:border-2',
                                                             'placeholder': 'Digite seu usuário'}))
    password = forms.CharField(label='Senha:', max_length=32, required=True,
                               widget=forms.PasswordInput(attrs={'class': 'w-full h-11 border border-neutral-300 rounded-md outline-none px-4 hover:border-blue-500 hover:border-2',
                                                                 'placeholder': 'Digite sua senha'}))


class RegisterForm(forms.Form):
    username = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(required=True,
                            widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=32,
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control'}),
                               required=True)
