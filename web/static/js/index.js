// when .modal-wide opened, set content-body height based on browser height; 200 is appx height of modal padding, modal title and button bar
$(function() {  //this is jQuery's short notation for "fire all this when page is ready"
   $('#login').on('click', submitLogin);
   $('#register').on('click', submitRegister);
   
});

$(".modal-wide").on("show.bs.modal", function() {
  var height = $(window).height() - 200;
  $(this).find(".modal-body").css("max-height", height);
});

function sendEmail(){
	var mailfrom = $('#mailfrom').val();
    var to = $('#to').val();
	var url_link = $('#url_link').val();
	var description = $('#description').val();
	if (url_link.length == 0)
	{
		alert("must enter url link\n");
		return;
	}
	
	if (to.length == 0)
	{
		alert("must enter the address email destination\n");
		return;
	}
	
	if (mailfrom.length == 0)
	{
		alert("must enter the your name\n");
		return;
	}	
	
	if(!validateEmail(to))
	{
		alert("mail address not valid\n");
		return;
	}
	if(!ValidURL(url_link))
	{
		return;
	}
	
	$.ajax({
		url:'/sendmail',
		type:'GET',
		dataType:'json',
        data:{mailfrom:mailfrom, to:to,url_link:url_link,description:description},
		success:function(data, status, xhr) {
            alert("success!!");            
			location.reload();

		},
		error:function(xhr, status, error) {
            alert("the send email failed!!");
			console.error(xhr, status, error);
		//	window.location.href = "/index";	
		}
	});

}

function validateEmail(email) {
    var re = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i;
    return re.test(email);
}

function submitLogin() {
    var email = $('#login_email').val();
    var password = $('#login_password').val();
    $.ajax({
		url:'/login',
		type:'GET',
		dataType:'json',
        data:{email:email, password:password},
		success:function(data, status, xhr) {
           // location.reload();
		   window.location.href = "/mysavedlinks";	

		},
		error:function(xhr, status, error) {
            alert("the login failed!!");
			console.error(xhr, status, error);
			window.location.href = "/index";	
		}
	});
}

function submitRegister() {
    var email = $('#reg_email').val();
    var password = $('#reg_password').val();
	if ( !validateEmail(email))
	{
		alert("must inter valid email");
		return;
	}
	$.ajax({
		url:'/sign_up_buttom',
		type:'GET',
		dataType:'json',
        data:{email:email, password:password},
		success:function(data, status, xhr) {
		   // location.reload();
		   window.location.href = "/mysavedlinks";	
		},
		error:function(xhr, status, error) {
            alert("sign up failed");
			//alert(xhr.responseText);
			console.error(xhr, status, error);
		}
	});
}


function setsendEmail() {
		$('#url_link').val($('#urlpageindex').val());
		
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