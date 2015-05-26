

$(function() {  //this is jQuery's short notation for "fire all this when page is ready"
   $('#shareMail').on('click', shareMail);
});



function shareMail() {
    var description = $('#description').val();
    var url_link = $('#url').val();
	var email = $('#email').val();
	
	if (url_link.length == 0)
	{
		alert("must enter url link\n");
		return;
	}
	if(!ValidURL(url_link)){
		document.getElementById("url").value = "";
		return;
	}
	

    $.ajax({
		url:'/shareMail',
		type:'GET',
		dataType:'json',
        data:{description:description, url_link:url_link, email:email},
		success:function(data, status, xhr) {
			alert("you ShareLink via email!");
			location.reload();
			return;
		},
		error:function(xhr, status, error) {
            alert("sending failed!\n");
			document.getElementById("description").value = "";
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
