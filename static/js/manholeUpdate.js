

function time() {

    $.getJSON('/info/ajax_manhole/', function (ret) {
        $.each(ret, function (i, item) {
            element_id = i+1;
            if (Math.abs(item.TMR_data - item.threshold) < 100) {
                document.getElementById(element_id).className = "btn btn-normal";
                document.getElementById(element_id).innerHTML = item.id+"<br>正常";
            }
            else if (Math.abs(item.TMR_data - item.threshold) >= 100) {
                document.getElementById(element_id).className = "btn btn-alert";
                document.getElementById(element_id).innerHTML = item.id+"<br>丢失";
            }

        });
    })
}

window.onload = function () {
    time();
    setInterval(time, 1000);
}