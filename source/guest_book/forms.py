from django import forms


class PageForm(forms.Form):
    author = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=50, required=True)
    note_text = forms.CharField(max_length=1000, required=True, widget=forms.Textarea)
