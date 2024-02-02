let el_btn = document.getElementById("btn");
el_btn.addEventListener("click", validation);
let el_msg = document.getElementById("message");
let el_1000 = document.getElementById("rad_1000");


function validation(e) {
    let message = ""
    if (el_1000.checked) {
        message = message + "Avec une commande de 1kg, vous avez une réduction !";

    }

    if (document.getElementById("grains").checked) {
        message = message + "Attention, il vous faut un moulin à café !";
    }

    el_msg.textContent = message;
    message.firstChild.nodeValue = message;
}
