from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Usuário:', required=True,
                               widget=forms.TextInput(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 font-inter text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
                                                             'placeholder': 'Digite seu usuário'}))
    password = forms.CharField(label='Senha:', max_length=32, required=True,
                               widget=forms.PasswordInput(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 font-inter text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
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
