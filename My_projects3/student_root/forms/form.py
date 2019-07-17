from django import forms
from forms.models import Student1

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student1
        fields = ['Students_id','Students_name','email']
