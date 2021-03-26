from django import forms


class ListaForm(forms.Form):
    lista = forms.CharField(max_length=300, required=False)