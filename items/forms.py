from django import forms
from items.models import Item


class ItemForm(forms.ModelForm):
    """ Render and process a form based on the Item model. """
    class Meta:
        model = Item
        fields = ('food_name', 'description', 'is_public')