from django import forms

class loginForm(forms.Form):
    field = forms.CharField(widget=forms.TextInput(attrs={'onKeyUp': 'submit();','size': 10, 'autofocus': True}))
    #field = forms.CharField()
    #field = forms.CharField(attrs={'autofocus':True})
class PracownikFormConf(forms.Form):
    potwierdzenie = forms.CharField(widget=forms.TextInput(attrs={'onKeyUp': 'submit();','size': 10, 'autofocus': True}))
