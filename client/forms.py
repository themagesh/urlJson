from django import forms

class NameURLForm(forms.Form):
    name1 = forms.CharField(label='Name 1', max_length=100)
    name2 = forms.CharField(label='Name 2', max_length=100)
    name3 = forms.CharField(label='Name 3', max_length=100)
    name4 = forms.CharField(label='Name 4', max_length=100)
    name5 = forms.CharField(label='Name 5', max_length=100)
    name6 = forms.CharField(label='Name 6', max_length=100)
    
    url1 = forms.URLField(label='URL 1', required=False)
    url2 = forms.URLField(label='URL 2', required=False)
    url3 = forms.URLField(label='URL 3', required=False)
    url4 = forms.URLField(label='URL 4', required=False)
    url5 = forms.URLField(label='URL 5', required=False)
