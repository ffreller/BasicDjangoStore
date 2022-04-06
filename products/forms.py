from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(max_length=120, widget=forms.TextInput(attrs={'placeholder':'Title'})) # max_length = required
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
        'placeholder':'Description',
        'class':'class_name',
        'id':'description',
        'rows':20,
        'cols':40,
        }))
    class Meta:
        model = Product
        fields = [
            "title",
            "description",
            "price",
            "active",
        ]
        
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if "CFE" in title:
            raise forms.ValidationError("Não é um título válido")
        return title
        
        
# class RawProductForm(forms.Form):
#     title = forms.CharField(max_length=120, widget=forms.TextInput(attrs={'placeholder':'Title'})) # max_length = required
#     description = forms.CharField(required=False, )
#     price = forms.DecimalField(max_digits=10, decimal_places=2)
#     active = forms.BooleanField()