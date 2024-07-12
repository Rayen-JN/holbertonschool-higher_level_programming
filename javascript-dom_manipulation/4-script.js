const addItemElement = document.querySelector('#add_item');

addItemElement.addEventListener('click', function() {
  const newListItem = document.createElement('li');
  newListItem.textContent = 'Item';
  const myListElement = document.querySelector('.my_list');
  myListElement.appendChild(newListItem);
});
