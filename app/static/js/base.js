document.addEventListener("DOMContentLoaded", function () {
    const navbar = document.querySelector(".navbar");
  
    window.onscroll = function () {

      if (navbar && window.scrollY > 0) {
        navbar.classList.add("dark-bg");
      } else if (navbar) {
        navbar.classList.remove("dark-bg");
      }
    };
  });

var homeButton = document.querySelector('#home');
var loginButton = document.querySelector('#login');
var registerButton = document.querySelector('#register');
/* Checking the current route */
var currentRoute = window.location.pathname;

// Check the current route
if (currentRoute === "/" || currentRoute === "/home" || currentRoute === "/index"){
  homeButton.classList.add('highlighted');
} else if (currentRoute === "/login"){
  loginButton.classList.add("highlighted");
} else if (currentRoute === "/register"){
  registerButton.classList.add("highlighted");
}
