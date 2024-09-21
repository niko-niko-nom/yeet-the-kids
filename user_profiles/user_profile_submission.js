document.getElementById('profile-data-submission').addEventListener('submit', function(event) {
    // Prevent default form submission
    event.preventDefault();

    // Create a new FormData object with the form's data
    const formData = new FormData(this);

    // Send the form data using fetch or XMLHttpRequest (using fetch here)
    fetch(this.action, {
      method: this.method,
      body: formData
    })
    .then(response => {
      if (response.ok) {
        // Redirect the user to a different page after successful form submission
        window.location.href = "succesful_submission.html";
      } else {
        alert("Form submission failed.");
      }
    })
    .catch(error => {
      console.error("Error:", error);
    });
  });