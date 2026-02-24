window.onload = function() {
    on(); // Display the overlay when the window loads
};

function on() {
    document.getElementById("overlay").style.display = "block";
}

function closeOverlay() {
    document.getElementById("overlay").style.display = "none";
}

// footer-animate.js

function handleFooterScroll() {
    const footer = document.querySelector('footer'); // targets all footer tags on the page
    if (!footer) return; // stop if there’s no footer

    const windowHeight = window.innerHeight;
    const elementVisible = 50;

    const footerTop = footer.getBoundingClientRect().top;

    if (footerTop < windowHeight - elementVisible && !footer.classList.contains('active')) {
        footer.classList.add('active');
    }

    // Once the footer has animated, stop listening
    if (footer.classList.contains('active')) {
        window.removeEventListener('scroll', handleFooterScroll);
    }
}

// Run once on page load in case footer is already visible
handleFooterScroll();

// Listen for scroll events
window.addEventListener('scroll', handleFooterScroll);
