from django import forms
from .models import CarSell,Comment, YEAR_CHOICES
from .snippets import choices, karobka

class CarSellCreateForm(forms.ModelForm):
    title = forms.CharField( label='Modeli',widget=forms.TextInput( attrs={'class':'form-control','placeholder': 'Mashina modelini kiriting'}))
    categories = forms.CharField(label='Kampaniya', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Campaniya nomini kiriting'}))
    image = forms.ImageField(label='Rasm', widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    location = forms.CharField(label='Joylashuv', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Lakatsiya kiriting'}))
    price = forms.IntegerField(label='Narxi', widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Narxini kiriting'}))
    vat = forms.IntegerField(label='Yurgan',  widget=forms.NumberInput(attrs={'class': 'form-control','placeholder':'Qancha km Yurgan'}))
    taste = forms.ChoiceField(label='Yoqilgi', widget=forms.Select(attrs={'class': 'form-control'}),choices=choices)
    persons = forms.ChoiceField(label='Uzatish qutisi', widget=forms.Select(
        attrs={'class': 'form-control'}), choices=karobka)
    details = forms.CharField(label='Qo\'shimcha malumotlar', widget=forms.Textarea(attrs={'class': 'form-control'}))
    year = forms.ChoiceField(label='Yili', widget=forms.Select(attrs={'class': 'form-control'}), choices=YEAR_CHOICES)
    tel = forms.IntegerField(label='Telefon raqam', widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Telefon raqamingizni kiriting'}))
    class Meta:
        model = CarSell
        fields = ['title','image','categories','location','year', 'price','vat','persons' ,'taste','tel' ,'details']
