from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Item, Orders


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
        
class ItemListForm(forms.ModelForm):

    class Meta:
        
        model = Item
        fields = ('title', 'price', 'category', 'label', 'description')

class OrdersForm(forms.ModelForm):

    class Meta:
        model = Orders
        fields = ('quantity',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['quantity'].widget.attrs['min'] = 1