from django import forms
from bugApp.models import SomeUser

class LoginForm(forms.Form):
    username = forms.CharField(max_length =42)
    password = forms.CharField(widget=forms.PasswordInput)

class RegesterForm(forms.Form):
    username = forms.CharField(max_length =42)
    display_name = forms.CharField(max_length =42)
    password = forms.CharField(widget=forms.PasswordInput)

class TicketAddForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)

class TicketEditForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)
    assigned = forms.ModelChoiceField(queryset=SomeUser.objects.all(),required=False)
    compleated = forms.ModelChoiceField(queryset=SomeUser.objects.all(),required=False)
    choices = [
        ('New','New'),
        ('In Progress','In Progress'),
        ('Done','Done'),
        ('Invalid','Invalid')
    ] 
    status = forms.ChoiceField(choices=choices)