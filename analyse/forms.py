from django import forms

class FileFieldForm(forms.Form):
    uploader = forms.CharField(widget=forms.HiddenInput)
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

