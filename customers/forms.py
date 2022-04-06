from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    name = forms.CharField(max_length=120, widget=forms.TextInput(attrs={'placeholder':'Name'})) # max_length = required
    about_me = forms.CharField(required=False, widget=forms.Textarea(attrs={
        'placeholder':'about_me',
        'class':'class_name',
        'id':'about_me',
        'rows':20,
        'cols':40,
        }))
    class Meta:
        model = Customer
        fields = [
            "name",
            "email",
            "age",
            "about_me",
        ]
        
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if "@" not in email:
            raise forms.ValidationError("Não é um título válido")
        return email