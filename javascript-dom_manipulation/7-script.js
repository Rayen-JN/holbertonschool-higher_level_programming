const listMoviesElement = document.querySelector('#list_movies');

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return response.json();
  })
  .then(data => {
    data.results.forEach(movie => {
      const newListItem = document.createElement('li');
      newListItem.textContent = movie.title;
      listMoviesElement.appendChild(newListItem);
    });
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });
