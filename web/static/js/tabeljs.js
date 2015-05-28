function setintheshortmodel(url_link,description){
	$('#descriptionshare').val(description);
	$('#urlshare').val(url_link);
}

function setintheshortmodelsave(url_link,description,from){
	$('#descriptionadd').val(description);
	$('#urladd').val(url_link);
	$('#descriptionadd1').val(description);
	$('#urladd1').val(url_link);
	$('#fromadd').val(from);
}


//this delet link from page saved link
function deletelink(url_link,description,from_link) {
	    $.ajax({
		url:'/deletelink',
		type:'GET',
		dataType:'json',
        data:{description:description, url_link:url_link,from_link:from_link},
		success:function(data, status, xhr) {
			window.location.reload();
			return;
		},
		error:function(xhr, status, error) {
            alert("the remove link from the list failed!\n");
			return;
		}
	});
}

function share(){
	var to_link = $('#usertoshare').val();
    var description = $('#descriptionshare').val();
    var url_link = $('#urlshare').val();
	if (url_link.length == 0)
	{
		alert("must enter url link\n");
		return;
	}
	if (to_link.length == 0)
	{
		alert("must enter the email user that you want to share\n");
		return;
	}
	$.ajax({
		url:'/share',
		type:'GET',
		dataType:'json',
        data:{description:description, url_link:url_link,to_link:to_link},
		success:function(data, status, xhr) {
			alert("send link was sucsess");
			window.location.reload();
			return;
		},
		error:function(xhr, status, error) {
            alert("the add link to the list failed!\n");
			return;
		}
	});
	

}
function addLinkfromnew(from_link){
	var description = $('#descriptionadd1').val();
    var url_link = $('#urladd1').val();
	var from =	$('#fromadd').val();
	addLink();
	deletelink(url_link,description,from);
	window.location.reload();
}
function addLink() {
    var description = $('#descriptionadd').val();
    var url_link = $('#urladd').val();
	
	if (url_link.length == 0)
	{
		alert("must enter url link\n");
		return;
	}
	if(!ValidURL(url_link)){
		document.getElementById("urladd").value = "";
		return;
	}
	

    $.ajax({
		url:'/addLink',
		type:'GET',
		dataType:'json',
        data:{description:description, url_link:url_link},
		success:function(data, status, xhr) {
			window.location.reload();
			return;
		},
		error:function(xhr, status, error) {
            alert("the add link to the list failed!\n");
			document.getElementById("descriptionadd").value = "";
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
