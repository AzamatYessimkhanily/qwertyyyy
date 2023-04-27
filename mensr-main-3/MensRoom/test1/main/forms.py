from django import forms

class ClothingFilterForm(forms.Form):
    sizes = forms.MultipleChoiceField(choices=(('XXS', 'XXS'), ('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('нет в наличий', 'нет в наличий')), required=False, widget=forms.CheckboxSelectMultiple)
    price_min = forms.DecimalField(max_digits=10, decimal_places=2, required=False)
    price_max = forms.DecimalField(max_digits=10, decimal_places=2, required=False)
