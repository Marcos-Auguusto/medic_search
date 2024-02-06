from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='', required=True,
                               widget=forms.TextInput(attrs={'class': 'border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 w-full h-11 py-2 px-2'}))
    password = forms.CharField(label='', max_length=32, required=True,
                               widget=forms.PasswordInput(attrs={'class': 'border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 w-full h-11 py-2 px-2'}))


class RegisterForm(forms.Form):
    username = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(required=True,
                            widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=32,
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control'}),
                               required=True)
