	var link={From:"moranmo", Description:"Top 10 CSS Table Design" ,Link:"http://codepen.io/anon/pen/bdVyMa"};
	var link1={From:"moranmo", Description:"" ,Link:"http://www.w3.org/Style/Examples/007/evenodd"};
	var link2={From:"liranharari" ,Description:"stackoverflow", Link:"http://stackoverflow.com/questions/19/what-is-the-fastest-way-to-get-the-value-of-%CF%80"};
	var link3={From:"avitol", Description:"in this link have a lot of Examples", Link:"http://www.w3schools.com"};
	var link4={From:"daniel", Description:"create button" ,Link:"http://css3buttongenerator.com/"};
	var links=[link,link1,link2,link3,link4];
	
function writeTheValueInTabel(){
	var index;	
	var text="";

	for (index = 0; index < links.length; index++) {
        text += "<tr><td><strong>" + links[index]["From"]+"</strong></td>"+
				"<td>"+links[index]["Description"]+"</td>"+
				"<td><a href=\""+ links[index]["Link"] + "\" target=\"_blank\">"+ links[index]["Link"] +"</a></td>"+
				
				"<td><div class=\"listingbtns\"><span class=\"listbuttons\">"+
				"<a type=\"button\" id=\""+index+"\" data-toggle=\"modal\" href=\"#shortModaladdmylist\">SaveLink</a></span>"+
				"<span class=\"listbuttons\">"+
				"<a href=\"#\">Delete</a></span>"+"</div></td></tr>";	
    }
	document.write(text);
}

$(function() {  //this is jQuery's short notation for "fire all this when page is ready"
   $('#addButtonList').on('click', addLink);
	$("a").click(function(e){
		var idClicked = e.target.id;
		$('#descriptionadd').val(links[idClicked]["Description"]);
		$('#urladd').val(links[idClicked]["Link"]);
});
});



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
			alert("susses to add link to the list ");
			location.reload();
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
