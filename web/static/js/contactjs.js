
function setintheshortmodel(contact_user_email){
	$('#destintion_user').val(contact_user_email);
}



//this delet contact 
function deletecontact(contact_user_email) {
	    $.ajax({
		url:'/deletecontact',
		type:'GET',
		dataType:'json',
        data:{contact_user_email:contact_user_email},
		success:function(data, status, xhr) {
            //alert("contact removed!\n");
			window.location.reload();
			return;
		},
		error:function(xhr, status, error) {
            alert("remove contact failed!\n");
			return;
		}
	});
}


function addContact() {
    var nick_name = $('#nick_name_add').val();
    var contact_user_email = $('#contact_user_email_add').val();

	if (contact_user_email.length == 0)
	{
		alert("must enter email address\n");
		return;
	}
	if (nick_name.length == 0)
	{
		alert("must enter contact name\n");
		return;
	}
	// WE CHECK MAIL VALID????
	//if(!ValidURL(url_link)){
	//	document.getElementById("urladd").value = "";
	//	return;
	//}
	

    $.ajax({
		url:'/addContact',
		type:'GET',
		dataType:'json',
        data:{nick_name:nick_name, contact_user_email:contact_user_email},
		success:function(data, status, xhr) {
			console.log("RELOADING");
			//alert("add contact was sucsess");
			window.location.reload();
			return;
		},
		error:function(xhr, status, error) {
            alert("add contact failed!\n");
			return;
		}
	});
}

function ValidURL(str) {
  var regexp = /(ftp|http|https):\/\/(\w+:{0,1}\w*@)?(\S+)(:[0-9]+)?(\/|\/([\w#!:.?+=&%@!\-\/]))?/
  if(!regexp.test(str)) {
    alert("Please enter a valid URL.");
    return false;
  } else {
    return true;
  }
}
