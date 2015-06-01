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
	var mailfrom = $('#mailfromid').val();
    var to = $('#to').val();
	var url_link = $('#url_link').val();
	var description = $('#description').val();
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