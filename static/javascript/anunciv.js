const objectList = document.getElementById("anuncis-list");

fetch("/api/AnunciViewSet/")
  .then(response => response.json())
  .then(data => {
    for (let i = 0; i < data.length; i++) {
      const object = data[i];
      const objectItem = document.createElement("li");
      objectItem.innerText = object.name;
      objectList.appendChild(objectItem);
    }
  })
  .catch(error => console.error(error));