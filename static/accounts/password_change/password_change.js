
// Toggle password visibility
const current_password = document.getElementById('id_oldpassword');
const toggle_current_password = document.getElementById('toggle-current-password');

const new_password = document.getElementById('id_password1');
const toggle_new_password = document.getElementById('toggle-new-password');

const new_password_again = document.getElementById('id_password2');
const toggle_password_again = document.getElementById('toggle-password-again');

toggle_current_password.addEventListener('click', function() {
  const type = current_password .getAttribute('type') === 'password' ? 'text' : 'password';
  current_password .setAttribute('type', type);
  this.textContent = type === 'password' ? 'Show' : 'Hide';
});

toggle_new_password.addEventListener('click', function() {
  const type = new_password.getAttribute('type') === 'password' ? 'text' : 'password';
  new_password.setAttribute('type', type);
  this.textContent = type === 'password' ? 'Show' : 'Hide';
});

toggle_password_again.addEventListener('click', function() {
  const type = new_password_again.getAttribute('type') === 'password' ? 'text' : 'password';
  new_password_again.setAttribute('type', type);
  this.textContent = type === 'password' ? 'Show' : 'Hide';
});



