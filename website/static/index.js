$('a[href^="#"]').on("click", function (event) {
  var target = $(this.getAttribute("href"));
  if (target.length) {
    event.preventDefault();
    $("html, body").stop().animate(
      {
        scrollTop: target.offset().top,
      },
      1000,
      "easeInOutExpo",
    );
  }
});

// Get the header element
var header = document.getElementById("myHeader");

// Listen for scroll events
window.addEventListener("scroll", function () {
  // Check scroll position
  if (window.scrollY > 100) {
    // adjust this value based on when you want to change the header
    // Modify the header when scrolled down
    header.style.backgroundColor = "#1c5d34";
  } else {
    // Modify the header when at the top
    header.style.backgroundColor = "rgba(174, 246, 148, 0.15)";
  }
});
