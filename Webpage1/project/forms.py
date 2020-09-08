from django import forms
from .models import Category

class Registration(forms.ModelForm) :
    class Meta :
        model = Category
        fields = ['product','subcateg','category']   
        widgets  = {
            'product' : forms.TextInput(attrs={'class':'form-control'}),
            'subcateg' : forms.TextInput(attrs={'class':'form-control'}),
            'category' : forms.TextInput(attrs={'class':'form-control'})
             ,
        }






