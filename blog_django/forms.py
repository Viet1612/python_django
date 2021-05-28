from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import blog_django.models as UserCre
from django.contrib.auth.hashers import make_password
user_db = UserCre.User
class RegisterForm(UserCreationForm):
    
    # email = forms.EmailField()
    class Meta:
	    model = User
	    fields = ["username", "email", "password1", "password2"]
    # def clean_password2(self):
    #     if 'password1' in self.cleaned_data:
    #         password1 = self.cleaned_data['password1']
            
    #         password2 = self.cleaned_data['password2']
    #         if password1 == password2 and password1:
    #             return password2
    #     raise forms.ValidationError("Mật khẩu không hợp lệ")  
      
    def clean_username(self):
        username = (self.cleaned_data['username'])
        try:
            user_db.objects.get(user_name=username)
        except user_db.DoesNotExist:
            return username
        raise forms.ValidationError("Username is taken. Please choose a different one.")
    
    def clean_email(self):
        email = (self.cleaned_data['email'])
        try:
            user_db.objects.get(email=email)
        except user_db.DoesNotExist:
            return email
        raise forms.ValidationError("Email is taken. Please choose a different one.")


    def save(self):
        user_db.objects.create(user_name=self.cleaned_data['username'], email=self.cleaned_data['email'], passw=make_password(self.cleaned_data['password2']), image='static/image/default.jpg')
