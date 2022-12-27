from django.shortcuts import render, redirect
from . import forms

def inscription(request):
    form = forms.FormulaireEnregistrement()
    if request.method == 'POST':
        form = forms.FormulaireEnregistrement(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enregistrement')
    return render(request, 'authentication/inscription.html', context={'form': form})
