from django.forms import ModelForm
from .models import Portfolio
from django import forms
class PortfolioForm(ModelForm):
    class Meta:
        model = Portfolio
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'img': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.TextInput(attrs={'class': 'form-control'}),
            'marital_status': forms.TextInput(attrs={'class': 'form-control'}),
            'nationality': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nationality'}),
            'skills': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Skills'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'linkedin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'LinkedIn Profile URL'}),
            'about': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'about'}),
            'experience': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'experience'}),
            'education': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'education'}),
            'certification': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'certification'}),
            'project_title': forms.TextInput(attrs={'class': 'form-control','placeholder': 'project title'}),
            'project_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'project description'}),
            'project_link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'project link'}),

        }