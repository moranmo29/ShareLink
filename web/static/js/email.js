function sendEmail(){
	/*
	var email = document.getElementById("email").value;
	var description = document.getElementById("description").value;
	var url = document.getElementById("url").value;
	
	description = "ShareLink: " + description;
	
	var body = "This email was sent to you from ShareLink by the user \"username\"\n" + url;
	*/
	
	//location.href('mailto:' + email + '?subject=' + description + '&body=' + body);
	
	window.location.href = "mailto:korkotyan@gmail.com?cc=CCaddress@example.com&subject="+escape("link")+"&body="+escape("link");
}