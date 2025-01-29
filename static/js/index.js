function handleScroll() {
  const elementsToAnimate = document.querySelectorAll('.fromleft, .fromright');
  const windowHeight = window.innerHeight;
  const elementVisible = 150;

  elementsToAnimate.forEach((element) => {
      const elementTop = element.getBoundingClientRect().top;

      if (elementTop < windowHeight - elementVisible && !element.classList.contains('active')) {
          // If the element is within the visible part of the viewport
          // and hasn't been animated yet, add the 'active' class
          element.classList.add('active');
      }
  });


  if (document.querySelectorAll('.fromleft:not(.active), .fromright:not(.active)').length === 0) {
      window.removeEventListener('scroll', handleScroll);
    } 
  }

handleScroll();

window.addEventListener('scroll', handleScroll);