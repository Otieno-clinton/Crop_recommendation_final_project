//||
const registration = document.getElementById("registration_form");
registration.addEventListener("submit", async (event) => {
  event.preventDefault();
  const name = document.getElementById("username").value.trim();
  const email = document.getElementById("email").value.trim();
  const contact = document.getElementById("contact").value.trim();
  const password = document.getElementById("password").value.trim();
  const confirm_password = document
    .getElementById("confirm_password")
    .value.trim();

  if (name == "") {
    document.getElementById("error").textContent = "enter your name";
    document.getElementById("error").style.color = "red";
    return;
  } else {
    document.getElementById("error").textContent = "";
  }
  if (contact == "") {
    document.getElementById("contacterror").textContent =
      "fill the contact field";
    document.getElementById("contacterror").style.color = "red";
    return;
  } else {
    document.getElementById("contacterror").textContent = "";
  }

  if (email == "") {
    document.getElementById("berror").textContent = "please fill your email";
    document.getElementById("berror").style.color = "red";
    // const name = document.getElementById("username").style.outlineColor = "red";
    return;
  } else {
    document.getElementById("berror").textContent = "";
  }

  if (password == "") {
    document.getElementById("passworderror").textContent =
      "please input password";
    document.getElementById("passworderror").style.color = "red";
    // const name = document.getElementById("username").style.outlineColor = "red";
    return;
  } else {
    document.getElementById("passworderror").textContent = "";
  }
  if (password !== confirm_password) {
    document.getElementById("passworderror").textContent =
      "password don't match";
    document.getElementById("passworderror").style.color = "red";
    return;
  }
  document.getElementById("passworderror").textContent = "";

  document.getElementById("registration_form").submit();
});

async function login(event) {
  // Prevent the default form submission
  event.preventDefault();
  const login_email = document.getElementById("login_email").value.trim();
  let login_password = document.getElementById("login_password").value.trim();

  //   const loader = document.getElementById("loader");

  // Email validation
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  // Password validation regex (at least 8 characters)
  const passwordRegex = /^.{6,}$/;

  // Validate phone number
  const phoneRegex = /^(07|01)\d{8}$/;

  // Validate email and password

  if (login_email == "" || login_password == "") {
    document.getElementById("login_emptyerror").style.color = "red";
    document.getElementById("login_emptyerror").textContent =
      "Please fill all the fields";
    return;
  } else {
    document.getElementById("login_emptyerror").textContent = "";
  }
  if (!emailRegex.test(login_email)) {
    document.getElementById("login_emailerror").style.color = "red";
    document.getElementById("login_emailerror").textContent =
      "Please provide a valid email address.";
    return;
  } else {
    document.getElementById("login_emailerror").textContent = "";
  }
  if (!passwordRegex.test(login_password)) {
    document.getElementById("login_password").style.color = "red";
    document.getElementById("login_password").textContent =
      "Password must be at least 6 characters.";
    return;
  } else {
    document.getElementById("login_password").textContent = "";
  }

  //   loader.style.display = "block";

  try {
    const response = await fetch("/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ login_email, login_password }),
    });

    // Parse the JSON response
    const result = await response.json();
    // loader.style.display = "none";
    // Display success or error message
    if (result.success) {
      alert("login successful. Click ok proceed to your account");
      //   resetsuccessful(); // You can customize how you want to display the success message
      window.location.href = "/success.html";
    } else {
      // alert(result.error);
      //   errorlogincard(); // You can customize how you want to display the error message
      alert("Login failed. Incorrect details");
    }
  } catch (error) {
    console.error("Error submitting form:", error);
    alert("An error occurred while processing your request. Please try again.");
  }
}

// Attach the event listener to your form outside the function
document.getElementById("login_form").addEventListener("submit", login);
