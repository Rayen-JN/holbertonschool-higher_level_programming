const characterElement = document.querySelector('#character');

fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return response.json();
  })
  .then(data => {
    characterElement.textContent = data.name;
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });
