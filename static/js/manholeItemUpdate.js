function time() {

    $.getJSON('/info/ajax_manholeitem/?id=' + document.getElementById("nodeid").innerHTML, function (ret) {

        $.each(ret, function (i, item) {
            document.getElementById("level").innerHTML = "沉降等级:" + item.level;
            if (item.open_status == "open_false") {
                open_status = "未开启"
            }
            else {
                open_status = "已开启"
            }
            if (item.loss_status == "loss_false") {
                loss_status = "未丢失"
            }
            else {
                loss_status = "已丢失"
            }
            document.getElementById("open_status").innerHTML = "开启状态:" + open_status;
            document.getElementById("loss_status").innerHTML = "丢失状态:" + loss_status;
            document.getElementById("battery").innerHTML = "电池电量:" + item.battery + "%";
            document.getElementById("asypiechart-blue_span").innerHTML = item.battery + "%";
            document.getElementById("easypiechart-blue").setAttribute("data-percent", item.battery);
            document.getElementById("leasypiechart-blue_span").innerHTML = item.battery + "%";
            document.getElementById("leasypiechart-blue").setAttribute("data-percent", item.battery);
            battery_chart = window.chart = $('#leasypiechart-blue').data('easyPieChart');
            battery_chart.update(item.battery);
            battery_easychart = window.chart = $('#easypiechart-blue').data('easyPieChart');
            battery_easychart.update(item.battery);



            document.getElementById("updatetime").innerHTML = "更新时间:" + item.time;
            document.getElementById("leasypiechart-red_span").innerHTML = item.level_num + "%";
            document.getElementById("leasypiechart-red").setAttribute("data-percent", item.level_num);
            danger_chart = window.chart = $('#leasypiechart-red').data('easyPieChart');
            danger_chart.update(item.level_num);



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