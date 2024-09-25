document.getElementById('nameForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const name = document.getElementById('name').value;
    window.location.href = `/profiles/${encodeURIComponent(name)}/edit`;
});