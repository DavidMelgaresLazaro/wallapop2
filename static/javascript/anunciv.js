const objectList = document.getElementById("anuncis-list");
const dataContainer = document.getElementById('anuncis-list');


//   fetch('/api/anuncis/')
//             .then(response => response.json())
//             .then(data => {
//                 data.forEach((anunci,id) => {
//                     const item = document.createElement('div');
//                     item.innerHTML = `
//                         <div>

//                         <a href="#" id="anunci-${index}">
//                         <img src="${anunci.foto}" width="500" height="300">
//                         </a>
//                         <h2>
//                         <a href="/api/anuncis/${anunci.id}">${anunci.titol}</a>
//                         </h2>
//                         <p>Posted by: ${anunci.name.username}</p>
//                         <p>Date: ${anunci.data}</p>
//                         <p>Description: ${anunci.description}</p>
//                         <p>Price: $${anunci.preu}</p>
//                         <hr>
//                         </div>
//                     `;
//                     dataContainer.appendChild(item);
//                 });
//             })
//             .catch(error => {
//                 console.error('Error:', error);
//             });


            fetch('/api/anuncis/')
            .then(response => response.json())
            .then(data => {
              data.forEach((anunci, index) => {
                const item = document.createElement('div');
                item.innerHTML = `
                  <div>
                    <a href="${anunci.get_absolute_url}">
                      <img src="${anunci.foto}" width="500" height="300">
                    </a>
                    <h2>${anunci.titol}</h2>
                    <p>Posted by: ${anunci.name}</p>
                    <p>Date: ${anunci.data}</p>
                    <p>Description: ${anunci.description}</p>
                    <p>Price: $${anunci.preu}</p>
                    <hr>
                  </div>
                `;
                dataContainer.appendChild(item);
          
                const link = document.getElementById(`anunci-${index}`);
                link.addEventListener('click', () => {
                  // Handle the click event here
                  console.log(`Clicked on item ${index}`);
                });
              });
            })
            .catch(error => {
              console.error('Error:', error);
            });



