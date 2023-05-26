document.getElementById('post-form-comentari').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission

    // Create FormData object to collect form data
    const formData = new FormData(this);
    const date = new Date();


    // Make POST request to the Django REST API endpoint
    fetch('/api/agefir-comentari/', {
      method: 'POST',
      body: formData,
    })
      .then(response => response.json())
      .then(dataResponse => {
        // Handle the response data
        console.log(dataResponse);
        const { description } = dataResponse;
        const name = currentUser;
        const data = date;
        const titol = currentAnunci;


      // Perform desired operations with the extracted data
      // For example, create a new object using the extracted data
        const newAnunci = {
            name,
            titol,
            data,
            description,
        };
        console.log(newAnunci)
      })
      .catch(error => {
        console.error('Error:', error);
      });
  });