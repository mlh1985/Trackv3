document.addEventListener('DOMContentLoaded', function() {
  var navbarToggle = document.getElementById('navbar-toggle');
  var navbarNav = document.getElementById('navbar-nav');

  navbarToggle.addEventListener('click', function() {
    if (navbarNav.style.display === 'flex') {
      navbarNav.style.display = 'none';
    } else {
      navbarNav.style.display = 'flex';
    }
  });
});
