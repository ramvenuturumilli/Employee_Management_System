from django import forms
from .models import user_table,user_auth

class user_table_form(forms.ModelForm):
    
    class Meta:
        model = user_table

        fields =[
            'user_name',
            'first_name',
            'last_name',
            'number',
            'email',
            'designation',
            'department',
        ]

class user_auth_forms(forms.ModelForm):
    class Meta:
        model = user_auth

        fields = [
            'user_name',
            'emailField',
            'password',
        ]