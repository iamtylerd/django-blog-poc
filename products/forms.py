from turtle import title
from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title        = forms.CharField(label='',
                        widget=forms.TextInput(attrs={"placeholder": "Your Title"}))
    description  = forms.CharField(
                        required=False, 
                        widget=forms.Textarea(
                            attrs= {
                                "class": "new-class"
                            }
                        )
                    )
    price        = forms.DecimalField(initial=20.33)
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "CFE" in title:
            raise forms.ValidationError("This is not valid")
        return title



class RawProductForm(forms.Form):
    title        = forms.CharField(label='')
    description  = forms.CharField(
                        required=False, 
                        widget=forms.Textarea(
                            attrs= {
                                "class": "new-class"
                            }
                        )
                        )
    price        = forms.DecimalField(initial=20.33)