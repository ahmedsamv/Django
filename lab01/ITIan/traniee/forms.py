from django import forms
from .models import *
from course.models import Course

class TranieeForm(forms.Form):
    id = forms.IntegerField(required=True)
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    fees = forms.DecimalField(decimal_places=2, max_digits=10, required=True)
    Traniee_image = forms.ImageField(required=False,label="Cover Image")
    Course = forms.ChoiceField(choices=[(course.id, course.name) for course in Course.objects.all()], required=True)


class TranieeModelForm(forms.ModelForm):
    class Meta:
        model = Traniee
        fields = '__all__'
