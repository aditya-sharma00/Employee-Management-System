from django import forms
from .models import Emp  # Import your user model (Emp)

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Emp  # Use your user model
        fields = ['name', 'phone', 'email', 'password', 'cpassword', 'address', 'state', 'country', 'image']
