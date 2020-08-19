from django import forms


# has a form that just takes in a text line


class TextlineForm(forms.Form):
    text_line = forms.CharField(max_length=150)
