from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control letra-kanit-300'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control letra-kanit-300'}))

class RegistroForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    fecha_nacimiento = forms.DateField(label='Fecha de Nacimiento')
    cedula = forms.IntegerField(label='Cedula')
    email = forms.EmailField(label='Correo Electrónico')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

    # Nuevo campo para el nombre de usuario
    username = forms.CharField(label='Usuario', max_length=100)