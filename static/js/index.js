function handleScroll() {
  const observer = new IntersectionObserver(
  (entries, observer) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active');
        observer.unobserve(entry.target); // animate only once
      }
    });
  },
  {
    threshold: 0.1, // triggers when 10% visible
  }
);

document.querySelectorAll('.fromleft, .fromright').forEach((el) => {
  observer.observe(el);
});
  }

handleScroll();

window.addEventListener('scroll', handleScroll);