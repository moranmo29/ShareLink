function sendEmail(){
	/*
	var email = document.getElementById("email").value;
	var description = document.getElementById("description").value;
	var url = document.getElementById("url").value;
	
	description = "ShareLink: " + description;
	
	var body = "This email was sent to you from ShareLink by the user \"username\"\n" + url;
	*/
	
	//location.href('mailto:' + email + '?subject=' + description + '&body=' + body);
	
	alert("I am an alert box!");
	
	//window.location.href = "http://mail.google.com/mail/?view=cm&fs=1" + "&to=adi8554@gmail.com" + "&su="+escape("link")+"&body="+escape("link");
	
	window.location.href = "mailto:adi8554@gmail.com?" + "cc=korkotyan@gmail.com" + "&subject="+escape("link")+"&body="+escape("link");
}