from django import forms

QUANTITY_CHOICE = [(i, str(i)) for i in range( 1, 101)]

class CartForm(forms.Form):
    quantity = forms.TypedChoiceField(choices = QUANTITY_CHOICE, coerce= int)
    update = forms.BooleanField(required = False,
                               initial = False,
                                widget = forms.HiddenInput)