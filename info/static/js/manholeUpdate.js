function time() {

    $.getJSON('/info/ajax_manhole/', function (ret) {
        $.each(ret, function (i, item) {
            element_id = i + 1;
            if (item.level=="低") {
                document.getElementById(element_id).className = "btn btn-normal";
            }
            else if (item.level=="中") {
                document.getElementById(element_id).className = "btn btn-dangerous";
            }
            else if (item.level=="高") {
                document.getElementById(element_id).className = "btn btn-dis-3";
            }
            else if (item.level=="未知") {
                document.getElementById(element_id).className = "btn btn-unknow";
                item.level = "低"
            }
            open_status = "未开启";
            if (item.open_status == "open_true"){
                document.getElementById(element_id).className = "btn btn-alert";
                open_status = "已开启";
            }

            document.getElementById(element_id).innerHTML = "井盖编号:" + item.id + "<br>"
                +"沉降程度:" + item.level + "<br>"
            + "开启状态:"+open_status;

        });
    })
}

window.onload = function () {
    time();
    setInterval(time, 1000);
}