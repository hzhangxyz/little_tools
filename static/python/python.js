run=function(){
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET","/python?run="+encodeURIComponent(document.getElementById("in").value), false);
    xmlHttp.send(null);
    document.getElementById("out").value=xmlHttp.responseText;
    return true
}
pre=function(e){
    if((e.keyCode==13)&&(e.shiftKey)){
	run()
	return false
    }
    return true
}
