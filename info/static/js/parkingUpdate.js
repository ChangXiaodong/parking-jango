function PrefixInteger(num) {
    return ( "0000" + num ).substr(-4);
}

function audioplayer(id, file) {
    var audioplayer = document.getElementById(id);
    if (audioplayer != null) {
        document.body.removeChild(audioplayer);
    }

    if (typeof(file) != 'undefined') {
        if (navigator.userAgent.indexOf("MSIE") > 0) {// IE

            var player = document.createElement('bgsound');
            player.id = id;
            player.src = file['mp3'];
            player.setAttribute('autostart', 'true');
            //if (loop) {
            //    player.setAttribute('loop', 'infinite');
            //}
            document.body.appendChild(player);

        } else { // Other FF Chome Safari Opera

            var player = document.createElement('audio');
            player.id = id;
            player.setAttribute('autoplay', 'autoplay');
            //if (loop) {
            //    player.setAttribute('loop', 'loop');
            //}
            document.body.appendChild(player);

            var mp3 = document.createElement('source');
            mp3.src = file['mp3'];
            mp3.type = 'audio/mpeg';
            player.appendChild(mp3);

            var ogg = document.createElement('source');
            ogg.src = file['ogg'];
            ogg.type = 'audio/ogg';
            player.appendChild(ogg);

            return player;

        }
    }
}

function time() {
    //document.body.clientWidth
    $.getJSON('/info/ajax_parking/', function (ret) {
        $.each(ret, function (i, item) {
            var j = PrefixInteger(i + 1)
            if (item.id == "0000") {
                var file = [];
                //document.getElementById("printf").innerHTML = item.voice;
                file['mp3'] = item.voice;
                player = audioplayer('audioplane', file);

            }
            else {
                if (document.body.clientWidth < 450) {
                    document.getElementById(j).href = "/info/parking-config/?id=" + item.id;
                    if (item.data == 0) {
                        document.getElementById(j).className = "btn btn-normal";
                        document.getElementById(j).innerHTML = item.id + "<br>未停车";
                    }
                    else if (item.data == 253) {
                        document.getElementById(j).className = "btn btn-uncalibrate";
                        document.getElementById(j).innerHTML = item.id + "<br>无信号";
                    }
                    else {
                        document.getElementById(j).className = "btn btn-alert";
                        document.getElementById(j).innerHTML = item.id + "<br>已停车";
                    }
                }
                else {
                    if (item.data == 0) {
                        document.getElementById(item.id).className = "btn btn-normal";
                        document.getElementById(item.id).innerHTML = item.id + "<br>未停车";
                        ;
                    }
                    else if (item.data == 253) {
                        document.getElementById(item.id).className = "btn btn-uncalibrate";
                        document.getElementById(item.id).innerHTML = item.id + "<br>无信号";
                    }
                    else {
                        document.getElementById(item.id).className = "btn btn-alert";
                        document.getElementById(item.id).innerHTML = item.id + "<br>已停车";
                    }
                }
            }
        });
    })
}

window.onload = function () {
    time();
    setInterval(time, 1000);
}

function play() {
    var file = [];
    file['mp3'] = '/static/audios/voice.mp3';
    player = audioplayer('audioplane', file, false); // 播放
    player.onended = function () {
        player.src = '';
    }
}
