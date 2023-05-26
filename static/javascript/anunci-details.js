

const dataContainer = document.getElementById('anunci');
const pk = document.getElementById('ad');

fetch(`/api/anuncis/${ad}/`)
  .then(response => response.json())
  .then(data => {
    console.log(data)
    const anunciElement = document.createElement('div');
    anunciElement.innerHTML = `
      <h1 style="color: black;text-align: center;">${data.titol}</h1>
      <a><img src="${data.foto}" width="500" height="300"></a>
      <p><b>Usuari:</b><a href="/profile/${data.name}">${data.name}</a></p>
      <p><b>Data:</b>${data.data}</p>
      <p>${data.description}</p>
      <p><b>Preu:</b> ${data.preu}€</p>

    `;
    dataContainer.appendChild(anunciElement);
  })
  .catch(error => {
    console.error('Error:', error);
  });
  
  fetch(`/api/comentaris/${ad}/`)
  .then(response => response.json())
  .then(dataResponse => {
    console.log(dataResponse)
    
    if (Array.isArray(dataResponse)) {
      dataResponse.forEach(comment => {
        const objectElement = document.createElement('div');
          objectElement.innerHTML = `
          <h1 style="color: black;text-align: center;">Comentaris</h1>
          <p><a href="/profile/${comment.name}">${comment.name}</a> <b>  ha comentat:</b></p>    
          <p><b>Data:</b> ${comment.data_com}</p>          
          <p>${comment.description}</p>
          <hr>
          `;
          dataContainer.appendChild(objectElement);
      });
    } else {
      const objectElement = document.createElement('div');
      objectElement.innerHTML = `
          <h1 style="color: black;text-align: center;">Comentaris</h1>
          <p><a href="/profile/${dataResponse.name}">${dataResponse.name}</a> <b>  ha comentat:</b></p>    
          <p><b>Data:</b> ${dataResponse.data_com}</p>          
          <p>${dataResponse.description}</p>
          <hr>
          `;
          dataContainer.appendChild(objectElement);
    }
  })
  .catch(error => {
    console.error('Error:', error);
  });