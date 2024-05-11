// Smooth scrolling using jQuery easing
$('a.js-scroll-trigger[href*="#"]:not([href="#"])').click(function () {
  if (
    location.pathname.replace(/^\//, "") == this.pathname.replace(/^\//, "") &&
    location.hostname == this.hostname
  ) {
    var target = $(this.hash);
    target = target.length ? target : $("[name=" + this.hash.slice(1) + "]");
    if (target.length) {
      $("html, body").animate(
        {
          scrollTop: target.offset().top,
        },
        1000,
        "easeInOutExpo"
      );
      return false;
    }
  }
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
