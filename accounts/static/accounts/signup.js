// JavaScript for mobile navigation
const burger = document.querySelector('.burger');
const sidebar = document.querySelector('.sidebar');
const overlay = document.querySelector('.overlay');
const closeBtn = document.querySelector('.close-btn');

burger.addEventListener('click', () => {
  sidebar.classList.add('active');
  overlay.classList.add('active');
  document.body.style.overflow = 'hidden';
});

function closeSidebar() {
  sidebar.classList.remove('active');
  overlay.classList.remove('active');
  document.body.style.overflow = 'auto';
}

closeBtn.addEventListener('click', closeSidebar);
overlay.addEventListener('click', closeSidebar);

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

// Form validation
const form = document.getElementById('signup-form');

form.addEventListener('submit', function(e) {
  e.preventDefault();
  
  // Reset errors
  document.querySelectorAll('.error-message').forEach(el => el.style.display = 'none');
  
  let isValid = true;
  
  // Validate first name
  const firstName = document.getElementById('first-name').value.trim();
  if (firstName === '') {
    document.getElementById('first-name-error').style.display = 'block';
    isValid = false;
  }
  
  // Validate last name
  const lastName = document.getElementById('last-name').value.trim();
  if (lastName === '') {
    document.getElementById('last-name-error').style.display = 'block';
    isValid = false;
  }
  
  // Validate username
  const username = document.getElementById('username').value.trim();
  if (username.length < 3) {
    document.getElementById('username-error').style.display = 'block';
    isValid = false;
  }
  
  // Validate age
  const age = document.getElementById('age').value;
  if (age < 13) {
    document.getElementById('age-error').style.display = 'block';
    isValid = false;
  }
  
  // Validate email
  const email = document.getElementById('email').value.trim();
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email)) {
    document.getElementById('email-error').style.display = 'block';
    isValid = false;
  }
  
  // Validate phone (optional)
  const phone = document.getElementById('phone').value.trim();
  if (phone !== '') {
    const phoneRegex = /^[\d\s\-\(\)]+$/;
    if (!phoneRegex.test(phone)) {
      document.getElementById('phone-error').style.display = 'block';
      isValid = false;
    }
  }
  
  // Validate password
  const password = document.getElementById('password').value;
  if (password.length < 8) {
    document.getElementById('password-error').style.display = 'block';
    isValid = false;
  }
  
  // Validate confirm password
  const confirmPassword = document.getElementById('confirm-password').value;
  if (password !== confirmPassword) {
    document.getElementById('confirm-password-error').style.display = 'block';
    isValid = false;
  }
  
  // If form is valid, submit
  if (isValid) {
    alert('Account created successfully!');
    // In a real application, this would submit the form data to a server
    form.reset();
  }
});