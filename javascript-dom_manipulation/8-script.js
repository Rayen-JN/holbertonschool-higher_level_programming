const helloElement = document.querySelector('#hello');

fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return response.json();
  })
  .then(data => {
    helloElement.textContent = data.hello;
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });
