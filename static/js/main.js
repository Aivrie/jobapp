// CREATE MODAL

// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("jobBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
btn.onclick = function () {
    modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function () {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}






// UPDATE MODAL

// Get the modal
var modal_edit = document.getElementById("myModalEdit");

// Get the button that opens the modal
var btn_edit = document.getElementById("jobBtnEdit");

// Get the <span> element that closes the modal
var span_edit = document.getElementsByClassName("close-edit")[0];

// When the user clicks on the button, open the modal
btn_edit.onclick = function () {
    modal_edit.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span_edit.onclick = function () {
    modal_edit.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
    if (event.target == modal_edit) {
        modal_edit.style.display = "none";
    }
}