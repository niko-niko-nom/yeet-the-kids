from django.shortcuts import render
from django.contrib import messages
from . import forms, models

# Create your views here.

def kaas(request):
    return render(request, 'kaas.html')

def stem_van_de_week(request):
    form = forms.VoteForm()
    if request.method == "POST":
        form = forms.VoteForm(request.POST)

        if not form.is_valid():
            return render(request, 'kaas_vote.html', { 'form': form })

        try:
            vote = models.Vote(ip=request.META['REMOTE_ADDR'], vote=form.cleaned_data["vote"])
            vote.save()
            messages.add_message(request, messages.SUCCESS, "Added vote")
        except:
            messages.add_message(request, messages.SUCCESS, "Already voted")

    voteModels = list(models.Vote.objects.all())
    votes = []
    total = 0;

    for vote in voteModels:
        while len(votes)-1 < vote.vote:
            votes.append(0)
        v = votes[vote.vote]
        votes[vote.vote] = v+1
        total += 1

    return render(request, 'kaas_vote.html', {'form': form, 'votes': votes, 'total': total})
