const objectList = document.getElementById("anuncis-list");
const dataContainer = document.getElementById('anuncis-list');

// fetch("/api/anuncis")
//   .then(response => response.json())
//   .then(data => {
//     for (let i = 0; i < data.length; i++) {
//       const object = data[i];
//       const nameItem = document.createElement("li");
//       const dataItem = document.createElement("li");
//       objectItem.innerText = object.name;
//       objectItem.innerText = object.d
//       objectList.appendChild(objectItem);
//     }
//   })
//   .catch(error => console.error(error));

  fetch('/api/anuncis/')
            .then(response => response.json())
            .then(data => {
                data.forEach(anunci => {
                    const item = document.createElement('div');
                    item.innerHTML = `
                        <div>
                        <img src="${anunci.foto}" width="500" height="300"></a>
                        <h2>${anunci.titol}</h2>
                        <p>Posted by: ${anunci.name.username}</p>
                        <p>Date: ${anunci.data}</p>
                        <p>Description: ${anunci.description}</p>
                        <p>Price: $${anunci.preu}</p>
                        <hr>
                        </div>
                    `;
                    dataContainer.appendChild(item);
                });
            })
            .catch(error => {
                console.error('Error:', error);
            });
