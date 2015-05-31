/*
var logInField = document.getElementById("logInField"),
	username = document.createElement("input"),
	password = document.createElement("input");
	
username.id = "usernameTextBox";
username.type = "text";

password.id = "password";
password.type = "password";

var inputs  = append

document.getElementById("login").onclick = function(){
	logInField.appendChild(username);
	logInField.appendChild(password);
}
*/


function sing_in_prompt()
{
	var username = prompt("Log In\n\nPlease enter your username:");
	
	while (username.length < 6)
	{
		alert("Username should contain at least 6 char");
		username = prompt("Log In\n\nPlease enter your username:");
	}
	
		//--!!-- check if username exists in database --!!--
		
	var password = prompt("Password:");
		
	if (password.length > 5)
	{
		//--!!-- check if password matches username --!!--
	}
}