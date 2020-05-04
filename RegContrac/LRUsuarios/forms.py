from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# Extendemos UserForm del original AuthenticationForm
class UserForm(AuthenticationForm):
    # Ahora el campo username es de tipo email y cambiamos su texto
    username = forms.CharField(label="Usuario", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'id': 'usuario'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password', 'id': 'usuariopass'})

    class Meta:
        model = User
        fields = ["username", "password"]

# Extendemos UserCreateForm del original UserCreationForm
class UserCreateForm(UserCreationForm):
    # Ahora el campo username es de tipo email y cambiamos su texto
    username = forms.CharField(label="Usuario", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'id': 'usuario'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password1', 'id': 'usuariopass1'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password2', 'id': 'usuariopass2'})

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

# Extendemos UserForm del original AuthenticationForm
class UserAdminForm(AuthenticationForm):
    # Ahora el campo username es de tipo email y cambiamos su texto
    username = forms.CharField(label="Usuario", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'id': 'admin'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password', 'id': 'adminpass'})

    class Meta:
        model = User
        fields = ["username", "password"]

# Extendemos UserCreateForm del original UserCreationForm
class UserAdminCreateForm(UserCreationForm):
    # Ahora el campo username es de tipo email y cambiamos su texto
    username = forms.CharField(label="Usuario", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'id': 'admin'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password1', 'id': 'adminpass1'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password2', 'id': 'adminpass2'})

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]