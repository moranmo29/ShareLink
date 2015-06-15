var memberstogroup= [];


function addMember(){
	var member= $('#member_add').val();
	if(member.length==0)
		return;
	$.ajax({
		url:'/api/add_memebr',
		type:'GET',
		dataType:'json',
        data:{member:member},
		success:function(data, status, xhr) {
			//alert("add contact was success");
			memberstogroup.push(member);
			var text= "<ul>";
			for(index=0;index<memberstogroup.length;index++)
			{
				text+="<li>"+memberstogroup[index]+"</li>";
			}
			text+="</ul>";
			document.getElementById("addmem").innerHTML=text;
			$('#member_add').val("");
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


function deleteGroup(groupid){
	console.log(5+7);
	$.ajax({
		url:'/api/delete_group',
		type:'GET',
		dataType:'json',
        data:{groupid:groupid},
		success:function(data, status, xhr) {
	        alert("success to remove group!\n");
			window.location.reload();
		},
		error:function(xhr, status, error) {
            alert("remove group failed!\n");
			return;
		}
	});
	
}


function addLinkGroup(groupid){
	var des= $('#description_add_to_the_group').val();
	var url_link= $('#url_add_to_the_group').val();
	if(url_link.length==0){
		 alert("must enter url link add to the group.\n");
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


