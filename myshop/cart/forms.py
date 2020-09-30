from django import forms
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 10)]
Size_choice = (
        ('L', 'Large'),
        ('S', 'small'),

)
class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
                                choices=PRODUCT_QUANTITY_CHOICES,
                                coerce=int)
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)

    # size = forms.TypedChoiceField(
    #                             choices=Size_choice
    #                             )

    
