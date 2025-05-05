// JavaScript for pagination
const pageButtons = document.querySelectorAll('.page-btn');
    
pageButtons.forEach(button => {
  button.addEventListener('click', () => {
    // Remove active class from all buttons
    pageButtons.forEach(btn => btn.classList.remove('active'));
    
    // Add active class to clicked button
    button.classList.add('active');
    
  });
});