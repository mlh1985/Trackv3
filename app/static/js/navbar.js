document.addEventListener('DOMContentLoaded', function() {
    var navbarToggle = document.getElementById('navbar-toggle');
    var navbarSlide = document.getElementById('navbar-slide');
  
    navbarToggle.addEventListener('click', function() {
      if (navbarSlide.classList.contains('open')) {
        navbarSlide.classList.remove('open');
      } else {
        navbarSlide.classList.add('open');
      }
    });
  });
  