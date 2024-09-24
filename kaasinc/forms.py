from django import forms

class VoteForm(forms.Form):
    vote = forms.TypedChoiceField(choices = (
        (0, "Ja, bombardeer Old Amsterdam Kaas (kans op faillissement Kaas Inc.)"),
        (1, "Nee, ga in gesprek met de Old Amsterdam Kaas woordvoerder."),
        (2, "Nee, laat Miku het geheime recept van Old Amsterdam Kaas stelen.")))
