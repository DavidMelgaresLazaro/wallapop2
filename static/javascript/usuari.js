const dataContainer = document.getElementById('userinfo');

fetch(`/api/users/`)
  .then(response => response.json())
  .then(usuaris => {
    console.log(usuaris)
    const usuarisElement = document.createElement('div');
    usuarisElement.innerHTML = `
      <h1 style="color: black;text-align: center;">${usuaris.username}</h1>
      <a><img src="${usuaris.avatar}" width="500" height="300"></a>
      <p><b>Usuari:</b><a href="/users/${data.name}">${data.name}</a></p>
      <p><b>:</b>${usuaris.phone}</p>
      <p>${usuaris.email}</p>
      <p><b>Bio:</b> ${usuaris.bio}€</p>

    `;
    dataContainer.appendChild(usuarisElement);
  })
  .catch(error => {
    console.error('Error:', error);
  });