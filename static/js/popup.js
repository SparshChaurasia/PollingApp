function hideAlert() {
    let alert = document.getElementsByClassName("alert");
    alert[0].classList.remove("show");
    alert[0].classList.add("hide");
}

let alertBtn = document.getElementsByClassName("close-btn");
console.log(alertBtn);
alertBtn[0].addEventListener("click", hideAlert); 
