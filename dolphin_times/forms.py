from django import forms

class DolphinVoteForm(forms.Form):
    voter_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control col-7'}), required=False, max_length=50)
    dolphin_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control col-7'}), required=True, max_length=50)