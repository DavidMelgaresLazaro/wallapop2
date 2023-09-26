document.getElementById('post-form').addEventListener('submit', function (event) {
  event.preventDefault(); // Prevent form submission

  // Create FormData object to collect form data
  const formData = new FormData(this);
  const date = new Date();


  // Make POST request to the Django REST API endpoint
  fetch('/api/anuncis/', {
    method: 'POST',
    body: formData,
  })
    .then(response => response.json())
    .then(dataResponse => {
      // Handle the response data
      const { foto, titol, description, preu } = dataResponse;
      const name = currentUser;
      const data = date;

      // Perform desired operations with the extracted data
      // For example, create a new object using the extracted data
      const newAnunci = {
        foto,
        titol,
        name,
        data,
        description,
        preu
      };
      console.log(newAnunci)
    })
    .catch(error => {
      console.error('Error:', error);
    });
});