// Smooth scrolling using jQuery easing
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault();
    document.querySelector(this.getAttribute("href")).scrollIntoView({
      behavior: "smooth",
    });
  });
});

// Change header background color on scroll
const header = document.getElementById("myHeader");
window.addEventListener("scroll", () => {
  if (window.scrollY > 100) {
    header.style.backgroundColor = "#1c5d34";
  } else {
    header.style.backgroundColor = "rgba(174, 246, 148, 0.15)";
  }
});

// Add click event to close buttons
const closebtns = document.getElementsByClassName("close");
for (let i = 0; i < closebtns.length; i++) {
  closebtns[i].addEventListener("click", function () {
    this.parentElement.style.display = "none";
  });
}

// Toggle profile selection on profile picture click
document
  .getElementById("profile-picture")
  .addEventListener("click", function () {
    var profileSelection = document.getElementById("profile-selection");
    if (
      profileSelection.style.display === "none" ||
      profileSelection.style.display === ""
    ) {
      profileSelection.style.display = "block";
    } else {
      profileSelection.style.display = "none";
    }
  });

function toggleNavbar() {
  var x = document.getElementById("myTopnav");
  var hamburger = document.querySelector(".hamburger-menu");
  var navList = document.querySelector("#myTopnav ul"); // Select the unordered list within the navbar

  if (x.className === "nav") {
    x.className += " responsive";
    hamburger.classList.add("open"); // Add open class
    navList.style.display = "block"; // Display the unordered list
  } else {
    x.className = "nav";
    hamburger.classList.remove("open"); // Remove open class
    navList.style.display = "none"; // Hide the unordered list
  }
}
