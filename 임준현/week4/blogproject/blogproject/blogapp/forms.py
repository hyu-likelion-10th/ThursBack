#장고에서 제공하는 폼기능 구현
from django import forms
from .models import Blog

class BlogForm(forms.Form):
    #입력받고자 하는 값들
    title = forms.CharField()
    body=forms.CharField(widget=forms.Textarea)