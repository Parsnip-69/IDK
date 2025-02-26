window.onload = function() {
    on(); // Display the overlay when the window loads
};

function on() {
    document.getElementById("overlay").style.display = "block";
}

function closeOverlay() {
    document.getElementById("overlay").style.display = "none";
}

