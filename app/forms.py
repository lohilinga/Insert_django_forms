from django import forms

class Student_form(forms.Form):
    Sname=forms.CharField(max_length=100)
    Sid=  forms.IntegerField()
    Semail=forms.EmailField()
    

    

