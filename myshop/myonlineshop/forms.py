from .models import Review, Contact
from django import forms
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('name', 'email', 'body','rate')

from django import forms
class EmailPostForm(forms.Form):
    name= forms.CharField(max_length=25)
    name= forms.CharField(max_length=25)
    email= forms.EmailField()
    Message = forms.CharField(required=False, widget=forms.Textarea)

class SearchForm(forms.Form):
    query = forms.CharField(label='Search')

SIZE_CHOICES = (

        ('S', 'Small'),
        ('L', 'Large')
    )




class VariationForm(forms.Form):
    size = forms.TypedChoiceField(required=True, choices=SIZE_CHOICES , widget=forms.RadioSelect, label="Size:")
  

class ContactForm(forms.Form):
    name= forms.CharField(max_length=500, label="Name")
    email= forms.EmailField(max_length=500, label="Email")
    comment= forms.CharField(label='',widget=forms.Textarea(
                        attrs={'placeholder': 'Enter your comment here'}))
    
