from .models import Review
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
