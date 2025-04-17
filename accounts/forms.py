from django import forms
from allauth.account.forms import SignupForm, LoginForm

class CustomSignupForm(SignupForm):
    
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id':'first-name'}))
    
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id':'last-name'}))
    
    age = forms.IntegerField(required=True, label='Age', widget=forms.NumberInput(attrs={'class': 'form-control', 'id':'age', 'type':'number', 'min':'10'}))
    
    phone_number = forms.CharField(required=False, max_length=15, widget=forms.TextInput(attrs={'class':'form-control','id':'phone', 'type':'tel','placeholder':'e.g. +91 123456789'}))
    
    notifications = forms.BooleanField(required=False )
    agree = forms.BooleanField(required=True)

    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'id':'username'})
        
        self.fields['email'].widget = forms.EmailInput(attrs={
            'placeholder': 'Your email address',
            'class': 'form-control'
        })
        
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'id':'password', 'type':'password'})
        
        self.fields['password2'].widget =  forms.PasswordInput(attrs={'class': 'form-control', 'id':'confirm-password', 'type':'password'})
        
    def save(self, request):
        user = super().save(request)
        user.age = self.cleaned_data['age']
        user.phone_number = self.cleaned_data['phone_number']
        user.notifications = self.cleaned_data['notifications']
        user.agree= self.cleaned_data['agree']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user
    


class CustomLoginForm(LoginForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['login'].widget = forms.TextInput(attrs={'class': 'form-control', 'id':'username', 'type':'text'})
        
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'id':'password', 'type':'password'})
        
    
    