const pollData = {
    "Ja, bombardeer groepje één punt nul (kans op faillissement Kaas Inc.)": 20,
    "Nee, ga in gesprek met de Old Amsterdam Kaas": 5.5,
    "Nee, laat Miku het geheime recept van Old Amsterdam Kaas stelen.": 5.5,
    "Ja, bombardeer Old Amsterdam kaas terwijl team één punt nul daar een rondleiding heeft.": 69
};

function submitPoll() {
    const options = document.getElementsByName('poll');
    let selectedValue = null;

    for (const option of options) {
        if (option.checked) {
            selectedValue = option.value;
            break;
        }
    }

    if (selectedValue) {
        // Voeg de stem toe aan de pollData
        pollData[selectedValue]++;
        displayResults();
    } else {
        alert("Kies een optie om te stemmen!");
    }
}

function displayResults() {
    const totalVotes = Object.values(pollData).reduce((total, votes) => total + votes, 0);
    const resultsDiv = document.getElementById('poll-results');
    resultsDiv.innerHTML = "";  // Leeg de vorige resultaten

    for (const [option, votes] of Object.entries(pollData)) {
        const percentage = totalVotes > 0 ? (votes / totalVotes) * 100 : 0;
        // Maak de resultaten dynamisch en gebruik vaste waarden
        const barHTML = `
            <div class="bar">
                <div class="bar-inner" style="width: ${percentage}%;"></div>
                <span>${option} - ${percentage.toFixed(1)}%</span>
            </div>
        `;
        resultsDiv.innerHTML += barHTML;
    }
}