const objectList = document.getElementById("profile_change");
const dataContainer = document.getElementById('profiel_change');





            fetch('/api/usuaris/')
            .then(response => response.json())
            .then(data => {
              data.forEach((usuaris, index) => {
                const item = document.createElement('div');
                item.innerHTML = `
                  <div>
                    <a href="${usuaris.get_absolute_url}">
                      <img src="${usuaris.foto}" width="500" height="300">
                    </a>
                    <h2>${usuaris.titol}</h2>
                    <p>Posted by: ${usuaris.name}</p>
                    <p>Date: ${usuaris.data}</p>
                    <p>Description: ${usuaris.description}</p>
                    <p>Price: $${usuaris.preu}</p>
                    <hr>
                  </div>
                `;
                dataContainer.appendChild(item);
          
                const link = document.getElementById(`profile/${index}`);
                link.addEventListener('click', () => {
                  // Handle the click event here
                  console.log(`Clicked on item ${index}`);
                });
              });
            })
            .catch(error => {
              console.error('Error:', error);
            });




