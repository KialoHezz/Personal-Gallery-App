from django.forms import forms,ModelForm
from gallary.models import Image,Location,Category


class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = '__all__'


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'description')


class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = '__all__'