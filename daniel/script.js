document.getElementById('admission-form').addEventListener('submit', function (e) {
    e.preventDefault();

    const formData = new FormData(document.getElementById('admission-form'));

    fetch('/api/admission', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Handle the server's response, e.g., display a success message
        console.log(data);
    })
    .catch(error => {
        // Handle errors, e.g., display an error message
        console.error(error);
    });
});
