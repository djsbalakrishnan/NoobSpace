function search(){
	tags = document.getElementById("search-text").value
	if(tags == ""){
		alert("The tags field is empty");
	}
	else{
		$.ajax({
			type:"GET",
			url:"search",
			data:{
				value:tags
			},
			success : function(data) {
				$('#post-list').html(data);
			}
		});
	}
}
