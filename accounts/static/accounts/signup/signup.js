// Toggle password visibility
const togglePassword = document.getElementById('toggle-password');
const toggleConfirmPassword = document.getElementById('toggle-confirm-password');
const passwordInput = document.getElementById('password');
const confirmPasswordInput = document.getElementById('confirm-password');

togglePassword.addEventListener('click', function() {
  const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
  passwordInput.setAttribute('type', type);
  this.textContent = type === 'password' ? 'Show' : 'Hide';
});

toggleConfirmPassword.addEventListener('click', function() {
  const type = confirmPasswordInput.getAttribute('type') === 'password' ? 'text' : 'password';
  confirmPasswordInput.setAttribute('type', type);
  this.textContent = type === 'password' ? 'Show' : 'Hide';
});

// Password strength checker
const strengthBar = document.getElementById('password-strength-bar');
const strengthText = document.getElementById('password-strength-text');

passwordInput.addEventListener('input', function() {
  const password = this.value;
  const strength = checkPasswordStrength(password);
  updatePasswordStrength(strength);
});

function checkPasswordStrength(password) {
  // Basic password strength checker
  let score = 0;
  
  // Length check
  if (password.length >= 8) score += 20;
  if (password.length >= 12) score += 10;
  
  // Complexity checks
  if (/[a-z]/.test(password)) score += 10;
  if (/[A-Z]/.test(password)) score += 20;
  if (/[0-9]/.test(password)) score += 20;
  if (/[^a-zA-Z0-9]/.test(password)) score += 20;
  
  return score;
}

function updatePasswordStrength(score) {
  let strength, color;
  
  if (score >= 80) {
    strength = 'Strong';
    color = '#4CAF50';
  } else if (score >= 60) {
    strength = 'Good';
    color = '#8BC34A';
  } else if (score >= 40) {
    strength = 'Moderate';
    color = '#FFC107';
  } else if (score >= 20) {
    strength = 'Weak';
    color = '#FF9800';
  } else {
    strength = 'Very Weak';
    color = '#F44336';
  }
  
  strengthBar.style.width = score + '%';
  strengthBar.style.backgroundColor = color;
  strengthText.textContent = 'Password strength: ' + strength;
}

