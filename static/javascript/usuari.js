const objectList = document.getElementById("profile");
const dataContainer = document.getElementById('profile');





            fetch('/api/usuaris/')
            .then(response => response.json())
            .then(data => {
              data.forEach((usuaris, index) => {
                const item = document.createElement('div');
                item.innerHTML = `
                  <div>
                    <a href="${usuaris.User}">
                      <img src="${usuaris.avatar}" width="500" height="300">
                    </a>
                    <h2>${usuaris.name}</h2>
                    <p>Posted by: ${usuaris.name}</p>
                    <p>Adress: ${usuaris.adress}</p>
                    <p>Bio: ${usuaris.bio}</p>
                    <p>Email:: $${usuaris.email}</p>
                    <hr>
                  </div>
                `;
                dataContainer.appendChild(item);
          
                const link = document.getElementById(`usuaris/${index}`);
                link.addEventListener('click', () => {
                  // Handle the click event here
                  console.log(`Clicked on item ${index}`);
                });
              });
            })
            .catch(error => {
              console.error('Error:', error);
            });




