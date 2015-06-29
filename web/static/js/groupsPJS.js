var memberstogroup= [];
var memberstogroupExsistGroup= [];


function addMember( booleanVar){
	var member= $('#member_add').val();
	var id="addmem";
	if(booleanVar == true){
		member = $('#member_add_exsist_group').val();
		id="addmember";
	}
	if(member.length==0)
		return;
	$.ajax({
		url:'/api/add_memebr',
		type:'GET',
		dataType:'json',
        data:{member:member},
		success:function(data, status, xhr) {
			//alert("add contact was success");
			if (booleanVar){
				memberstogroupExsistGroup.push(member);
				var text= "<ul>";
				for(index=0;index<memberstogroupExsistGroup.length;index++)
				{
					text+="<li>"+memberstogroupExsistGroup[index]+"</li>";
				}
				text+="</ul>";
				$('#member_add_exsist_group').val("");				
			}
			else{
				memberstogroup.push(member);
				var text= "<ul>";
				for(index=0;index<memberstogroup.length;index++)
				{
					text+="<li>"+memberstogroup[index]+"</li>";
				}
				text+="</ul>";
				$('#member_add').val("");
			}				
			document.getElementById(id).innerHTML=text;
			
		return;
			
			
		},
		error:function(xhr, status, error) {
            alert("add person is faild.\n");
			return;
		}
	});
	
	
}


function addGroup(){
	var group_name= $('#group_name_add').val();
	var members= memberstogroup;
	if(group_name.length==0){
		 alert("must enter name group.\n");
		return;
	}
		
	$.ajax({
		url:'/api/create_group',
		type:'GET',
		dataType:'json',
        data:{group_name:group_name, members: JSON.stringify(members)},
		success:function(data, status, xhr) {
			window.location.reload();	
			memberstogroup=[];	
			return;
		},
		error:function(xhr, status, error) {
            alert("create group failed!\n");
			return;
		}
	
	});
}

function cancelGroup(){
	memberstogroup=[];
	window.location.reload();
}
function deleteMemberFromTheGroup(groupid,emailMember){
	$.ajax({
		url:'/api/delete_member_from_the_group',
		type:'GET',
		dataType:'json',
        data:{groupid:groupid,emailMember:emailMember},
		success:function(data, status, xhr) {
			return;
		},
		error:function(xhr, status, error) {
            alert("remove member from the group failed!\n");
			return;
		}
	});

}

function deleteGroup(groupid){
var result = confirm("are you sure you want to delete this group?");
	if (result) {

	$.ajax({
		url:'/api/delete_group',
		type:'GET',
		dataType:'json',
        data:{groupid:groupid},
		success:function(data, status, xhr) {
			window.location.href="/mygroups";
			return;
		},
		error:function(xhr, status, error) {
            alert("remove group failed!\n");
			return;
		}
	});
	}
}

function addMoreMemberOnExsistGroup(group_id){
	var members= memberstogroupExsistGroup;
	$.ajax({
		url:'/api/add_more_member',
		type:'GET',
		dataType:'json',
        data:{group_id:group_id, members: JSON.stringify(members)},
		success:function(data, status, xhr) {
			window.location.reload();	
			memberstogroupExsistGroup=[];	
			return;
		},
		error:function(xhr, status, error) {
            alert("add members to the group failed!\n");
			return;
		}
	
	});
}


function addLinkGroup(groupid){
	var des= $('#description_add_to_the_group').val();
	var url_link= $('#url_add_to_the_group').val();
	if( url_link.length!=0 && !ValidURL(url_link)){
		return;
	}
		
	$.ajax({
		url:'/api/add_link_group',
		type:'GET',
		dataType:'json',
        data:{des:des, url_link:url_link,groupid:groupid},
		success:function(data, status, xhr) {
			window.location.reload();
			$('#description_add_to_the_group').val("");
			$('#url_add_to_the_group').val("");
			return;
		},
		error:function(xhr, status, error) {
            alert("add link to the group failed!\n");
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


function replaceDiv(){

   d1 = document.getElementById('change_when_press_the_button');
   d2 = document.getElementById('change_when_press_the_button_and_what_to_add');
   if( d2.style.display == "none" )
   {
      d1.style.display = "none";
      d2.style.display = "block";
	  document.getElementById("bigger_the_model").style.width = "620px";
	  document.getElementById("addMore").style.display = "inline";
   }
}
