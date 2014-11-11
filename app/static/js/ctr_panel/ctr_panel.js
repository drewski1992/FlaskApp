$(document).ready(function(){
	setInterval('get_status()', 1000);
});

var get_status = function(){
	$.getJSON('/api_v1/status', null,
		function(data){
			// Display Time
			$('#sys_time').text(data.sys_time);

			// Display Size
			$('#space_used').text(data.space_used);
			$('#space_avail').text(data.space_avail);
			$('#space_fail').text(data.space_fail);
			var space_fail = data.space_fail;
			var space_avail = data.space_avail;
			var space_used = data.space_used;
			var percent_used = (space_used / space_avail)*100;
			var percent_fail = (space_fail / space_avail)*100;
			console.log(percent_used+" "+ percent_fail)
			// $('#space_used_percent').style("width: "+percent_used+"%");
			// $('#space_fail_percent').style("width: "+percent_fail+"%");

			// Operations
			$('#opr_status').text(data.opr_status);
			$('#config_active').text(data.config_active);
			$('#recording').text(data.recording);
		});
}