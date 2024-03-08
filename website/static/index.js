$('a[href^="#"]').on("click", function (event) {
  var target = $(this.getAttribute("href"));
  if (target.length) {
    event.preventDefault();
    $("html, body").stop().animate(
      {
        scrollTop: target.offset().top,
      },
      1000,
      "easeInOutExpo"
    );
  }
});

const header = document.getElementById("myHeader");

window.addEventListener("scroll", () => {
  if (window.scrollY > 100) {
    header.style.backgroundColor = "#1c5d34";
  } else {
    header.style.backgroundColor = "rgba(174, 246, 148, 0.15)";
  }
});

const closebtns = document.getElementsByClassName("close");

// Loop through all close buttons
for (let i = 0; i < closebtns.length; i++) {
  // When a close button is clicked
  closebtns[i].addEventListener("click", function () {
    // Hide the flash message
    this.parentElement.style.display = "none";
  });
}
