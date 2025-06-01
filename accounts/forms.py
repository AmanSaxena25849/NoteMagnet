from django import forms
from .models import users
from allauth.account.forms import SignupForm, LoginForm, ResetPasswordKeyForm, ReauthenticateForm, SetPasswordForm



class CustomSignupForm(SignupForm):
    
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id':'first-name'}))
    
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id':'last-name'}))
    
    age = forms.IntegerField(required=True, label='Age', widget=forms.NumberInput(attrs={'class': 'form-control', 'id':'age', 'type':'number', 'min':'10'}))
    
    notifications = forms.BooleanField(required=False )
    agree = forms.BooleanField(required=True)


    #adding widgets to custom fields.
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
        user.notifications = self.cleaned_data['notifications']
        user.agree= self.cleaned_data['agree']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user
    


class CustomLoginForm(LoginForm):
    #adding widgets
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['login'].widget = forms.TextInput(attrs={'class': 'form-control', 'id':'username', 'type':'text'})
        
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'id':'password', 'type':'password'})
        
 
     
class CustomResetPasswordKeyForm(ResetPasswordKeyForm):
    #adding widgets
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'id':'password', 'type':'password'})
        
        self.fields['password2'].widget =  forms.PasswordInput(attrs={'class': 'form-control', 'id':'confirm-password', 'type':'password'})
        
   
        
class CustomSetPasswordForm(SetPasswordForm):
    #adding widgets
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'id':'password', 'type':'password'})
        
        self.fields['password2'].widget =  forms.PasswordInput(attrs={'class': 'form-control', 'id':'confirm-password', 'type':'password'})
        


class CustomReauthenticateForm(ReauthenticateForm):
    #adding widgets
     def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['password'].widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'type': 'password',
            'id': 'password'
        })
        
        

class DashboardForm(forms.ModelForm):
    class Meta:
        model = users
        fields = [
            'first_name', 'last_name', 'username', 'age', 'email', 'bio', 'profile_image'
        ]
        
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'first-name', 'readonly': 'true'}),
            
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'last-name', 'readonly': 'true'}),
            
            'username': forms.TextInput(attrs={'class': 'form-control', 'id': 'username', 'readonly': 'true'}),
            
            'age': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'age', 'type': 'number', 'min': '10', 'readonly': 'true'
            }),
            
            'email': forms.EmailInput(attrs={'class': 'form-control', 'readonly': 'true'}),
            
            'bio': forms.Textarea(attrs={'class': 'form-control bio-text', 'id': 'bio', 'readonly': 'true'}),
            
            'profile_image': forms.FileInput(attrs={'class':'note-image', 'id':'note-image', 'type':'file', 'accept':'image/*'})
        }
        
        
