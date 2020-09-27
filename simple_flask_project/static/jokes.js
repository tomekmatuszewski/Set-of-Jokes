function ShowPunchline(num) {
  document.querySelector(".jokes_set .jokes .punchline-link-" + num).style.display = "none";
  document.querySelector(".jokes_set .jokes .punchline-" + num).style.display = "block";

}