from test_pages.models import User
from django.forms import ModelForm


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
