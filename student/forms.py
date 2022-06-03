from django import forms
class StudForm(forms.Form):
    s_name=forms.CharField(max_length=30,label='student name')
    s_class=forms.CharField(max_length=30,label='student class')
    s_addr=forms.CharField(max_length=30,label='student address')
    s_school=forms.CharField(max_length=30,label='student school')
    s_email=forms.EmailField(max_length=30,label='student email')
class SForm(forms.Form):
    s_name=forms.CharField(max_length=30,label='student name')
class DForm(forms.Form):
    s_name=forms.CharField(max_length=30,label='student name')