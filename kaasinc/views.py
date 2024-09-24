from django.shortcuts import render
from . import forms, models

# Create your views here.

def kaas(request):
    return render(request, 'kaas.html')

def stem_van_de_week(request):
    if request.method == "POST":
        form = forms.VoteForm(request.POST)

        if not form.is_valid():
            return render(request, 'kaas_vote.html', { 'form': form })

        try:
            vote = models.Vote(ip=request.ip, vote=forms.cleaned_data["vote"])
            vote.save()
        except:
            return render(request, 'kaas_vote.html', {'form': form})
        
        return render(request, 'kaas_vote.html', {'form': form})

    form = forms.VoteForm()
    return render(request, 'kaas_vote.html', {'form': form})
