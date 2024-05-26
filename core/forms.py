from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .models import Property

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password1', 'password2', 'is_seller', 'is_buyer']




class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'description', 'place', 'area', 'bedrooms', 'bathrooms', 'price', 'hospitals_nearby', 'colleges_nearby']
