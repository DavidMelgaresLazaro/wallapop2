const dataContainer = document.getElementById('anuncis-list');

fetch('/api/anuncis/')
  .then(response => response.json())
  .then(data => {
    data.forEach(anunci  => {
      const item = document.createElement('div');
      item.innerHTML = `
        <div>
          <a href="anuncis/${anunci.id}"><img src="${anunci.foto}" width="500" height="300"></a>
          <h2>${anunci.titol}</h2> <br>
          <p><b>Usuari:</b><a href="/profile/${anunci.name}">${anunci.name}</a></p>
          <p><b>Data:</b>${anunci.data}</p>
          <p>${anunci.description}</p>
          <p><b>Preu:</b> ${anunci.preu}€</p>
          <hr>
        </div>
      `;
      dataContainer.appendChild(item);
    });
  })
  .catch(error => {
    console.error('Error:', error);
  });