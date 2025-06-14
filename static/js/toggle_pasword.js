// Toggle password visibility
function togglePassword(fieldId) {
    const passwordField = document.getElementById(fieldId)
    const eyeIcon = document.getElementById(fieldId + "Eye")
  
    if (passwordField.type === "password") {
      passwordField.type = "text"
      eyeIcon.classList.remove("fa-eye")
      eyeIcon.classList.add("fa-eye-slash")
    } else {
      passwordField.type = "password"
      eyeIcon.classList.remove("fa-eye-slash")
      eyeIcon.classList.add("fa-eye")
    }
  }
  