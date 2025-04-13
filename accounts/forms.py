from django import forms
from .models import users

class SignupForm(forms.ModelForm):
    
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control','type':'password','id':'confirm-password'}),
        label='Confirm Password',
        required=True
    )
    
    agree = forms.BooleanField(
        label="I agree to the Terms and Conditions and Privacy Policy",
        required=True,
    )
    
    class Meta:
        model = users
        fields = ['first_name', 'last_name', 'username', 'age', 'email', 'phone_number', 'password', 'notifications']
        
        lables = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'username': 'Username',
            'age': 'Age',
            'email': 'Email Address*',
            'phone_number': 'Phone Number',
            'password': 'Password',
            'notifications': 'Sign up for our newsletter to receive updates and special offers',
        }
        
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'id':'first-name'}),
            
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'id':'last-name'}),
            
            'username': forms.TextInput(attrs={'class': 'form-control', 'id':'username'}),
            
            'age': forms.NumberInput(attrs={'class': 'form-control', 'id':'age', 'type':'number', 'min':'10'}),
            
            'email': forms.EmailInput(attrs={'class': 'form-control','id':'email', 'type':'email'}),
            
            'phone_number': forms.TextInput(attrs={'class':'form-control','id':'phone', 'type':'tel','placeholder':'e.g. (123) 456-7890'}),
            
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'id':'password', 'type':'password'}),
        }
        
        error_messages = {
            'phone_number':{
                'invalid': 'Please enter a valid US phone number.',
            }
        }
        

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match")