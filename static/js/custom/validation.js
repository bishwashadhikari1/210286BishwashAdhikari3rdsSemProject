


var emailRegex = new RegExp("^(.+)@(.+)$");
var passRegex = new RegExp("^(?=.[A-Za-z])(?=.\d)[A-Za-z\d]{8,}$");
const form = document.getElementById("form")

form.addEventListener('submit',(e) => {
    document.getElementById("register-username-field").innerHTML = "";
    document.getElementById("register-email-field").innerHTML = "";
    document.getElementById("register-password-field").innerHTML = "";
    document.getElementById("register-api-field").innerHTML = "";




    var username = document.getElementById("inputusername").value ;

    var email = document.getElementById("inputemail").value;
    
    var password = document.getElementById("inputpassword").value;
    var apikey = document.getElementById("inputapikey").value;
    
    var apisecret = document.getElementById("inputapisecret").value;
    console.log(password)
    if ( username == "" ) {
        document.getElementById("register-username-field").innerHTML = "Username is empty";
        e.preventDefault();
    }
    if (email == "") {
        document.getElementById("register-email-field").innerHTML = "Email is empty";
        e.preventDefault();
    }
    if (password == "") {
        document.getElementById("register-password-field").innerHTML = "Please enter a password";
        e.preventDefault();
    }
    if (apikey == "") {
        document.getElementById("register-api-field").innerHTML = "Enter your apis";
        e.preventDefault();
    }
    if (apisecret == "") {
        document.getElementById("register-api-field").innerHTML = "Enter your apis";
        e.preventDefault();
    }

    // else if (!passRegex.test(password)){
    //     document.getElementById("register-password-field").innerHTML = "Enter stronger password";
    //     e.preventDefault();
    // }
    else if (!emailRegex.test(email)){
        document.getElementById("register-emaill-field").innerHTML = "Email address is not valid";
        e.preventDefault();
    }
    else {
        alert("Successfully signed up");
        location.href = "/login" ; 
    }
})