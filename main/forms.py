from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(
        max_length=64,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        max_length=15,
        label='Correo Electrónico',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    mensaje = forms.CharField(
        max_length=64,
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4})
    )

class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    passRepeat = forms.CharField(widget=forms.PasswordInput())