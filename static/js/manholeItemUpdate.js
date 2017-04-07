function time() {

    $.getJSON('/info/ajax_manholeitem/?id=' + document.getElementById("nodeid").innerHTML, function (ret) {

        $.each(ret, function (i, item) {

            if (Math.abs(item.TMR_data - item.threshold) > 100) {
                document.getElementById("status").innerHTML = "井盖丢失";
            }
            else
            {
                document.getElementById("status").innerHTML = "井盖正常";
            }
            document.getElementById("value").innerHTML = "传感器值:" + item.TMR_data;
            document.getElementById("threshold").innerHTML = "阈值:" + item.threshold;
            document.getElementById("updatetime").innerHTML = "更新时间:" + item.time;

            if (item.cmd == 1) {
                document.getElementById("cali_icon").innerHTML = '  <i class="fa fa-refresh">'
                document.getElementById("s_cali_icon").innerHTML = '  <i class="fa fa-refresh">'
            }
            else {
                document.getElementById("cali_icon").innerHTML = ''
                document.getElementById("s_cali_icon").innerHTML = ''
            }
            if (item.cmd == 2) {
                document.getElementById("reboot_icon").innerHTML = '  <i class="fa fa-refresh">'
                document.getElementById("s_reboot_icon").innerHTML = '  <i class="fa fa-refresh">'
            }
            else {
                document.getElementById("reboot_icon").innerHTML = ''
                document.getElementById("s_reboot_icon").innerHTML = ''
            }
            if (item.cmd == 3) {
                document.getElementById("stop_icon").innerHTML = '  <i class="fa fa-refresh">'
                document.getElementById("s_stop_icon").innerHTML = '  <i class="fa fa-refresh">'
            }
            else {
                document.getElementById("stop_icon").innerHTML = ''
                document.getElementById("s_stop_icon").innerHTML = ''
            }
            if (item.cmd == 4) {
                document.getElementById("start_icon").innerHTML = '  <i class="fa fa-refresh">'
                document.getElementById("s_start_icon").innerHTML = '  <i class="fa fa-refresh">'
            }
            else {
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

$(document).ready(function () {
    var nodeid = document.getElementById("nodeid").innerHTML
    if (document.body.clientWidth < 450) {
        $("#s_cali").click(function () {
            $.get("/info/manhole-update-threshold/?id=" + nodeid, function (ret) {
            })
        });
        $("#s_reboot").click(function () {
            $.get("/info/manhole-cmd/?num=" + nodeid + "&cmd=2", function (ret) {
            })
        });
        $("#s_stop").click(function () {
            $.get("/info/manhole-cmd/?num=" + nodeid + "&cmd=3", function (ret) {
            })
        });
        $("#s_start").click(function () {
            $.get("/info/manhole-cmd/?num=" + nodeid + "&cmd=4", function (ret) {
            })
        });
    }
    else {
        $("#cali").click(function () {
            $.get("/info/manhole-update-threshold/?id=" + nodeid, function (ret) {
            })
        });
        $("#reboot").click(function () {
            $.get("/info/manhole-cmd/?num=" + nodeid + "&cmd=2", function (ret) {
            })
        });
        $("#stop").click(function () {
            $.get("/info/manhole-cmd/?num=" + nodeid + "&cmd=3", function (ret) {
            })
        });
        $("#start").click(function () {
            $.get("/info/manhole-cmd/?num=" + nodeid + "&cmd=4", function (ret) {
            })
        });
    }

});