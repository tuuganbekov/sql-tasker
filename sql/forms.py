from django import forms


class SqlForm(forms.Form):
    code_editor = forms.CharField(widget=forms.Textarea)
