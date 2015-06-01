
function successAlert() {
	var mailfrom = $('#Email_Address').val();
    var name = $('#Full_Name').val();
	var message = $('#Your_Message').val();
	
	if (name.length == 0)
	{
		alert("must enter your name\n");
		return;
	}

	if (message.length == 0)
	{
		alert("must enter body message link\n");
		return;
	}

	
	if (mailfrom.length == 0)
	{
		alert("must enter the your email address\n");
		return;
	}	
	
	if(!(validateEmail(mailfrom)))
	{
		alert("mail address not valid\n");
		return;
	}
	
	$.ajax({
		url:'/sendcontactus',
		type:'GET',
		dataType:'json',
        data:{mailfrom:mailfrom, name:name, message:message},
		success:function(data, status, xhr) {
            alert("your massege has been send\n thank you!!"); 
			location.reload();
		   //window.location.href = "/contactuspage";	

		},
		error:function(xhr, status, error) {
            alert("the send message failed!!");
			console.error(xhr, status, error);
		}
	});
	
	
}
function validateEmail(email) {
    var re = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i;
    return re.test(email);
}