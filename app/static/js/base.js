document.addEventListener("DOMContentLoaded", function () {
    const navbar = document.querySelector(".navbar");
  
    window.onscroll = function () {
      console.log("Scrolling...");
      console.log("Navbar:", navbar);
  
      if (navbar && window.scrollY > 0) {
        navbar.classList.add("dark-bg");
      } else if (navbar) {
        navbar.classList.remove("dark-bg");
      }
    };
  });
  