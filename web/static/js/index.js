// when .modal-wide opened, set content-body height based on browser height; 200 is appx height of modal padding, modal title and button bar

$(".modal-wide").on("show.bs.modal", function() {
  var height = $(window).height() - 200;
  $(this).find(".modal-body").css("max-height", height);
});




$(function() {  //this is jQuery's short notation for "fire all this when page is ready"
    $('#modaltrigger').on('click', submitLogin); // connect between login function and its btn
    $('#signup').on('click', submitsignup);  // connect between login function and its btn
});

function submitLogin() {
    var email = $('#login_email').val(); //taking the value of email textbox
    var password = $('#login_password').val();// taking the value of the password textbox
    $.ajax({ //going the web login gets  the parameters and handel it
		url:'/login', // going to the python function that define as login
		type:'GET', 
		dataType:'json',
        data:{email:email, password:password}, // מעבירים את הפרמטרים האלה בלוגין ומחכים לתשובה
		success:function(data, status, xhr) {
            location.reload(); // התמודדות עם החזרה
		},
		error:function(xhr, status, error) { // אם זה חוזר עם טעות תריץ את הקוד הזה
            alert(xhr.responseText);
			console.error(xhr, status, error);
		}
	});
}

//ההרשמה - 
function submitsignup() {
    var email = $('#signup_email').val();
    var password = $('#signup_password').val();
    $.ajax({
		url:'/register',  // going to the python function that define as login
		type:'GET',
		dataType:'json',
        data:{email:email, password:password},
		success:function(data, status, xhr) {
            location.reload();
		},
		error:function(xhr, status, error) {
            alert(xhr.responseText);
			console.error(xhr, status, error);
		}
	});
}