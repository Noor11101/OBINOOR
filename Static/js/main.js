

// contact form
const form = document.querySelector('form');
const first_name = document.getElementById("firstName");
const last_name = document.getElementById("lastName");
const email = document.getElementById("email");
const company= document.getElementById("company");
const message = document.getElementById("message");

function sendEmail() {
  const bodyMessage = `First Name: ${firstName.value} <br> Last Name: ${lastName.value} <br> 
  Email: ${email.value}<br> Company: ${company.value}<br> Message: ${message.value}` ;




  Email.send({
    SecureToken: "e03b94b8-af5e-468d-9ba0-af51ab1abb01" ,
    To: 'nooralhamshari70@gmail.com',
    From: "nooralhamshari70@gmail.com",
    Subject: company.value,
    Body: bodyMessage
  }).then(
    message => {
      if (message == "OK"){
          Swal.fire({
              title: "Success!",
              text: "message sent successfully!",
              icon: "success"
            });
      }
    }
  );
}

form.addEventListener("submit", (e) => {
  e.preventDefault();
  sendEmail();
});




function checkEmail(){
  const emailRegex = /^([a-z\d\.-]+)@([a-z\d-]+)\.([a-z]{2,3})(\.[a-z]{2,3})?$/;

  const errorTxtEmail = document.querySelector(".error-txt.email")

  if (!email.value.match(emailRegex)) {
      email.classList.add("error");
      email.parentElement.classList.add("error");

      if (email.value != "") {
          errorTxtEmail.innerText = "Enter a Valid email address"
      }
      else {
          errorTxtEmail.innerText = "Email Address Can't be blank"



      }
  }
  else {
      email.classList.remove("error");
      email.parentElement.classList.remove("error");
  }
}

form.addEventListener("submit", (e) => {
  e.preventDefault();
  checkInput();

  if (
      !first_name.classList.contains("error") &&
      !last_name.classList.contains("error") &&
      !email.classList.contains("error") &&
      !company.classList.contains("error") &&
      !message.classList.contains("error")
  ) {
      sendEmail();  

      form.reset();
      return false;
  }
});
