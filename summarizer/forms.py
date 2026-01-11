from django import forms

class SummarizerForm(forms.Form):
    pdf_file = forms.FileField(required=False)
    url = forms.URLField(required=False)
    sentence_count = forms.IntegerField(
        min_value=3,
        max_value=10,
        initial=5
    )
