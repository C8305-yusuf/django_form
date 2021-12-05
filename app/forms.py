from django import forms
from .models import StudentModel

# class StudentForm(forms.Form):
#     first_name = forms.CharField(max_length=50)
#     last_name = forms.CharField(max_length=50)
#     number = forms.IntegerField(required=False)

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = ["first_name", "last_name", "number", "profile_pic"]
        labels = {"first_name": "Name"}