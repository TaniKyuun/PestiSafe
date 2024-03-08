document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault();

    document.querySelector(this.getAttribute("href")).scrollIntoView({
      behavior: "smooth",
    });
  });
});

let header = document.getElementById("myHeader");

window.addEventListener("scroll", function () {
  if (window.scrollY > 100) {
    header.style.backgroundColor = "#1c5d34";
  } else {
    // Modify the header when at the top
    header.style.backgroundColor = "rgba(174, 246, 148, 0.15)";
  }
});

// Flash message Close Event
// Get all close buttons
let closebtns = document.getElementsByClassName("close");

// Loop through all close buttons
for (var i = 0; i < closebtns.length; i++) {
  // When a close button is clicked
  closebtns[i].addEventListener("click", function () {
    // Hide the flash message
    this.parentElement.style.display = "none";
  });
}
