from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Usuário:', required=True,
                               widget=forms.TextInput(attrs={'class': 'border border-gray-300 text-gray-900 font-inter text-sm rounded-lg focus:outline-none focus:border-blue-500 focus:ring-2 w-full p-2.5',
                                                             'placeholder': 'Digite seu usuário'}))
    password = forms.CharField(label='Senha:', max_length=32, required=True,
                               widget=forms.PasswordInput(attrs={'class': 'border border-gray-300 text-gray-900 font-inter text-sm rounded-lg focus:outline-none focus:border-blue-500 focus:ring-2 w-full p-2.5',
                                                                 'placeholder': 'Digite sua senha'}))


class RegisterForm(forms.Form):
    username = forms.CharField(label='Usuário:', required=True,
                               widget=forms.TextInput(attrs={'class': 'border border-gray-300 text-gray-900 font-inter text-sm rounded-lg focus:outline-none focus:border-blue-500 focus:ring-2 w-full p-2.5',
                                                             'placeholder': 'Digite seu usuário'}))
    email = forms.CharField(label='Email:', required=True,
                            widget=forms.EmailInput(attrs={'class': 'border border-gray-300 text-gray-900 font-inter text-sm rounded-lg focus:outline-none focus:border-blue-500 focus:ring-2 w-full p-2.5',
                                                           'placeholder': 'Digite seu e-mail'}))
    password = forms.CharField(label='Senha:', max_length=32,
                               widget=forms.PasswordInput(
                                   attrs={'class': 'border border-gray-300 text-gray-900 font-inter text-sm rounded-lg focus:outline-none focus:border-blue-500 focus:ring-2 w-full p-2.5',
                                          'placeholder': 'Digite sua senha'}), required=True)
    password_confirm = forms.CharField(label='Confirmar senha:', max_length=32,  widget=forms.PasswordInput(attrs={'class': 'border border-gray-300 text-gray-900 font-inter text-sm rounded-lg focus:outline-none focus:border-blue-500 focus:ring-2 w-full p-2.5 ',
                                                                                                                   'placeholder': 'Confirme a senha'}), required=True)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password != password_confirm:
            self.add_error('password_confirm', 'As senhas não correspondem.')
