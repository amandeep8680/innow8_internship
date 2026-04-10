from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','age','email']

    # def clean_age(self):
    #     age=self.cleaned_data.get('age')
    #     if age < 18:
    #         raise forms.ValidationError("Age must by 18+")
    #     return age
    
    # def clean(self):
    #     cleaned_data = super().clean()
    #     name = cleaned_data.get('name')
    #     email = cleaned_data.get('email')

    #     if name and email:
    #         if name.lower() == "admin" and "gmail" in email:
    #             raise forms.ValidationError("Admin cannot use Gmail")

    #     return cleaned_data