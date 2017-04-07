function PrefixInteger(num) {
    return ( "0000" + num ).substr(-4);
}

function time() {

    $.getJSON('/info/ajax_parkingitem/?id='+document.getElementById("nodeid").innerHTML, function (ret) {
		
        $.each(ret, function (i, item) {
			if(item.data == 0){
				document.getElementById("status").innerHTML = "未停车";
			}
			else if(item.data == 1){
				document.getElementById("status").innerHTML = "已停车";
			}
			else if(item.data == 253){
				document.getElementById("status").innerHTML = "掉线";
			}
			else if(item.data == 252){
				document.getElementById("status").innerHTML = "电量低";
			}
			else if(item.data == 251){
				document.getElementById("status").innerHTML = "温度异常";
			}
			else if(item.data == 250){
				document.getElementById("status").innerHTML = "传感器异常";
			}

			document.getElementById("statuscode").innerHTML = "状态码:"+item.data;
			document.getElementById("updatetime").innerHTML = "更新时间:"+item.time;

			if(item.cmd==1){
				document.getElementById("send_data_icon").innerHTML = '  <i class="fa fa-refresh">'
                document.getElementById("s_send_data_icon").innerHTML = '  <i class="fa fa-refresh">'
			}
			else{
				document.getElementById("send_data_icon").innerHTML = ''
                document.getElementById("s_send_data_icon").innerHTML = ''
			}
			if(item.cmd==2){
				document.getElementById("before_cali_icon").innerHTML = '  <i class="fa fa-refresh">'
                document.getElementById("s_before_cali_icon").innerHTML = '  <i class="fa fa-refresh">'
			}
			else{
				document.getElementById("before_cali_icon").innerHTML = ''
                document.getElementById("s_before_cali_icon").innerHTML = ''
			}
			if(item.cmd==3){
				document.getElementById("after_cali_icon").innerHTML = '  <i class="fa fa-refresh">'
                document.getElementById("s_after_cali_icon").innerHTML = '  <i class="fa fa-refresh">'
			}
			else{
				document.getElementById("after_cali_icon").innerHTML = ''
                document.getElementById("s_after_cali_icon").innerHTML = ''
			}
			if(item.cmd==4){
				document.getElementById("reboot_icon").innerHTML = '  <i class="fa fa-refresh">'
                document.getElementById("s_reboot_icon").innerHTML = '  <i class="fa fa-refresh">'
			}
			else{
				document.getElementById("reboot_icon").innerHTML = ''
                document.getElementById("s_reboot_icon").innerHTML = ''
			}
			if(item.cmd==5){
				document.getElementById("stop_icon").innerHTML = '  <i class="fa fa-refresh">'
                document.getElementById("s_stop_icon").innerHTML = '  <i class="fa fa-refresh">'
			}
			else{
				document.getElementById("stop_icon").innerHTML = ''
                document.getElementById("s_stop_icon").innerHTML = ''
			}
			if(item.cmd==6){
				document.getElementById("start_icon").innerHTML = '  <i class="fa fa-refresh">'
                document.getElementById("s_start_icon").innerHTML = '  <i class="fa fa-refresh">'
			}
			else{
				document.getElementById("start_icon").innerHTML = ''
                document.getElementById("s_start_icon").innerHTML = ''
			}
        });
    })
}

window.onload = function () {
	time();
    setInterval(time, 1000);
}
//
//$(document).ready(function () {
//    var nodeid = document.getElementById("nodeid").innerHTML
//        if (document.body.clientWidth < 450) {
//            $("#s_send_data").click(function () {
//                $.get("/info/manhole-cmd/?num=" + nodeid + "&cmd=1", function (ret) {
//                })
//            });
//            $("#s_before_cali").click(function () {
//                $.get("/info/manhole-cmd/?num=" + nodeid + "&cmd=2", function (ret) {
//                })
//            });
//            $("#s_after_cali").click(function () {
//                $.get("/info/manhole-cmd/?num=" + nodeid + "&cmd=3", function (ret) {
//                })
//            });
//            $("#s_reboot").click(function () {
//                $.get("/info/manhole-cmd/?num=" + nodeid + "&cmd=4", function (ret) {
//                })
//            });
//            $("#s_stop").click(function () {
//                $.get("/info/manhole-cmd/?num=" + nodeid + "&cmd=5", function (ret) {
//                })
//            });
//            $("#s_start").click(function () {
//                $.get("/info/manhole-cmd/?num=" + nodeid + "&cmd=6", function (ret) {
//                })
//            });
//        }
//        else {
//            $("#send_data").click(function () {
//                $.get("/info/manhole-cmd/?num=" + nodeid + "&cmd=1", function (ret) {
//                })
//            });
//            $("#before_cali").click(function () {
//                $.get("/info/manhole-cmd/?num=" + nodeid + "&cmd=2", function (ret) {
//                })
//            });
//            $("#after_cali").click(function () {
//                $.get("/info/manhole-cmd/?num=" + nodeid + "&cmd=3", function (ret) {
//                })
//            });
//            $("#reboot").click(function () {
//                $.get("/info/manhole-cmd/?num=" + nodeid + "&cmd=4", function (ret) {
//                })
//            });
//            $("#stop").click(function () {
//                $.get("/info/manhole-cmd/?num=" + nodeid + "&cmd=5", function (ret) {
//                })
//            });
//            $("#start").click(function () {
//                $.get("/info/manhole-cmd/?num=" + nodeid + "&cmd=6", function (ret) {
//                })
//            });
//        }
//
//    });