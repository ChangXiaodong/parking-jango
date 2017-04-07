function toggle(targetid){
    if (document.getElementById){
        target=document.getElementById(targetid);
            if (target.style.display=="block"){
                target.style.display="none";
            } else {
                target.style.display="block";
            }
    }
}
function enable(targetid){
	if (document.getElementById){
		target=document.getElementById(targetid);
		target.style.display="block";
	}
}

function disable(targetid){
	if (document.getElementById){
		target=document.getElementById(targetid);
		target.style.display="none";
	}
	
}


window.onload = function () {
    if(document.body.clientWidth<450){
		disable("largesize");
		enable("smallsize");
	}
	else{
		disable("smallsize");
		enable("largesize");
	}
}