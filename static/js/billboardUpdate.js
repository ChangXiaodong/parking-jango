function PrefixInteger(num) {
    return ( "0000" + num ).substr(-4);
}

function time() {
    $.getJSON('/info/ajax_billboard/', function (ret) {
        $.each(ret, function (i, item) {
            var j = PrefixInteger(i + 1);

            if (document.body.clientWidth < 450) {
                element_id = j;
            }
            else{
                element_id = item.id
            }
            document.getElementById(element_id).innerHTML = item.id+"<br>X:" + item.x + "&nbspY:" + item.y;
        });
    })
}

window.onload = function () {
    time();
    setInterval(time, 5000);
    //time();
}