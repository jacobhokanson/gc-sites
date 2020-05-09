from django import forms

class SearchWord(forms.Form):
    your_search = forms.CharField(label = 'Search word', max_length = 50)

class SignUp(forms.Form):
    #first_name = forms.CharField(label = 'Your First Name', max_length = 50)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Your First Name')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='Your Last Name', max_length = 50)
    sources = [("email", "Email"), ("web", "from a website"), ("IG", "Instagram"),]
    where_did_you_hear = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=sources)
