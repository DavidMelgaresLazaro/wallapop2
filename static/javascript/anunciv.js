const objectList = document.getElementById("anuncis-list");

fetch("/api/anuncis")
  .then(response => response.json())
  .then(data => {
    for (let i = 0; i < data.length; i++) {
      const object = data[i];
      const nameItem = document.createElement("li");
      const dataItem = document.createElement("li");
      objectItem.innerText = object.name;
      objectItem.innerText = object.d
      objectList.appendChild(objectItem);
    }
  })
  .catch(error => console.error(error));
