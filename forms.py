from django import forms
from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget

class loginForm(forms.Form):
    field = forms.CharField(widget=forms.TextInput(attrs={'onfocusout': 'focus()', 'onKeyUp': 'submit();','size': 10, 'autofocus': True}))
    #field = forms.CharField()
    #field = forms.CharField(attrs={'autofocus':True})
class PracownikFormConf(forms.Form):
    potwierdzenie = forms.CharField(widget=forms.PasswordInput(attrs={'onfocusout': 'focus()', 'onKeyUp': 'submit();','size': 10, 'autofocus': True}))
class SignatureForm(forms.Form):
    signature = JSignatureField(widget=JSignatureWidget(jsignature_attrs={'undobutton' : 'yes'}))
    #JSIGNATURE_WIDTH (width)
    #JSIGNATURE_HEIGHT (height)
    #JSIGNATURE_COLOR (color)
    #JSIGNATURE_BACKGROUND_COLOR (background-color)
    #JSIGNATURE_DECOR_COLOR (decor-color)
    #JSIGNATURE_LINE_WIDTH (lineWidth)
    #JSIGNATURE_UNDO_BUTTON (UndoButton)
    #JSIGNATURE_RESET_BUTTON (ResetButton)
class LoginForm2(forms.Form):
        user = forms.CharField(label='LOGIN')
        password = forms.CharField(label='HASŁO', widget=forms.PasswordInput)
