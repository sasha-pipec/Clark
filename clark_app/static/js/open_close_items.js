function toggleAll() {
    const contents = document.querySelectorAll('.accordion-content');
    contents.forEach(content => {
      content.style.display = (content.style.display === 'block') ? 'none' : 'block';
    });
  }