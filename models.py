# Create your models here.
from django.db import models
from forms import forms
from django.utils import timezone
from jsignature.fields import JSignatureField
class Odziez(models.Model):
    nazwa = models.CharField(max_length=30,blank=True,null=True)
    opis = models.CharField(max_length=255,blank=True,null=False,default="") # previously null=True
    def __str__(self):
        return self.nazwa
class OdziezForm(forms.ModelForm):
    class Meta:
        model = Odziez
        fields = ['nazwa','opis']

    
class Narzedzie(models.Model):
    nazwa = models.CharField(max_length=30,blank=True,null=True)
    opis = models.CharField(max_length=255,blank=True,null=False,default="") # previously null=True
    #waga = models.FloatField(null=True)
    class Meta:
        ordering = ['nazwa'] #### SORTOWANIE
    def __str__(self):
        return str(self.nazwa)
class NarzedzieForm(forms.ModelForm):
    class Meta:
        model = Narzedzie
        fields = ['nazwa','opis']

class Pracownik(models.Model):
    from django.utils import timezone
    nr_pracownika = models.IntegerField(default=0)
    nr_karty = models.IntegerField(default=0)
    nazwisko_imie = models.CharField(max_length=50,blank=True,null=True)
    dzial = models.CharField(max_length=50,blank=True,null=True)
    stanowisko = models.CharField(max_length=50,blank=True,null=True)
    zatrudnienie = models.DateField(auto_now=True)
    spot = models.CharField(max_length=10,blank=True,null=True)
    podgrupa_prac = models.CharField(max_length=50,blank=True,null=True)
    typ_umowy = models.CharField(max_length=50,blank=True,null=True) 
    komentarz = models.CharField(max_length=250,blank=True,null=True)
    potwierdzenie = models.CharField(max_length=50,blank=True,null=True)
    narzedzia = models.TextField(blank=True,null=True)
    zwolniony = models.NullBooleanField(default=False,blank=True,null=True)
    def __str__(self):
        return str(self.nr_pracownika)+" "+str(self.nazwisko_imie)
class PracownikForm(forms.ModelForm):
    class Meta:
        model = Pracownik
        fields = '__all__'
class Pakiet(models.Model):
    dzial = models.CharField(max_length=50,blank=True,null=True)
    poz_1 = models.ForeignKey(Narzedzie,on_delete=None,null=True,related_name='Narzedzie_poz_1')
    #poz_1_n = models.IntegerField(default=1)
    poz_2 = models.ForeignKey(Narzedzie,on_delete=None,null=True,related_name='Narzedzie_poz_2')
    #poz_2_n = models.IntegerField(default=1)
class PakietForm(forms.ModelForm):
    class Meta:
        model = Pakiet
        fields = '__all__'
class Pobranie(models.Model):
    pracownik = models.ForeignKey(Pracownik,on_delete=None,blank=True)
    narzedzie = models.ForeignKey(Narzedzie,on_delete=None,blank=True)
    ilosc = models.IntegerField(default=1)
    data_pobrania=models.DateField(blank=True,null=True,default=timezone.now) ### usuniete () po timezone.now 25-03-2021
    data_oddania=models.DateField(blank=True,null=True)
    oddano = models.NullBooleanField(default=False,blank=True,null=True)
    signature=models.BinaryField(blank=True,null=True)
    sgn=models.CharField(max_length=100,blank=True,null=True)
    opis=models.CharField(max_length=50,blank=True,null=True)
    signature_handy=JSignatureField(null=True,blank=True)
    def __str__(self):
        return self.narzedzie.nazwa+self.pracownik.nazwisko_imie

class PobranieForm(forms.ModelForm):
    class Meta:
        model = Pobranie
        fields = '__all__'
        #def __init__(self, *args, **kwargs):
        #    self.fields['narzedzie'].queryset = Narzedzie.objects.none()
class PobranieOdziez(models.Model):
    pracownik = models.ForeignKey(Pracownik,on_delete=None,blank=True)
    odziez = models.ForeignKey(Odziez,on_delete=None,blank=True)
    ilosc = models.IntegerField(default=1)
    data_pobrania=models.DateField(blank=True,null=True,default=timezone.now())
    data_oddania=models.DateField(blank=True,null=True)
    oddano = models.NullBooleanField(default=False,blank=True,null=True)
    signature=models.BinaryField(blank=True,null=True)
    sgn=models.CharField(max_length=100,blank=True,null=True)
    opis=models.CharField(max_length=50,blank=True,null=True)
    signature_handy=JSignatureField(null=True,blank=True)
    def __str__(self):
        return self.odziez.nazwa+self.pracownik.nazwisko_imie

class PobranieOdziezForm(forms.ModelForm):
    class Meta:
        model = Pobranie
        fields = '__all__'

class Szablon(models.Model):
    dzial = models.CharField(max_length=50)
    wariant = models.CharField(max_length=50,default=".")
    narzedzie = models.ForeignKey(Narzedzie,on_delete=None,blank=True)
    ilosc = models.IntegerField(default=1)
    def __str__(self):
        return self.dzial+self.narzedzie.nazwa
class SzablonForm(forms.ModelForm):
    class Meta:
        model = Szablon
        fields = '__all__'
class SzablonOdziez(models.Model):
    dzial = models.CharField(max_length=50)
    wariant = models.CharField(max_length=50,default=".")
    odziez = models.ForeignKey(Odziez,on_delete=None,blank=True)
    ilosc = models.IntegerField(default=1)
    def __str__(self):
        return self.dzial+self.odziez.nazwa
class SzablonOdziezForm(forms.ModelForm):
    class Meta:
        model = SzablonOdziez
        fields = '__all__'
class Potwierdz(models.Model):
    prac=models.IntegerField(blank=True,null=True)
    def __str__(self):
        return str(self.prac)

class SignatureModel(models.Model):
    signature = JSignatureField() 

