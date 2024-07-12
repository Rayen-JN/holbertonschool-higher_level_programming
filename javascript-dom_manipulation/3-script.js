const toggleHeaderElement = document.querySelector('#toggle_header');

toggleHeaderElement.addEventListener('click', function() {
  headerElement.classList.toggle('red');
  headerElement.classList.toggle('green');
});
