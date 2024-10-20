from django import forms
from .models import Student

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'
        labels = {
            'student_id':'Student ID',
            'name': 'Name',
            'school': 'School',
            'graduation_year': 'Graduation Year',
            'major': 'Primary Major',
        }

        widgets = {
            'student_id': forms.NumberInput(
                attrs= {'placeholder': 'e.g 1234567', 'class':'form-control'}),
            'name': forms.TextInput(
                attrs={'placeholder': 'e.g. Baldwin', 'class': 'form-control'}),
            'school': forms.TextInput(
                attrs={'placeholder': 'e.g Boston College', 'class': 'form-control'}),
            'graduation_year': forms.Select(
                attrs={'class': 'form-control'}),
            'major': forms.Select(
                attrs={'class': 'form-control'}),
            'minor': forms.Select(
                attrs={'class': 'form-control'}),

        }