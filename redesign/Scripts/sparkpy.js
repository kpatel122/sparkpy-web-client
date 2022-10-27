
/* source: https://www.youtube.com/watch?v=At4B7A4GOPg */

var toggleButton = document.getElementsByClassName('toggle-button')[0];
var navbarLinks = document.getElementsByClassName('navbar-links')[0];

toggleButton.addEventListener('click', () => {
  navbarLinks.classList.toggle('active')
   
})