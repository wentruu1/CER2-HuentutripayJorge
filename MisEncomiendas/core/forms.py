from django import forms

class FiltrarResidencia(forms.Form):
    residencia = forms.IntegerField()