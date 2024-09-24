from django import forms

class VoteForm(forms.Form):
    vote = forms.ChoiceField(
        widget = forms.RadioSelect,
        choices = (
            (0, "Ja, bombardeer groepje één punt nul (kans op faillissement Kaas Inc.)"),
            (1, "Nee, ga in gesprek met de Old Amsterdam Kaas woordvoerder."),
            (2, "Nee, laat Miku het geheime recept van Old Amsterdam Kaas stelen."),
            (3, "Ja, bombardeer Old Amsterdam Kaas terwijl team één punt nul daar een rondleiding heeft.")
            )
        )
