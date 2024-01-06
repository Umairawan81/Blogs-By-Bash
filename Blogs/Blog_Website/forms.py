from django import forms

class Comment_form(forms.Form):
    comment = forms.CharField(label="comment" , max_length = 1000)